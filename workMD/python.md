# 環境
VSCODE當中的PYTHON延伸模組
# 介紹
## 變數與型別
- 不同於JAVA等等嚴格的語言，在python當中使用變數，是不需要宣告的。
- 當指定變數是甚麼的時候，會同時決定它的型態 可以使用type(變數名稱)來查看變數的型別。
- 使用除法時，會強制轉成 float (不管除出來是不是整數)
- string 的連接可以用符號"+" , 但是string 不能跟其他數字型別用符號"+"  
## 集合型態
- List、Tuple、Set、Dictionary、(Array)
- List 
  - 注意 切片 前包後不包
  - 使用=符號 會變成兩個變數控制同一個 小心使用
## 運算子
- 算術運算子
  - '+-*/'、次方"**"、取floor"%%"、取餘數"%"
- 比較運算子
  - '=='、'<'、'>'、'!='、'<='、'>='
- 邏輯運算子
  - and、or、not (在其他程式語言是&&、||、!)
- 設定運算子
  - '='、'+='.....
## 邏輯、迴圈
- if 、 if...else 、 if elseif...
- while 、 for
- break (強制離開迴圈)
- continue (強制直達迴圈的底部 中間過程不執行)
## 函數 
- python 函數定義 使用 def 
```python
def my_function(parameter):
    do_something() 
    return something
```
- 注意縮排、可傳入參數(call by referrence)、注意變數的範圍(若要使用外部變數 需要傳入)
##  異常處理 
- try... except 異常物件... (else...finally...)
- raise (也可以自己主動拋出異常) 
## class & Object (類別&物件)
- 宣告類別 使用 Class MyClass
- 產生物件 myOb = MyClass()
- 建構子 def \_\_init\_\_()
- 繼承 Class MyClass(要繼承的Class名稱) 

## Numpy、Pandas 套件
- import numpy as np 
- np.array([1,2,3])
-  
```python

```