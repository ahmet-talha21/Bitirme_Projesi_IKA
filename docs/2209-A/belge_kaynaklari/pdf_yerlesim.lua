-- Yalnız PDF yerleşimini düzenler; metni ve kaynak görselleri değiştirmez.
function Image(image)
  image.attributes.width = "16cm"
  if image.src:match("akademik_duzen/sekil_[34]") then
    image.src = image.src:gsub("%.png$", ".pdf")
  end
  return image
end

function Table(tbl)
  local label = pandoc.utils.stringify(tbl.head.rows[1].cells[1].contents)
  local count = #tbl.colspecs
  local widths
  if count == 2 then
    widths = {0.30, 0.70}
  elseif count == 4 and label == "İP" then
    widths = {0.05, 0.54, 0.30, 0.11}
  elseif count == 4 and label == "Kalem" then
    widths = {0.50, 0.10, 0.20, 0.20}
  elseif count == 4 and label == "Koşul" then
    widths = {0.07, 0.20, 0.64, 0.09}
  elseif count == 5 and label == "Dönem" then
    widths = {0.09, 0.21, 0.14, 0.48, 0.08}
  elseif count == 4 then
    widths = {0.20, 0.25, 0.47, 0.08}
  elseif count == 3 and label == "Koşul" then
    widths = {0.10, 0.75, 0.15}
  elseif count == 3 and label == "Kişisel kaynak" then
    widths = {0.20, 0.36, 0.44}
  elseif count == 3 and label == "Bileşen" then
    widths = {0.22, 0.08, 0.70}
  elseif count == 3 and label == "Risk" then
    widths = {0.24, 0.67, 0.09}
  elseif count == 3 and label == "Ölçüt" then
    widths = {0.22, 0.43, 0.35}
  elseif count == 3 and label == "Çıktı kategorisi" then
    widths = {0.20, 0.37, 0.43}
  elseif count == 3 and label == "Senaryo" then
    widths = {0.10, 0.46, 0.44}
  elseif count == 3 then
    widths = {0.18, 0.34, 0.48}
  end
  if widths then
    for i, width in ipairs(widths) do tbl.colspecs[i][2] = width end
  end
  if not widths then return tbl end
  local specs = {}
  for i, width in ipairs(widths) do
    local align = label == "Kalem" and i >= 3 and "\\raggedleft" or "\\raggedright"
    specs[i] = ">{" .. align .. "\\arraybackslash}p{\\dimexpr" .. width .. "\\linewidth-2\\tabcolsep-2\\arrayrulewidth\\relax}"
  end
  local function row_text(row, heading)
    local cells = {}
    for i, cell in ipairs(row.cells) do
      local value = pandoc.write(pandoc.Pandoc(cell.contents), "latex"):gsub("^%s+", ""):gsub("%s+$", "")
      cells[i] = heading and "\\textbf{" .. value .. "}" or value
    end
    return (heading and "\\rowcolor{TableHead}" or "") .. table.concat(cells, " & ") .. " \\\\ \\hline\n"
  end
  local reserve = label == "Dönem" and "\\Needspace{7cm}" or ""
  local lines = {reserve .. "\\begingroup\\fontsize{9}{10.5}\\selectfont\\setlength{\\tabcolsep}{4pt}\\renewcommand{\\arraystretch}{1.12}",
    "\\arrayrulecolor{TableRule}\\begin{longtable}{|" .. table.concat(specs,"|") .. "|}\\hline"}
  local head = ""
  for _, row in ipairs(tbl.head.rows) do head = head .. row_text(row,true) end
  table.insert(lines, head .. "\\endfirsthead")
  table.insert(lines, head .. "\\endhead")
  for _, body in ipairs(tbl.bodies) do
    for _, row in ipairs(body.head) do table.insert(lines,row_text(row,false)) end
    for _, row in ipairs(body.body) do table.insert(lines,row_text(row,false)) end
  end
  table.insert(lines,"\\end{longtable}\\endgroup")
  return pandoc.RawBlock("latex",table.concat(lines,"\n"))
