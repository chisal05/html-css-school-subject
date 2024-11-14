document.querySelector('.menu-icon').addEventListener('click', function() {
    const menu = document.querySelector('.side-menu');
    if (menu.style.left === '0px') {
        menu.style.left = '-300px';
    } else {
        menu.style.left = '0px';
    }
});
