import pytest
from classes.Produto import Produto
@pytest.mark.produto
def test_get_id():
    produto = Produto(1, 'bolo', 5)
    assert 1 == produto.get_id()

@pytest.mark.produto
def test_dicionario_produto():
    produto = Produto(1, 'bolo', 5)
    assert {'Id': 1, 'Nome': 'bolo'} == produto.to_dict()

@pytest.mark.produto
def test_busca_nome():
    p3 = Produto(3, 'macarrão', 3)
    assert [p3] == Produto.busca_nome('mac')