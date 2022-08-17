var descricao = document.getElementById('input_descricao')
var valor = document.getElementById('input_valor')
var total = document.getElementById('valor_total')
var tabela_itens_orcamento = document.getElementById('tabela_itens_orcamento')
var lista = []
//var soma = 0


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
         redesenharTabela()

        //adicionaTr()//extra
        //total.value = soma.toFixed(2)
        //soma += parseFloat(valor.value)//controla o somatório total


        descricao.value = ''
        valor.value = ''
    }
}
//extra
// function adicionaTr() {
//     //cria os elementos da tabela
//     tr = document.createElement('tr')
//     td = document.createElement('td')
//     td.innerHTML = descricao.value
//     tr.appendChild(td)//adiciona o dado na row
//     tabela_itens_orcamento.appendChild(tr)//adiciona a row no corpo da tabela
//     td = document.createElement('td')
//     td.innerHTML = `R$ ${(parseFloat(valor.value)).toFixed(2)}`
//     tr.appendChild(td)
//     tabela_itens_orcamento.appendChild(tr)
// }

function redesenharTabela(){
    var corpo_tabela_itens = ''
    var soma = 0


    for (i=0; i < lista.length; i++){
        var item = lista[i]
        var valor = parseFloat(item['valor'])

        soma += valor

        corpo_tabela_itens += `
        <tr>
            <td>${item['descricao']}</td>
            <td class="text-right">R$ ${valor.toFixed(2)}</td>
        </tr>
        `
    }


    tabela_itens_orcamento.innerHTML = corpo_tabela_itens
    total.value = soma.toFixed(2)

}