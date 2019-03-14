arrangeGuide = function(){
  //var titles = document.querySelectorAll(".title-transition, .subtitle-transition");
  var titles = document.getElementsByClassName("title-transition");
  var guide = document.getElementById("pageGuide");
  for(let i = 0; i < titles.length; ++i){
      var li = document.createElement("li");
      var a = document.createElement("a");
      console.log(titles[i].id);
      a.href = "#" + titles[i].id;
      a.innerHTML = titles[i].getElementsByTagName("h3")[0].innerText;
       li.appendChild(a);
       guide.appendChild(li);
  }
}


loadContact = function(obj){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
          obj.innerHTML = xmlHttp.responseText;
  }
  xmlHttp.open("GET", "/contato", true); // true for asynchronous
  xmlHttp.send(null);
}

initContact = function(){
  var contObjs = document.getElementsByClassName("loadContact");
  for(let i = 0 ; i < contObjs.length; ++i)loadContact(contObjs[i]);
}

initContact();
arrangeGuide();
