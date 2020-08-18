$(document).ready(function(){
    $("body").hide();
});

$(window).on("load", function () {
    $(".flipbook").mousedown(function(){
          $(".arrow").fadeOut("slow");
          $(".arrow").stop();
      });

    var arrow = $(".arrow");

    var right = function () {
        arrow.animate({left: '50px'}, 2000, left);
    };

    var left = function () {
        arrow.animate({left: '0px'}, 2000, right);
    };

    right();

    $("body").show();
 });