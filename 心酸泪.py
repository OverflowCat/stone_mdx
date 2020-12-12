import os
import codecs
chaps = os.listdir("荒唐言")
output = []
for chap in chaps:
  o = []
  charname = chap.split(".")[0]
  o.append(charname) # entry
  print(chap)
  with codecs.open("荒唐言\\" + chap, 'r+', encoding='utf-8') as f:
    text = f.read()
  annotations = [
    ["```(甲戌双行夹批：", '<code class="jd">'],
    ["```(蒙侧批：", '<code class="ms">'],
    ["```(蒙：", '<code class="me">'],
    ["```(庚辰侧批：", '<code class="gs">'],
    ["```(庚辰双行夹批", '<code class="gd">'],
    ["```(庚辰眉批：", '<code class="gb">']
    ["```)", "<code>"]
  ]
  text = ("<small>").join(text.split("```("))
  text = ("</small>").join(text.split(")```"))
  text = ('<br>').join(text.split("\n"))
  o.append(text)
  o.append("</>")
  o = "\n".join(o)
  output.append(o)
output = "\n".join(output)

with codecs.open("stone.txt", 'w+', encoding='utf-8') as f:
  f.write(output)