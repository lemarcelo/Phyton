function tornarDark(){
    $("body").css({"color":"#ffffff",
     "background-color": "#333333"});
     $("h1").toggle(2000)
    .css({"color":"#000085"});
}
function tornarLight(){
    $("body").css({"color":"#000000",
     "background-color": "#ffffff",});
    $("h1").toggle(2000)
    .css({"color":"#ff0000"});
}

function tornarFade(){
    $("h2").last().addClass("gremista").fadeOut(3000).removeClass("gremista").addClass("colorado").fadeIn(3000);
}

function copiarTexto(){
    var nome = $("#nome_digitado").val();
    var texto = $("#texto_digitado").val();
    $("#div_destino").append("<br>" +nome+ " digitou: "+texto).css({"color":"#D9BFA9", "background-color": "#333333"});
    $("h3").css({"color":"#B0C1D9"})
    $("#texto_digitado").val('').select();
}

function revelarDataAtributos(){
    var autor = $('#paragrafo-data').data("autor");
    var ano = $('#paragrafo-data').data("ano");

    alert(`Autor: ${autor} - Ano: ${ano}`)
}

function percorrerCaixaSelecao(){
    var caixaSelecao = $(".cb-aluno:checked");

    $.each(caixaSelecao, function(indice, valor){
        var cb = $(valor)
        console.log(cb.data('telefone'))
    })
}

$('#btn-verificar').on('click', percorrerCaixaSelecao)//o segundo parametro é apenas o nome, não é necessário executar, então não vai o ()