window.onload = function () {
    var url = window.location.href;
    let navbar = document
        .getElementById("main_nav")
        .querySelectorAll('a');

    navbar.forEach((item, index) => {

        if (url == (item.href)) {
            console.log({ index, item });
            let p = item.parentNode;
            p.classList.add("current_menu");
            console.log(p);
        }
    });
}