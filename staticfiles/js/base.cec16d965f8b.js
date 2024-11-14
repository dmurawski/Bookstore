const navEl = document.querySelector('.c-navbar')
window.addEventListener('scroll',()=>{
    if (window.scrollY >= 50){
        navEl.classList.add('navbar-scrolled')
    }else if (window.scrollY < 50){
        navEl.classList.remove('navbar-scrolled')
    }
})


document.addEventListener("DOMContentLoaded", function () {
    const scrollToTopButton = document.getElementById("scrollToTop");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 200) {
            scrollToTopButton.classList.add("show");
        } else {
            scrollToTopButton.classList.remove("show");
        }
    });

    scrollToTopButton.addEventListener("click", function (e) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
});