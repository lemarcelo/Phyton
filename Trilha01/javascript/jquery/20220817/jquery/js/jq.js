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