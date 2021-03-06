#!/usr/bin/env python
from __future__ import print_function
from docx2pdf import convert
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import shutil
import dog_filter

# 変更のための様式たち
w2p_flag = True # PDFに変換するかどうか
kaitoBango = True # 回答番号の付記
choiceSort = True # 選択肢のソート


watch_dir_path = "./"
watch_file = "01_input.md"

def echoDog():
    print("mdの変更を検知しました。wordに変換しました。")
    return 0


class MyHandler(PatternMatchingEventHandler):
    def __init__(self,  patterns):
        super(MyHandler, self).__init__(patterns=patterns)

    def _run_command(self):
        dog_filter.dog_filter(kaitoBango , choiceSort)
        subprocess.run(["pandoc" , "-d" , "defaults.yml" ])
        echoDog()
        if w2p_flag:            
            try:
                convert("./", "./")
                print("\n")
                print("wordをpdfに変換しました。。")
            except:
                print("wordをpdfに変換できませんでした。")

    def on_moved(self, event):
        self._run_command()

    def on_created(self, event):
        self._run_command()

    def on_deleted(self, event):
        self._run_command()

    def on_modified(self, event):
        self._run_command()


def watch(path, extension):
    event_handler = MyHandler( ["*"+extension])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()









if __name__ == "__main__":
  print(watch_dir_path + "/" + watch_file + "を監視します。ワンワン。")
  watch(watch_dir_path , watch_file)