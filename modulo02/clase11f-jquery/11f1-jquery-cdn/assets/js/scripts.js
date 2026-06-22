$(document).ready(function () {
  $("p").dblclick(function () {
    $(this).hide("slow");
  });

  $("p").click(function () {
    $(this).css({
      "color": "red",
      "font-size": "2em"
    });
    console.log("click");
  });

  $("p").hover(function (){
    $(this).html("<a href='#'>Me convertí</a>");
  });

  $('.valor').click(function(){
    $(this).text("$100.000")
  })

  $('.vacaciones').click(function() {
    $(this).css({
      "background-color": "yellow"
    });
  });
});