# 台羅拼音、方音符號轉換器 Tailo-TPS-Converter
這是轉換台羅拼音和方音符號的插件

## 現有功能
1. 單向轉換簡易台羅到方音符號。

## 如何使用
1. 儲存含簡化台羅拼音（號碼標音、無破折）的文檔，例input.txt。
* 注意：**台羅的字行不可包括漢字**

2. 確保您的電腦已安裝python；在此插件的主文件夾，運行`python run.py input.txt`。

3. 如運行成功，開啟`stailo_hongim/out`查看轉換結果。
* main.txt: 主結果，包括漢字和方音符號
* hongim.txt: 方音符號
* tailo.txt: 簡化台羅拼音
* hanji.txt: 漢字

輸入文檔 input.txt
------
```
床前明月光，疑是地上霜
tshong5 tshian5 beng5 guat8 kong1,
gi5 si7 te7 siong7 song1

舉頭望明月，低頭思故鄉
ku2 thiu5 bang3 beng5 guat8,
te1 thiu5 su1 ko2 hiong1
```

轉換結果樣本 main.txt
------
```
床前明月光，疑是地上霜
ㄘㆲˊㄑㄧㄢˊㆠㆤㄥˊㆣㄨㄚㆵ̇ㄍㆲ ,
ㆣㄧˊㄒㄧ˫ㄉㆤ˫ㄒㄧㆲ˫ㄙㆲ 

舉頭望明月，低頭思故鄉
ㄍㄨˋㄊㄧㄨˊㆠㄤ˪ㆠㆤㄥˊㆣㄨㄚㆵ̇,
ㄉㆤ ㄊㄧㄨˊㄙㄨ ㄍㄛˋㄏㄧㆲ 
```
