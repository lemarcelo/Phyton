//função para quando clicam o botão
function cliqueBotao(){
    var elementoTexto = document.getElementById("texto");

    if((elementoTexto.style.color == '') || (elementoTexto.style.color == 'rgb(0, 0, 0)')){
        //quando esta preto clica e vira verde
        elementoTexto.style.color = '#00aa00';
    }else{
        //quando esta verde clica e vira preto
        elementoTexto.style.color = '#000000';
    }
}

//caminho que vai do body, entra no ul e depois puxa o  primeiro li:

/*console.log(document.body.childNodes[6].childNodes[1].textContent);

//Outro meio vai do body, entra no ul e depois puxa o  primeiro li:

var elementoTexto = document.getElementById("texto");

console.log(elementoTexto);

elementoTexto.style.color = '#00aa00';*/