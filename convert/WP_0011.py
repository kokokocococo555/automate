#! python3
# WP_0011.py - google docsからWPへコピーした際のHTMLの整形のため、クリップボードのテキストに以下の変換を行う
# １．<span style="font-weight: 400;">→削除
# ２．</span>→削除
# ３．### , ## , # ,→削除
# ４．h3>→h4>, h2>→h3>

import pyperclip
import re
from ctypes import *

def wp_0011(seq_before, seq_after, text):
    conv = re.compile(seq_before)
    num = len(conv.findall(text))
    result = seq_before + ': ' + str(num)
    text = conv.sub(seq_after, text)
    return result, text

text = pyperclip.paste()

res_list = []

# １．<span style="font-weight: 400;">→削除
seq_before = r'<span style="font-weight: 400;">'
seq_after = ''
texts = wp_0011(seq_before, seq_after, text)
res_list.append(texts[0])
text = texts[1]

# ２．</span>→削除
seq_before = r'</span>'
seq_after = ''
texts = wp_0011(seq_before, seq_after, text)
res_list.append(texts[0])
text = texts[1]

# ３．### , ## , # ,→削除
seq_before = r'#{1,3}\s'
seq_after = ''
texts = wp_0011(seq_before, seq_after, text)
res_list.append(texts[0])
text = texts[1]

# ４．h3>→h4>, h2>→h3>
seq_before = r'h3>'
seq_after = r'h4>'
texts = wp_0011(seq_before, seq_after, text)
res_list.append(texts[0])
text = texts[1]

seq_before = r'h2>'
seq_after = r'h3>'
texts = wp_0011(seq_before, seq_after, text)
res_list.append(texts[0])
text = texts[1]

pyperclip.copy(text)

results = '\n'.join(res_list)

# 結果確認用にWindowsのメッセージボックスを表示
user32 = windll.user32

user32.MessageBoxW(
    0, 
    results, 
    "Results", 
    0x00000040)
