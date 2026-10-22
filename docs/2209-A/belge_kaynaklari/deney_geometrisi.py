"""Planlanan dört deney koşulunu sayısal koordinatlardan çizer; deney verisi içermez."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/ika-matplotlib-cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'gorseller/akademik_duzen'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.titlesize':12,'axes.labelsize':11,'svg.fonttype':'none'})
navy='#203e5c';blue='#315c83';gray='#dce2e7'
fig,axs=plt.subplots(2,2,figsize=(8.2,7.5),layout='constrained')
route=np.array([[.75,.75],[2.25,.75],[2.25,2.25]])
conditions=[('K0 — Engelsiz referans',None),('K1 — Düz bölüm',(1.40,.75)),('K2 — Dönüş öncesi',(1.75,.75)),('K3 — Dönüş sonrası',(2.25,1.50))]
for ax,(title,obstacle) in zip(axs.flat,conditions):
 ax.set(xlim=(0,3),ylim=(0,3),xlabel='x (m)',ylabel='y (m)');ax.set_aspect('equal');ax.set_title(title,color=navy,fontweight='bold',pad=10)
 ax.set_xticks([0,.75,1.5,2.25,3],labels=['0','0,75','1,50','2,25','3'])
 ax.set_yticks([0,.75,1.5,2.25,3],labels=['0','0,75','1,50','2,25','3'])
 ax.grid(color='#e4e8ec',linewidth=.6);ax.set_axisbelow(True)
 for spine in ax.spines.values():spine.set_color('#8e9ba7');spine.set_linewidth(.8)
 ax.tick_params(labelsize=10,color='#8e9ba7')
 ax.plot(route[:,0],route[:,1],color=blue,linewidth=1.8,linestyle=(0,(4,3)),marker='o',markersize=4,zorder=3)
 for (x,y),label in zip(route,['A','B','C']):ax.annotate(label,(x,y),xytext=(5,7),textcoords='offset points',color=navy,fontweight='bold')
 for p,q in [(route[0],route[1]),(route[1],route[2])]:
  point=p+.72*(q-p);previous=p+.60*(q-p)
  ax.annotate('',xy=point,xytext=previous,arrowprops=dict(arrowstyle='-|>',color=blue,lw=1.5))
 if obstacle:
  x,y=obstacle;ax.add_patch(Rectangle((x-.15,y-.15),.30,.30,facecolor=gray,edgecolor='#455567',linewidth=1,zorder=4))
  ax.plot(x,y,'+',color='#455567',markersize=4,zorder=5)
fig.savefig(OUT/'sekil_3_deney_alani.png',dpi=300,facecolor='white')
fig.savefig(OUT/'sekil_3_deney_alani.pdf',facecolor='white')
fig.savefig(OUT/'sekil_3_deney_alani.svg',facecolor='white')
plt.close(fig)
print('Dört koşulun geometrisi üretildi.')
