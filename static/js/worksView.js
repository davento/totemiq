// $(function(){
//     var folder = "static/assets";
//     var divclass = "works_child";

//     $.ajax({
//         url : folder,
//         success: function (data) {
//             $(data).find("a").attr("href", function (i, val) {
//                 if( val.match(/\.(png)$/) ) {
//                     $("slideshow_container").append( "<div class='"+ divclass +"' id='"+ i +"'><img src='"+ folder + val +"'></div>" );
//                 }
//             });
//         }
//     });
// }
// )