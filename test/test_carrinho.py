import pytest
from classes.Carrinho import Carrinho
from classes.Produto import Produto

produto1 = Produto("001", "Mesa")
produto2 = Produto('002', 'Outra mesa')
carrinho1 = Carrinho()


@pytest.mark.integracao
@pytest.mark.produto
@pytest.mark.carrinho
def test_novo_item_quantidade_int():
    qtd, id = carrinho1.adicionar_item(produto1, 5)
    assert id == produto1.get_id() and qtd == 5

@pytest.mark.integracao
@pytest.mark.produto
@pytest.mark.carrinho
def test_novo_item_quantidade_str():
    qtd, id = carrinho1.adicionar_item(produto2, '1')
    assert id == produto2.get_id() and qtd == 1

@pytest.mark.integracao
@pytest.mark.produto
@pytest.mark.carrinho
def test_item_ja_existente():
    qtd, id = carrinho1.adicionar_item(produto1, 1)
    assert id == produto1.get_id() and qtd == 6

@pytest.mark.carrinho
def test_retorna_itens():
    dicio = {'001': 6, '002':1}
    assert dicio == carrinho1.get_itens()

