import pytest
from classes.PessoaFisica import PessoaFisica
from classes.Endereco import Endereco

endereco = Endereco('08320330', 430)
pessoa = PessoaFisica('524.222.452-6', 'tiago@email.com','Tiago')

@pytest.mark.pessoa
def test_nova_pessoa_com_nome():
    pessoa_nova = PessoaFisica('123.456.789-0', 'nova@gmail.com', 'Novaldina')
    assert 'Novaldina' == pessoa_nova.nome and 'nova@gmail.com' == pessoa_nova.email and '123.456.789-0' == pessoa_nova.cpf

@pytest.mark.pessoa
def test_nova_pessoa_sem_nome():
    pessoa_sem_nome = PessoaFisica('456.789.123-0', 'semnome@gmail.com')
    assert 'Visitante' == pessoa_sem_nome.nome and 'semnome@gmail.com' == pessoa_sem_nome.email and '456.789.123-0' == pessoa_sem_nome.cpf

@pytest.mark.integracao
@pytest.mark.pessoa
@pytest.mark.endereco
def test_novo_endereco():
    apelido = 'casa'
    assert endereco == pessoa.adicionar_endereco(apelido, endereco)

@pytest.mark.integracao
@pytest.mark.pessoa
@pytest.mark.endereco
def test_pegar_endereco():
    apelido = 'casa'
    assert endereco == pessoa.get_endereco(apelido)

@pytest.mark.integracao
@pytest.mark.pessoa
@pytest.mark.endereco
def test_lista_de_enderecos():
    assert [endereco] == pessoa.listar_enderecos()

@pytest.mark.pessoa
def test_busca_pessoa_pelo_nome():
    pessoa_busca = PessoaFisica('456.125.439-1', 'liviatanaka@gmail.com', 'Livia')
    assert [pessoa_busca] == PessoaFisica.busca_nome('li')

@pytest.mark.pessoa
def test_busca_nome_nao_existente():
    assert [] == PessoaFisica.busca_nome('alexandre')