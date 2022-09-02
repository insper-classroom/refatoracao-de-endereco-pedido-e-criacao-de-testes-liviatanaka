from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
from classes.Pedido import Pedido

import pytest

pessoa = PessoaFisica('123.456.789-0', 'pedido@gmail.com', 'pedidopessoa')
carrinho = Carrinho()

@pytest.mark.integracao
@pytest.mark.pessoa
@pytest.mark.carrinho
@pytest.mark.pedido
def test_novo_pedido():
    novo_pedido = Pedido(pessoa, carrinho)
    assert pessoa == novo_pedido.pessoa and novo_pedido.status == Pedido.EM_ABERTO