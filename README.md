# markdown2定期試験
* markdown で試験問題の雛形を作り、pandocで.docxに変換します。
* watchdogで監視しmdの変更を自動検知してpandocで変換します。

## 環境構築

* Pandocをインストールしてください。
* python環境を構築してください。
* `pip install watchdog`で、watchdogをインストールしてください。
* markdownエディタで`01_input.md`を開いて、編集します。
* 同時に、`pyhon dog.py`を実行します。すると、ファイルの監視が始まります。
* `01_input.md`を保存すると。同時に`02_output.docx`を生成します。

## memo

* reference.docx の編集がかなり難しかった
    * Heading1の書式ではなく、wordのスタイルウィンドウから`見出し1`の`スタイル`を変更する
* 行頭揃えは、ルーラー機能を使うと便利。



