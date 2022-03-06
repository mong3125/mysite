function popupShow(){
    document.querySelector('.background').className = "background show";
}
function popupClose(){
    document.querySelector('.background').className = "background";
}

window.onload = function(){
    document.querySelector('#showPopup').addEventListener("click", popupShow);
    document.querySelector('#closePopup').addEventListener("click", popupClose);
}