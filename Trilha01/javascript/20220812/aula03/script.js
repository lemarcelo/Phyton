var texto_digitado = document.getElementById('texto_digitado')
var texto_copiado = document.getElementById('texto_copiado')
var texto_inserido = document.getElementById('texto_inserido')


function calcular(){
    var input_a = document.getElementById('input_a')
    var input_b = document.getElementById('input_b')
    var resultado = document.getElementById('resultado')

    

     resultado.value=Number(input_a.value) + Number(input_b.value)
}

function copiarTexto(){
    texto_copiado.value = texto_digitado.value

    texto_inserido.innerHTML = texto_copiado.value
    texto_inserido.style.color="red"
}

function limpar(){
    texto_digitado.value=''
    texto_copiado.value=''
    texto_inserido.innerHTML = ''
}