$(document).ready(function() {
    const hamburguer = $(".hamburguer");
    const nav = $("nav");

    hamburguer.on("click", function() {
        nav.slideToggle();
    });
});