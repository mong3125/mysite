function clickBtn(){
    alert('눌렀다!');
    window.location.href = "{% url 'board:index' %}";
}

window.onload = function(){
    const deleteBtn = document.querySelector('.post_delete');
    deleteBtn.addEventListener('click', clickBtn);
}