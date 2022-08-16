var descricao = document.getElementById('input_descricao')
var valor = document.getElementById('input_valor')
var total = document.getElementById('valor_total')
var tabela_itens_orcamento = document.getElementById('tabela_itens_orcamento')
var lista = []
var soma = 0


function adicionar() {

    if (valor.value == '' || descricao.value == '') {
        alert('Inforome o produto e o valor!')
        
    }
    else {
        var item = {//configura o item (json)
            'descricao': descricao.value,
            'valor': parseFloat(valor.value)
        }
        
        lista.push(item)//adiciona o item na lista

        //cria os elementos da tabela
        tr = document.createElement('tr')
        td = document.createElement('td')
        td.innerHTML = descricao.value
        tr.appendChild(td)//adiciona o dado na row
        tabela_itens_orcamento.appendChild(tr)//adiciona a row no corpo da tabela
        td = document.createElement('td')
        td.innerHTML = `R$ ${(parseFloat(valor.value)).toFixed(2)}`
        tr.appendChild(td)
        tabela_itens_orcamento.appendChild(tr)

        soma += parseFloat(valor.value)//controla o somatório total


        
        
        total.value = soma.toFixed(2)
        descricao.value = ''
        valor.value = ''
    }
}