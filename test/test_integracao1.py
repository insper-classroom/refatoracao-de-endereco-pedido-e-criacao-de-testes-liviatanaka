import pytest
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
from classes.Produto import Produto
from classes.Pedido import Pedido
import copy

pessoa_i = PessoaFisica('789.456.123-0', 'integracao1@gamil.com', 'isabelle')
end_i1 = Endereco('20020050', 123)
end_i2 = Endereco('20020050', 456)
carrinho_i = Carrinho()
pedido_i = Pedido(pessoa_i, carrinho_i)
produto_i = Produto(5, 'Queijo', 5)

# main 2

@pytest.mark.integracao
@pytest.mark.endereco
@pytest.mark.pedido
def test_adiciona_endereco_entrega_pedido():
    pedido_i.endereco_entrega = end_i1
    assert pedido_i.endereco_entrega == end_i1

@pytest.mark.integracao
@pytest.mark.endereco
@pytest.mark.pedido
def test_adiciona_endereco_faturamento_pedido():
    pedido_i.endereco_faturamento = end_i2
    assert pedido_i.endereco_faturamento == end_i2


@pytest.mark.integracao
@pytest.mark.pedido
def test_infos_carrinho_completo():
    assert pedido_i.pessoa == pessoa_i
    assert pedido_i.carrinho == carrinho_i
    assert pedido_i.endereco_entrega == end_i1
    assert pedido_i.endereco_faturamento == end_i2
    assert pedido_i.status == Pedido.EM_ABERTO

@pytest.mark.integracao
@pytest.mark.produto
@pytest.mark.carrinho
def test_adiciona_item_produto_buscado():
    produtos = Produto.busca_nome('quei')
    if len(produtos)>0:
        prod = produtos[0]
    
    qtd, id = carrinho_i.adicionar_item(prod, 5)
    assert id == prod.get_id() and qtd == 5

