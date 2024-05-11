# Scripts

這裡的腳本可以將碼表轉換為TXT/YAML/JSON格式，方便用在其他輸入法軟件。<br />
由於不會在每次更新碼表時都發佈releases，若有需要可以用這裡的腳本自行生成。<br />
僅在Windows下進行了測試。<br />

## 使用方法
* **buildTxt.py**<br />
> 參數
```
-s source    需要轉換的源文件，如[Cangjie5.txt]
-o order     輸出文件的字和倉頡碼的順序[char=字在前, code=倉頡碼在前]
-d delimiter 輸出文件的分隔符[tab=製表鍵, space=一個空格, multi=多個空格, none=無]
-l linebreak 輸出文件的換行符[crlf, cr, lf]
-t template  使用模板生成包含配置項的碼表文件，此參數衹可以與-s共用
             [rime=ibus-rime,weasel=小狼亳, squirrel=鼠鬚管, fcitx=Fcitx 5, yong=小小輸入法]
```
> 示例
1. 轉換`一般排序`碼表，字在前，倉頡碼在後，以`Tab`分隔，以`\r\n`換行（格式與小狼亳相同，但不包含配置項）
```
python buildTxt.py -s Cangjie5.txt -o char -d tab -l crlf
```
效果如下
```
金	c
鈤	ca
錩	caa
𫓣	caaf
𨧹	cab
```
2. 轉換`傳統漢字優先，偏好香港用字習慣`碼表，字在前，倉頡碼在後，以`Tab`分隔，以`\r`換行（格式與鼠鬚管相同，但不包含配置項）
```
python buildTxt.py -s Cangjie5_HK.txt -o char -d tab -l cr
```
效果如下
```
金	c
鈤	ca
錩	caa
𫓣	caaf
𨧹	cab
```
3. 轉換`簡化字優先`碼表，倉頡碼在前，字在後，以`Space`分隔並對齊，以`\r\n`換行（格式與小小輸入法平台及「倉頡平台 2022」相同，但不包含配置項）
```
python buildTxt.py -s Cangjie5_SC.txt -o code -d multi -l crlf
```
效果如下
```
c       金
ca      鈤
caa     錩
caaf    𫓣
cab     𨧹
```
4. 使用模板轉換`一般排序`碼表，生成適用於小狼亳輸入法的`.dict.yaml`文件（使用模板時，生成的文件會**包含配置項**）
```
python buildTxt.py -s Cangjie5.txt -t weasel
```

* **buildYaml.py**<br />
> 無需輸入參數
* **buildJson.py**<br />
> 無需輸入參數
