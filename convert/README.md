# テキスト変換
## WP_0011
### 機能
google docsからWordPressへコピーした際のHTMLの整形のため、クリップボードのテキストに以下の変換を行う。
- \<span style="font-weight: 400;">→削除
- \</span>→削除
- \### , ## , # ,→削除
- h3>→h4>, h2>→h3>

実行すると変換した数が表示される。変換内容を確認できる。

※変換内容は任意で変更してください。
### 環境
- Windows10 64bit
- Python3.5
### 使い方
#### 準備
1. WP_0011.py, WP_0011.batを同じフォルダに保存
2. WP_0011.bat内のコードを絶対パスに変更
3. 「環境設定」から保存したフォルダへのPathを設定
#### 使用
1. 変換したいテキストをコピー
2. 「Windows + R」で「ファイル名を指定して実行」を起動し、「WP_0011.bat」と入力、実行
3. 変換後のテキストがクリップボードに保存され、変換結果がメッセージウインドウで表示される
### 参考
- [『退屈なことはPythonにやらせよう――ノンプログラマーにもできる自動化処理プログラミング』O'Reilly Japan](https://www.oreilly.co.jp/books/9784873117782/)
- [Python から Windows API を呼び出す - MessageBox の例 - Python 入門](https://python.keicode.com/advanced/ctypes-messagebox.php)
