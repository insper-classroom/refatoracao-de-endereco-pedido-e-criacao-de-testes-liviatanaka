import pytest
from classes.Produto import Produto
produto = Produto(1, 'bolo', 5)

@pytest.mark.produto
def test_novo_produto_com_preco():
    p2 = Produto(2, 'louça', 2)
    assert p2.nome == 'louça' and p2.preco == 2

@pytest.mark.produto
def test_novo_produto_sem_preco():
    p3 = Produto(3, 'parmesão')
    assert p3.nome == 'parmesão' and p3.preco == ''

@pytest.mark.produto
def test_get_id():
    assert 1 == produto.get_id()

@pytest.mark.produto
def test_dicionario_produto():
    assert {'Id': 1, 'Nome': 'bolo'} == produto.to_dict()

@pytest.mark.produto
def test_busca_nome_existente():
    p4 = Produto(4, 'macarrão', 4)
    assert [p4] == Produto.busca_nome('mac')

@pytest.mark.produto
def test_busca_nome_nao_existente():
    assert [] == Produto.busca_nome('beliche')