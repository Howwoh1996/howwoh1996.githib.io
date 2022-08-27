# react
## 重要規則
- 引入檔案有先後順序 (一定要先本體 在渲染)
  - 1.react 本體
  - 2.react 渲染
  - 3.bebal 轉譯
  
## jsx 介紹
- js 擴充語法 可以用類似XML的方式存取 但需要透過babel轉譯
- 自定義虛擬DOM 不能 加引號(因為不是當字串使用)
- 實際寫起來 就像一般的HTML語法  
- 要轉成 JS的內容(只能是表達式) 加入大括弧{}
- 數值組的寫法 會有雙重大括弧 一層表示 是數值組(key:value) 一層表示是用JS語法
- 寫JSX 語法時 script的type屬性要是 type="text/babel" 才會以JSX來讀
- 虛擬DOM只能有一個根標籤

## react 渲染
- ReactDOM.render(虛擬DOM,要丟入的容器)
- 虛擬DOM 是在JSX用 const 宣告的
- 要丟入的容器 取得方法:document.getElementById('myId')
## bebal
- 轉譯 JSX 到 JS 

## 好處
- 是SPA(single page app)，在切換頁面時，透過將組件渲染到頁面上，
來達到不刷新頁面更新內容，因為透過虛擬DOM，擁有更快的速度，(尤其是當頁面的節點很多的情況)

## class 類式組件
- 首字母必須大寫 標籤必須閉合(在JSX)
- 裡面的方法，使用附值語句，配合箭頭函數(這樣的this指向，可以指到物件本身)
- constructor 絕大部分的情況 可以不寫
- 用在綁定事件時加入括號()，方法要回傳一個函數

## 內建函數 生命週期
- 主要有 render、ComponentDidMount、ComponentWillUnmount
- 裡面的this 會自己指向物件本身，不需要另外寫附值語句的形式。(因為是ReactDOM幫忙調用 不是自己調用)
  
## 三大核心屬性
- state
  - class 中自帶的屬性 
  - 更新狀態動頁面渲染
  - 要用 setState 去更新()中帶的 key:value，且是合併不是取代
  - 調用setState 會經過閥門才到render 
- props
  - props 通常是指標籤組件上帶的參數 
- refs 
  - 綁定事件

## 