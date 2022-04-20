


$(".menu_list li").click(go_to_the_page);
        function go_to_the_page() {
            console.log($(this).text())
            window.location.href = $(this).text()+".html"; //頁面跳轉到該文字所指定的網頁
        }