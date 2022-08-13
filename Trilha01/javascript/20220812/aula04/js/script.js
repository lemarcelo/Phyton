var valor1 = document.getElementById('valor1')
var valor2 = document.getElementById('valor2')
var resultado = document.getElementById('resultado')

function somar(){
    resultado.value = Number(valor1.value)+Number(valor2.value)
    resultado.hidden=false
}
function subtrair(){
    resultado.value = Number(valor1.value)-Number(valor2.value)
    resultado.hidden=false
}
function multiplicar(){
    resultado.value = Number(valor1.value)*Number(valor2.value)
    resultado.hidden=false
}
function dividir(){
    resultado.value = Number(valor1.value)/Number(valor2.value)
    resultado.hidden=false
}
function limpar(){
    resultado.value = ''
    valor1.value = ''
    valor2.value = ''
    resultado.hidden=true
}