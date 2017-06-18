function toggleOverlay(objEm) {
    var overlay = document.getElementById("overlay");
    var specialBox = document.getElementById("specialBox");
    var specialSpan = document.getElementById("specialSpan");
    var specialImg = document.getElementById("specialImg");

    if(overlay.style.display == "block") {
        overlay.style.display = "none";
        specialBox.style.display = "none";
    } else {    
        overlay.style.display = "block";
        specialBox.style.display = "block";
        specialSpan.innerHTML = objEm.src;
        specialImg.src = objEm.src;
    }
}