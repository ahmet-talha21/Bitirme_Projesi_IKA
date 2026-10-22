"""Sentetik girdilerle ayrık zamanlı durum makinesi ön doğrulaması.

Fiziksel robot, ışın izleme, motor dinamiği veya sensör doğruluğu benzetilmez.
Bu kodda kullanılan mesafe/engel koşulları kontrollü sentetik girdilerdir.
"""
from dataclasses import dataclass
from pathlib import Path
import csv
import json
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/ika-matplotlib-cache')

DT_MS = 50
MAX_AGE_MS = 250
LINK_TIMEOUT_MS = 1000
TASK_LIMIT_MS = 120000
ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Frame:
    time_ms: int
    oldest_measurement_ms: int
    last_heartbeat_ms: int
    obstacle: bool = False
    inside_band: bool = False
    obstacle_behind: bool = False
    full_body_clear: bool = False
    goal_progress_m: float = 0.0
    progress_in_band_m: float = 0.0
    at_final_goal: bool = False


class Controller:
    def __init__(self):
        self.state = 'ROTA'
        self.reason = ''
        self.band_since_ms = None
        self.goal_since_ms = None

    def step(self, frame):
        if self.state in ('TAMAMLANDI', 'DURDURULDU'):
            return self.state
        if frame.time_ms - frame.oldest_measurement_ms > MAX_AGE_MS:
            self.state, self.reason = 'DURDURULDU', 'ESKI_SENSOR_VERISI'
        elif frame.time_ms - frame.last_heartbeat_ms >= LINK_TIMEOUT_MS:
            self.state, self.reason = 'DURDURULDU', 'BAGLANTI_KAYBI'
        elif frame.time_ms >= TASK_LIMIT_MS:
            self.state, self.reason = 'DURDURULDU', 'SURE_ASIMI'
        elif self.state == 'ROTA':
            if frame.obstacle:
                self.state = 'KENAR'
                self.goal_since_ms = None
            elif frame.at_final_goal:
                if self.goal_since_ms is None:
                    self.goal_since_ms = frame.time_ms
                if frame.time_ms - self.goal_since_ms >= 2000:
                    self.state = 'TAMAMLANDI'
            else:
                self.goal_since_ms = None
        elif self.state in ('KENAR', 'DONUS_DOGRULAMA'):
            candidate = (frame.inside_band and frame.obstacle_behind
                         and frame.full_body_clear and frame.goal_progress_m >= .10)
            if not candidate:
                self.state = 'KENAR'
                self.band_since_ms = None
            else:
                if self.band_since_ms is None:
                    self.band_since_ms = frame.time_ms
                self.state = 'DONUS_DOGRULAMA'
                if (frame.time_ms - self.band_since_ms >= 1000
                        and frame.progress_in_band_m >= .10):
                    self.state = 'ROTA'
                    self.band_since_ms = None
        return self.state


def synthetic_frame(case, t):
    # Ölçüm ve canlılık mesajları, hata enjeksiyonu dışında güncel kabul edilir.
    args = dict(time_ms=t, oldest_measurement_ms=t, last_heartbeat_ms=t)
    if case == 'S1':
        args['at_final_goal'] = t >= 2000
    elif case == 'S2':
        args.update(obstacle=1000 <= t < 1200,
                    inside_band=t >= 3000, obstacle_behind=t >= 3000,
                    full_body_clear=t >= 3000,
                    goal_progress_m=.5 if t >= 3000 else 0,
                    progress_in_band_m=max(0, (t-3000)/1000*.05),
                    at_final_goal=t >= 7000)
    elif case == 'S3':
        args.update(obstacle=1000 <= t < 1200, inside_band=t >= 3000,
                    obstacle_behind=True, full_body_clear=True,
                    goal_progress_m=0, progress_in_band_m=.3)
    elif case == 'S4':
        args['oldest_measurement_ms'] = min(t, 1000)
    elif case == 'S5':
        args['last_heartbeat_ms'] = min(t, 1000)
    elif case != 'S6':
        raise ValueError(case)
    return Frame(**args)


