$(document).ready(function() {
    // Variáveis
    const hamburguer = $(".hamburguer");
    const nav = $("nav");
    const aside = $("aside");
    const btnForm = $("#btn-form");
    const form = $("form");
    const sim = $(".rads");
    const nao = $(".radn");
    const mensagem = $("#mensagem");
    const endereco = $("#ender");
    const telefone = $('#telefone');

    let modal = new bootstrap.Modal($('#modal-site'));

    // Eventos
    hamburguer.on("click", function() {
        nav.slideToggle();
    });

    aside.on("click", function() {
        modal.show();
    });

    btnForm.on("click", function() {
        form.fadeIn();
        modal.hide();
    });

    sim.on("click", function() {
        endereco.slideDown();
        endereco.css("display", "flex");
        endereco.css("flex-direction", "column");
        mensagem.slideUp();
    });

    nao.on("click", function() {
        mensagem.slideDown();
        endereco.slideUp();
    });

    // Plugins
    telefone.mask('(00) 00000-0000');

    form.validate({
        rules: {
            nome: {
                required: true
            },
            email: {
                required: true,
                email: true
            },
            telefone: {
                required: true,
                minlength: 15
            },
            localizacao: {
                required: true
            }
        },
        messages: {
            nome: {
                required: "Por favor, insira o nome do restaurante",
            },
            email: {
                required: "Por favor, insira um email para contato",
                email: "Por favor, insira um email válido"
            },
            telefone: {
                required: "Por favor, insira um número de telefone para contato",
                minlength: "Um número de celular tem 11 números"
            },
            localizacao: {
                required: "Por favor, insira o endereço do restaurante"
            }
        }
    });
});