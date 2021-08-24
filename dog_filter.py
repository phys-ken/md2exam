import shutil



def dog_filter(kaitoBango = True , choiceSort = True):

  target_md = "01_input.md"
  sorted_md = "_tmp.md"
  row_cnt = 0
  qcnt = 0
  chs = []
  ch = dict()
  flag = False

  if (kaitoBango  == False and choiceSort == False):
    shutil.copyfile(target_md, sorted_md)
    return


  def stripSharp( s ):
    s = s.replace('##### ', '')
    return s

  def plusSharp( s ):
    s =  "##### "  + str(s) 
    return s

  with open(target_md, 'r',encoding="utf-8_sig") as f:
      lines = f.read()
      for l in lines.split("\n"):
          row_cnt += 1
          
          if "#####" in l:
            if flag == False:
              ch.setdefault(row_cnt , l)
              flag = True
            else:
              ch.setdefault(row_cnt , l)
          else:
            if flag == True:
              chs.append(ch)
              ch = dict()
            flag = False


  # 回答番号を付記
  kaito_box = 0
  if kaitoBango == True:
    #ファイルをリストで読み込み
    with open(target_md ,  'r',encoding="utf-8_sig" )as f:
        kaitoBoxData = f.read().split("\n")

    for c in chs:
      #print(list(c.keys())[0])

      row_cnt = 2
      while not "#" in kaitoBoxData[int(list(c.keys())[0]) - row_cnt]:
        row_cnt += 1  
      else:
        kaitoBoxData[list(c.keys())[0] - row_cnt] += "  解答番号：" + str(kaito_box)
        #print(kaitoBoxData[list(c.keys())[0] - row_cnt])  
            
      kaito_box = kaito_box + 1
    target_md = sorted_md

    #設問の最後に番号追加
    

    #元のファイルに書き込み
    with open(sorted_md, mode='w' ,encoding="utf-8_sig" )as f:
        for l in kaitoBoxData:
          f.write(str(l) + "\n")


  if choiceSort:
    # 選択肢を並び替える
    fix_dict = {}
    for c in chs:
      vals = list(c.values())
      vals = list(map(stripSharp , vals))
      try: ## 数値型に変換して並び替えてみる
        vals = sorted(list(map(float , vals)))
        #print("数値型:" + " - ".join(map(str, vals)))
      except:
        vals = sorted(list(map(str , vals)))
        #print("文字列型:" + " - ".join(map(str, vals)) )
      vals = list(map(plusSharp , vals))
      keys = sorted(list(c.keys()))
      cnt = 0
      for k in keys:
        fix_dict.setdefault(k , vals[cnt] )
        cnt += 1

    #ファイルをリストで読み込み
    with open(target_md ,  'r',encoding="utf-8_sig" )as f:
        sorted_data = f.read().split("\n")

    #とってつける
    for key in fix_dict:
      sorted_data.pop(key - 1)
      sorted_data.insert(key - 1, fix_dict[key])

    #元のファイルに書き込み
    with open(sorted_md, mode='w' ,encoding="utf-8_sig" )as f:
        for l in sorted_data:
          f.write(str(l) + "\n")


    #print(sorted_md + "__の選択肢を並び替えました。")


dog_filter()