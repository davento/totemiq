// function loadSlideshow(){
//     var folder = "..static/images/works/";
//     var divclass = "works_img fade";

//     $.ajax({
//         url: folder,
//         success: function (data) {
//             $(data).find("a").attr("href", function (i, val) {
//                 if (val.match(/\.(jpe?g|png|gif)$/)) {
//                     $("slideshow_container").append("<img class='work_img fade' img src='" + folder + val + "'>");
//                 }
//             });
//         }
//     });
// }



// function loadSlideshow() {
//     var dir = "static/images/obras/";
//     var fileextension = ".png";
//     $.ajax({
//         //This will retrieve the contents of the folder if the folder is configured as 'browsable'
//         url: dir,
//         success: function (data) {
//             //List all .png file names in the page
//             $(data).find("a:contains(" + fileextension + ")").each(function () {
//                 var filename = this.href.replace(window.location.host, "").replace("http://", "");
//                 $("slideshow_container").append("<img class='works_img fade' src='" + dir + filename + "'>");
//             });
//         }
//     });
// }