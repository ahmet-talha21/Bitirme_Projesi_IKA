-- Yalnız PDF yerleşimini düzenler; metni ve kaynak görselleri değiştirmez.
function Image(image)
  image.attributes.width = image.src:match("sekil_2") and "13cm" or "16cm"
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
  elseif count == 3 then
    widths = {0.18, 0.34, 0.48}
  end
  if widths then
    for i, width in ipairs(widths) do tbl.colspecs[i][2] = width end
  end
  return tbl
end

function Blocks(blocks)
  local result = pandoc.List()
  local cover_end
  for j, block in ipairs(blocks) do
    if block.t == "RawBlock" and block.text:match("KAPAK SONU") then cover_end = j end
  end
  if cover_end then
    result:insert(pandoc.RawBlock("latex", "\\begin{titlepage}\\centering\\vspace*{15mm}"))
  end
  local i = 1
  while i <= #blocks do
    local block = blocks[i]
    local caption = blocks[i + 1]
    if cover_end and i == cover_end then
      result:insert(pandoc.RawBlock("latex", "\\end{titlepage}\\setcounter{page}{2}"))
      i = i + 1
    elseif cover_end and i < cover_end then
      local label = pandoc.utils.stringify(block)
      if block.t == "Header" then
        result:insert(pandoc.RawBlock("latex", "{\\LARGE\\bfseries TÜBİTAK 2209-A\\par}\\vspace{10mm}"))
      else
        if label:match("^Kullanıcı tarafından") then
          result:insert(pandoc.RawBlock("latex", "\\vspace{8mm}\\begingroup\\Large"))
        end
        result:insert(block)
        if label:match("^Kullanıcı tarafından") then
          result:insert(pandoc.RawBlock("latex", "\\par\\endgroup\\vspace{12mm}"))
        else
          result:insert(pandoc.RawBlock("latex", "\\vspace{6mm}"))
        end
      end
      i = i + 1
    elseif block.t == "Header" and cover_end then
      if block.level == 2 and (pandoc.utils.stringify(block):match("^[123]%.") or pandoc.utils.stringify(block) == "KAYNAKLAR") then
        result:insert(pandoc.RawBlock("latex", "\\clearpage"))
      else
        result:insert(pandoc.RawBlock("latex", caption and caption.t == "Table"
          and "\\Needspace{18\\baselineskip}" or "\\Needspace{6\\baselineskip}"))
      end
      result:insert(block)
      i = i + 1
    elseif block.t == "Para" and #block.content == 1
      and block.content[1].t == "Image" and caption and caption.t == "Para"
      and pandoc.utils.stringify(caption):match("^Şekil [123]%.") then
      result:insert(pandoc.RawBlock("latex", "\\begin{minipage}{\\linewidth}\\centering"))
      result:insert(block)
      result:insert(caption)
      result:insert(pandoc.RawBlock("latex", "\\end{minipage}\\par\\medskip"))
      i = i + 2
    else
      result:insert(block)
      i = i + 1
    end
  end
  return result
end
