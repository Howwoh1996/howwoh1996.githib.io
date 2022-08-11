# react
## 重要規則
- 引入檔案有先後順序 (一定要先本體 在渲染)
  - 1.react 本體
  - 2.react 渲染
  - 3.bebal 轉譯
  
- jsx 介紹
js 擴充語法 可以用類似XML的方式存取
自定義虛擬DOM 不能 加引號(因為不是當字串使用)
實際寫起來 就像一般的HTML語法  
要轉成 JS的內容(只能是表達式) 加入大括弧{}
數值組的寫法 會有雙重大括弧 一層表示 是數值組(key:value) 一層表示是用JS語法
寫JSX 語法時 script的type屬性要是 type="text/babel"
才會以JSX來讀
虛擬DOM只能有一個根標籤

- react 渲染
ReactDOM.render(虛擬DOM,要丟入的容器)
虛擬DOM 是在JSX用 const 宣告的
要丟入的容器 取得方法:document.getElementById('myId')


