arrangeGuide = function(){
  //var titles = document.querySelectorAll(".title-transition, .subtitle-transition");
  var titles = document.getElementsByClassName("title-transition");
  var guide = document.getElementById("pageGuide");
  for(let i = 0; i < titles.length; ++i){
      var li = document.createElement("li");
      var a = document.createElement("a");

      var h = $(document).height();
      var w = $(document).width();

      $(a).click(function(){
        $('html, body').animate({
          scrollTop: $("#"+ titles[i].id).offset().top - (h * .05 - (w/(w*.5)))
        }, 1000);
      });

      $(a).hover(function(){
        $(this).css('cursor','pointer');
      });

      //a.href = void(0); 
      a.innerHTML = titles[i].getElementsByTagName("h3")[0].innerText;
       li.appendChild(a);
       guide.appendChild(li);
  }
}


openModalContact = function(source){
  source = window.location.href + " ; " + source
  $("#contact-source").val(source);
  $("#contactModal").modal("show");
}

$(document).ready(function() {
  $('#sidebarCollapse').on('click', function() {
    $('#sidebar').toggleClass('active');
    $(this).toggleClass('active');
  });


  arrangeGuide();
});



