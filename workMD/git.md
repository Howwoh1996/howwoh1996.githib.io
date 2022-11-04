# Git 學習筆記
網址:https://learngitbranching.js.org/
網站優點: 以圖形化的介面讓使用者知道現在在git中發生了甚麼事情、進行到哪一步，對初學者可以很好的理解Git的操作與使用

## git 概念總覽
git 是版本控制 
他的流程概念 可以用 數學中的 有向圖(directed graph或digraph)呈現
其中的節點 是每一次的紀錄(通常是透過commit產生) 
有向邊 directed edge 可以表示紀錄的順序性(箭頭指向上一次的紀錄)

分支(branch)的概念 
分支會在節點上 並隨著commit等等的指令移動於節點之間 
分支在實際上 常代表一個項目或功能的完成進度  
當功能完成時 再將那些更動內容 融合到主要支線(main)上 
可以確保在融合之前 主線的運作都是正常的 

標籤(tag)的概念
標籤會在節點上 但基本上不會移動位置
通常是標示一些重要的版本 可以藉此更方便的看出經歷了幾個版本的改變 

## 指令學習
- git commit  
更新HEAD所在的節點  並且若HEAD在分支上 也會使分支更新到那個節點上 

- HEAD 概念 
HEAD 就是當前編輯的節點/分支 
每一個節點 都是一個紀錄點 在操作上 是可以在任何一個節點 執行commit 動作
但不建議這樣做 commit只建議做在分支(branch)上  管理起來才好 (否則會detached HEAD (斷頭))
所以一般來說 不要在普通的節點上 設定head(當前編輯節點/分支)並且commit  
commit都在分支上(branch)做設定 會比較適合 (真要在節點加入commit 先創一個分支 再commit)

- git branch my_branch_name
  - 在HEAD創建一個分支
  - git branch  my_branch_name another_point (OVERLOAD 兩個參數時)
    -  在 another_point 創建一個分支
    -  another_point 可以是一個節點或分支 
  - git branch -f my_branch_name1 my_branch_name2(帶參數 -f 需要兩個參數)
    - 將my_branch_name1分支 強制指定在 my_branch_name2(可以是分支或節點) 上面  

- git checkout my_branch_name (git switch)
  - 切換到該分支 (該分支或節點變成HEAD ) (在該網站的展示中 當前分支的名稱後面會有*)
  - git checkout -b my_branch_name (帶參數 -b)
    - 創建一個分支 並設定其為HEAD
    - 等價於 git branch my_branch_name > git checkout my_branch_name    
  
- git merge my_branch_name 
    - 將當前分支和指定的分支融合加入當前分支 
    - (類似commit 在當前分支上 當前分支前進 指定的分支只有提供資料 沒有變動)
    - (融合別人 還是自己)(抓別人來融合)

- git rebase my_base_branch_name 
  - 將當前分支(head) 加入指定分支的底下 類似 merge 但是放的方式不同 會把原始的路線砍掉 接在指定路線上 (把自己接到別人身上)
  - rebase 英文上的意義是 從新建立一個基礎 當只有接受一個參數(分支) 就是指 將這個分支當作我現在這個HEAD的基礎 去建構
  - 接收兩個參數時 意思是指將我第一個接收到的參數(分支)當基礎 去重構第二個接收到的參數 
  - git rebase  my_base_branch_name my_target_branch_name (OVERLOAD 兩個參數時)
        - 以第一個branch為基準 將第二個分支接到第一個分支上(只會裝備沒有的節點) 
        - 意義上等於 git checkout my_target_branch_name2 > git rebase my_base_branch_name

- ^ 符號
    - 加在分支或節點或HEAD後面 表達其父節點  EX:HEAD^
- ~ 符號
  - 加在分支或節點或HEAD後面 表達其父節點的第幾個
  - 用法: HEAD~3 Head的父節點的父節點的父節點  (\^的多重版本)(HEAD^^^) 


- git revert a_point
類似commit 但是會revert 所指定的節點(或指定分支所在的節點) (產生 a_point')
- git reset a_point
移動當前的分支 到指定的位子
等價 git branch -f HEAD HEAD^
- git cherry-pick 
挑選想要的節點 放入當前的分支當中 (不能將上游的節點放入)
EX: git cherry-pick c3 c4 c7 
- git rebase -i HEAD~N 
重新排列 從前N個 N是一個整數
會有圖形化介面讓你選擇要用那些與順序

- git tag a_point /  describe a_point
  - tag 標籤 顧名思義 是指紀錄一個錨點 不會隨著commit或任何方式移動 
  - 用checkout 移動到標籤的時候 會出現HEAD分離的情況 (標籤本身不能是HEAD 所在的節點會是HEAD)
  - describe 用來描述離這個分支所在最近的錨點(標籤) 長相會是 v0_2_gc2
  - 意思是:標籤_距離_g點的名字

- git fakeTeamwork 
  - 在該網站上模擬 別人的GIT上面執行的事情 等同別人的 git commit
  - 可以後面放參數 git fakeTeamwork a_branch 意思是在a_branch分支上面進行一次commit
- git push
  - 將HEAD所在的分支狀態更新到遠端的git
  - 可以後面帶參數 如果是git push origin b1:b2 意思是把b1這個本機的分支推送到遠端的GIT的b2這個分支上(若無b2，會自動建立)
- git pull 
  - 將遠端的 Git 版本拉到本地所在的 Git 並融合(git fetch > git merge)
  - 可以後面帶參數 如果是 git pull origin b1:b2 意思是把b1這個遠端的分支拉到本地的GIT的b2這個分支上並融合(若無b2，會自動建立)
- git fetch 
  - 將遠端的 Git 版本拉到本地所在的 Git
  - 可以後面帶參數 如果是 git fetch origin b1:b2 意思是把b1這個遠端的分支拉到本地的GIT的b2這個分支上(若無b2，會自動建立)
- git checkout -b a_branch o/main 使a_branch這個分支追蹤o/main
  - 也等價於 git branch -u o/main a_branch
- detached HEAD (斷頭)
    當HEAD沒有綁定在分支上，稱為detached HEAD，盡量不要發生，如果出現這樣的情況，可以用git checkout a_branch 來把HEAD移動到分支上