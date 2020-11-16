function myFunction() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }

    // if ('serviceWorker' in navigator) { 
    //     // add addToHomeScreen CSS 
    //     cssLink = document.createElement("link");
    //     cssLink.id = "addToHomeScreen";
    //     cssLink.rel = "stylesheet";
    //     cssLink.type = "text/css";
    //     cssLink.href = "css/libs/addtohomescreen.css";
    //     document.head.appendChild(cssLink);
    // } 
}

    // Close the dropdown menu if the user clicks outside of it
    window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
        }
    }
    }