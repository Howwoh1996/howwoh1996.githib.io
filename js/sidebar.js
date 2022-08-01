$(".sidebar").append("<ul></ul>")
        for(let i=0;i<page_data.length;i++){
            $(".sidebar ul").append("<li> <a href='"+page_data[i].pageURL+"'> "+page_data[i].pageID+":"+page_data[i].title+"</a></li>")
        }