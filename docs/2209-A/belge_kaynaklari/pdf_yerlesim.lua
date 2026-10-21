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
  elseif count == 4 then
    widths = {0.20, 0.25, 0.47, 0.08}
  elseif count == 3 and label == "Koşul" then
    widths = {0.10, 0.75, 0.15}
  elseif count == 3 and label == "Kişisel kaynak" then
    widths = {0.20, 0.36, 0.44}
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
  local i = 1
  while i <= #blocks do
    local block = blocks[i]
    local caption = blocks[i + 1]
    if block.t == "Para" and #block.content == 1
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