def run():
    # İki sınır kontrolü: 250 ms kabul edilir; ilk sonraki denetim 300 ms'de durdurur.
    c = Controller()
    assert c.step(Frame(250, 0, 250)) == 'ROTA'
    assert c.step(Frame(300, 0, 300)) == 'DURDURULDU'
    scenarios = [
        ('S1', 'Engelsiz görev', 5000, 'TAMAMLANDI', ''),
        ('S2', 'Kaçınma ve rotaya dönüş', 10000, 'TAMAMLANDI', ''),
        ('S3', 'İlerlemesiz çizgi kesişimi', 6000, 'KENAR', ''),
        ('S4', 'Eski sensör verisi', 2000, 'DURDURULDU', 'ESKI_SENSOR_VERISI'),
        ('S5', 'Bağlantı kaybı', 2500, 'DURDURULDU', 'BAGLANTI_KAYBI'),
        ('S6', 'Görev süre sınırı', 120050, 'DURDURULDU', 'SURE_ASIMI'),
    ]
    results, transitions, sample_trace = [], [], []
    for code, title, end, expected_state, reason in scenarios:
        c = Controller()
        states = []
        last = None
        for t in range(0, end+1, DT_MS):
            f = synthetic_frame(code, t)
            state = c.step(f)
            states.append(state)
            if state != last:
                transitions.append({'senaryo': code, 'zaman_ms': t,
                                    'durum': state, 'neden': c.reason})
                last = state
            if code == 'S2':
                sample_trace.append({'zaman_ms': t, 'durum': state,
                                     'engel': int(f.obstacle),
                                     'donus_bandinda': int(f.inside_band),
                                     'hedefe_ilerleme_m': f.goal_progress_m,
                                     'bantta_ilerleme_m': round(f.progress_in_band_m, 4)})
        ok = c.state == expected_state and c.reason == reason
        if code == 'S2':
            ok = ok and all(s in states for s in ['KENAR', 'DONUS_DOGRULAMA'])
            return_time = next(x['zaman_ms'] for x in transitions
                               if x['senaryo'] == code and x['durum'] == 'ROTA'
                               and x['zaman_ms'] > 0)
            ok = ok and return_time == 5000
        if code == 'S3':
            ok = ok and 'DONUS_DOGRULAMA' not in states
        assert ok, (code, c.state, c.reason)
        results.append({'kod': code, 'senaryo': title, 'beklenen_durum': expected_state,
                        'gozlenen_durum': c.state, 'neden': c.reason,
                        'kontrol_saglandi': ok})
    artifact = {'tanim': 'Sentetik girdilerle mantıksal ön doğrulama; fiziksel deney değildir.',
                'kontrol_adimi_ms': DT_MS, 'eski_veri_siniri_ms': MAX_AGE_MS,
                'senaryo_sayisi': len(results),
                'saglanan_kontrol': sum(x['kontrol_saglandi'] for x in results),
                'sonuclar': results}
    (ROOT/'sonuclar.json').write_text(json.dumps(artifact, ensure_ascii=False, indent=2)+'\n')
    for name, rows in [('durum_gecisleri.csv', transitions), ('S2_zaman_serisi.csv', sample_trace)]:
        with (ROOT/name).open('w', encoding='utf-8-sig', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=';', lineterminator='\n')
            writer.writeheader(); writer.writerows(rows)
    draw(sample_trace)
    print(json.dumps(artifact, ensure_ascii=False))


def draw(rows):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    matplotlib.rcParams.update({'font.family': 'DejaVu Sans', 'pdf.fonttype': 42,
                                'ps.fonttype': 42, 'font.size': 10})
    labels = ['Rota izleme', 'Kenar izleme', 'Dönüş doğrulama', 'Görev tamamlandı']
    codes = {'ROTA': 0, 'KENAR': 1, 'DONUS_DOGRULAMA': 2, 'TAMAMLANDI': 3}
    fig, ax = plt.subplots(figsize=(8.2, 3.15), layout='constrained')
    ax.step([x['zaman_ms']/1000 for x in rows], [codes[x['durum']] for x in rows],
            where='post', color='#315c83', lw=2)
    ax.set(yticks=range(4), yticklabels=labels, xlabel='Benzetim zamanı (s)',
           xlim=(0, 10), ylim=(-.3, 3.3))
    ax.grid(color='#e4e8ec', lw=.7)
    ax.set_title('S2: Sentetik girdiler altında durum geçişleri', color='#203e5c', fontsize=11)
    for sp in ax.spines.values(): sp.set_color('#879CAE')
    out = ROOT.parent/'gorseller/akademik_duzen'
    for ext in ['png', 'pdf', 'svg']:
        fig.savefig(out/f'sekil_4_on_calisma.{ext}', dpi=300, facecolor='white')
    svg = out/'sekil_4_on_calisma.svg'
    svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
    plt.close(fig)


if __name__ == '__main__':
    run()
