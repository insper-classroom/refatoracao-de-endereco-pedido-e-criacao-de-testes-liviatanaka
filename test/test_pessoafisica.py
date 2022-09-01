import pytest
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

endereco = Endereco('08320330', 430)
pessoa = PessoaFisica('Tiago', 'tiago@email.com','524.222.452-6')

@pytest.mark.pessoa
def test_novo_endereco():
    apelido = 'casa'
    assert endereco == pessoa.adicionar_endereco(apelido, endereco)

@pytest.mark.pessoa
def test_pegar_endereco():
    apelido = 'casa'
    assert endereco == pessoa.get_endereco(apelido)

@pytest.mark.pessoa
def test_lista_de_enderecos():
    assert [endereco] == pessoa.listar_enderecos()

@pytest.mark.pessoa
def test_busca_pessoa_pelo_nome():
    pessoa_nova = PessoaFisica('Livia', 'liviatanaka@gmail.com', '456.125.439-1')
    assert [pessoa_nova] == PessoaFisica.busca_nome('livia')