end

function Div(div)
  if div.classes:includes("ozet") then
    local result = pandoc.List({pandoc.RawBlock("latex","\\begin{tcolorbox}[colback=white,colframe=TableRule,boxrule=0.45pt,arc=0pt,left=5pt,right=5pt,top=4pt,bottom=4pt,breakable]")})
    result:extend(div.content)
    result:insert(pandoc.RawBlock("latex","\\end{tcolorbox}"))
    return result
  end
  return div
end

function Blocks(blocks)
  local result = pandoc.List()
  local cover_end
  for j, block in ipairs(blocks) do
    if block.t == "RawBlock" and block.text:match("KAPAK SONU") then cover_end = j end
  end
  local i = 1
  if cover_end then
    local project_title = ""
    for j = 1, cover_end - 1 do
      local block = blocks[j]
      if block.t == "Para" and pandoc.utils.stringify(block):match("^Kullanıcı ") then
        project_title = pandoc.write(pandoc.Pandoc({block}), "latex")
      end
    end
    assert(project_title ~= "", "Kapakta proje başlığı bulunamadı")
    local cover = [[
\begin{titlepage}\sffamily\centering
\color{BrandNavy}\noindent\rule{\linewidth}{0.65pt}\par
\vspace*{12mm}
\includegraphics[height=32mm]{belge_kaynaklari/varliklar/tubitak_logo.pdf}\par
\vspace{14mm}
{\fontsize{23}{28}\selectfont\bfseries TÜBİTAK 2209-A\par}
\vspace{3mm}
{\fontsize{16}{23}\selectfont\bfseries ÜNİVERSİTE ÖĞRENCİLERİ ARAŞTIRMA\\PROJELERİ DESTEKLEME PROGRAMI\par}
\vspace{10mm}
{\color{TableRule}\rule{0.80\linewidth}{0.5pt}\par}
\vspace{10mm}
{\fontsize{20}{25}\selectfont\bfseries ARAŞTIRMA ÖNERİSİ\par}
\vspace{19mm}
{\fontsize{14}{21}\selectfont ]] .. project_title .. [[\par}
\vspace{14mm}
{\fontsize{10.5}{16}\selectfont\textbf{Proje yürütücüsü:} Ahmet Talha Arslan\\
\textbf{Akademik danışman:} Prof. Dr. Murat Ceylan\\
Konya Teknik Üniversitesi · Elektrik-Elektronik Mühendisliği\par}
\vfill
{\fontsize{14}{18}\selectfont 2026 Yılı\par}
\vspace{10mm}
{\color{TableRule}\rule{\linewidth}{0.5pt}\par}
\end{titlepage}\setcounter{page}{2}
]]
    result:insert(pandoc.RawBlock("latex", cover))
    i = cover_end + 1
  end
  while i <= #blocks do
    local block = blocks[i]
    local caption = blocks[i + 1]
    if block.t == "Header" and cover_end then
      local label = pandoc.utils.stringify(block)
      result:insert(pandoc.RawBlock("latex", (label == "KAYNAKLAR" or label == "6. EKLER")
        and "\\clearpage" or "\\Needspace{6\\baselineskip}"))
      result:insert(block)
      i = i + 1
    elseif block.t == "Para" and #block.content == 1
      and block.content[1].t == "Image" and caption and caption.t == "Para"
      and pandoc.utils.stringify(caption):match("^Şekil [1234]%.") then
      result:insert(pandoc.RawBlock("latex", "\\begin{minipage}{\\linewidth}\\centering"))
      result:insert(block)
      result:insert(pandoc.RawBlock("latex", "\\begingroup\\footnotesize\\color{CaptionInk}"))
      result:insert(caption)
      result:insert(pandoc.RawBlock("latex", "\\endgroup"))
      result:insert(pandoc.RawBlock("latex", "\\end{minipage}\\par\\medskip"))
      i = i + 2
    else
      result:insert(block)
      i = i + 1
    end
  end
  return result
end
