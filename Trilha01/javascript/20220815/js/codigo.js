var a = '12345'
var b = 100
var c = 5.999
var d = 123.99546

console.log(a)
console.log(b)
console.log(c)

var resultado = (parseInt(a) + b + c)

console.log(resultado)

console.log(Math.round(resultado))

console.log(d)

console.log(d.toFixed(2))

console.log(`A variável a vale: ` + a)

var texto = `
Variável a vale ${a}, 
variável b vale ${b}, 
variável c vale ${c}, 
variável d vale ${d},
variável resultado vale ${resultado}`

console.log(texto)

var x = 123
var y = 321

console.log(x + y)

console.log(x.toString() + y.toString())

var registro = {//json
    'nome': 'bernardo',
    'idade': 28
}

console.log(registro)
console.log(registro['nome'])
console.log(registro['idade'])

console.log('------JOGO------')

var equipe = []

var jogador1 = {
    'nome':'matheus',
    'idade':20
}

equipe.push(jogador1)

var jogador2 = {
    'nome':'julia',
    'idade':16
}

equipe.push(jogador2)

var jogador3 = {
    'nome':'pablo',
    'idade':29
}

equipe.push(jogador3)


console.log(equipe)

var julia = equipe[1]

console.log(julia)


console.log(`${julia['nome'].toUpperCase()} tem ${julia['idade']} anos`)
console.log(`A equipe é composta por ${equipe.length} jogadores`)