$(document).on('scroll', function () {
    console.log('scrolled')

    var $nav = $(".navbar-custom");
    $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
});


var navDiv = document.getElementById("navdiv");
navDiv.addEventListener("mouseover", showMenu, false);

var menuDiv = document.getElementById("menu-content")
menuDiv.addEventListener("mouseout", hideMenu, false);

var menuIcon = document.getElementById("nav-left-item")

function showMenu() {
    menuDiv.style.display = "block"
    navDiv.style.backgroundColor = "black"
    menuIcon.innerHTML.style.display = "none" 
    menuIcon.innerHTML = menuIcon.innerHTML + "<i class='fa-solid fa-xmark'></i>"
}


function hideMenu()
{  
    menuDiv.style.display = "none"
    navDiv.style.backgroundColor = null 
    var $ic = $(".fa-xmark") 
    menuIcon.removeChild($ic)
    menuIcon.innerHTML = "<img class='menu-icon mb-3' src='{{url_for('static', filename='img/menu_bars.png')}}' alt=''>"  

}

