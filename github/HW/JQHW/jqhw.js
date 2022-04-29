var menuarray = new Array;
menuarray = ["jqhw_menu","jqhw01","jqhw02","jqhw03","jqhw04"]

function auto_append_h1() {
    $("h1").append(`AIOT.17-JQuery-黃柏浩`);
}

function auto_append_menu(){
    for(i=0;i<menuarray.length;i++){
        $(".menu").append(`<li id="menu${i}"><a href="${menuarray[i]}.html">${menuarray[i]}</a></li>`)
    }
    
}
auto_append_menu();
auto_append_h1();
$("h1").hover(function(){
    $(".readme").css("opacity","0.8").css("z-index","3").css("display","block")
},function(){
    $(".readme").css("opacity","0").css("z-index","-2").css("display","none")
});

