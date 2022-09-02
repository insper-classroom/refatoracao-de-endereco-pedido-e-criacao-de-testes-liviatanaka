import pytest
from classes.Endereco import Endereco
import requests

@pytest.mark.endereco
def test_novo_endereco_com_cep_numero():
    novo_endereco1 = Endereco('04509002', 586)
    assert novo_endereco1.rua == 'Rua Jacques Félix' 

@pytest.mark.endereco
def test_novo_endereco_com_tudo():
    novo_endereco2 = Endereco('12345678', 123, 'rua lucca', 'estado lucca', 'cidade lucca', 130)
    assert novo_endereco2.rua == 'rua lucca' and novo_endereco2.cep == '12345678' and novo_endereco2.estado == 'estado lucca'

@pytest.mark.endereco
def test_cep_como_int():
    cep = 20020030
    end_json = Endereco.consultar_cep(cep)
    assert end_json['localidade'] == 'Rio de Janeiro'

@pytest.mark.endereco
def test_cep_como_string():
    cep = '20020030'
    end_json = Endereco.consultar_cep(cep)
    assert end_json['localidade'] == 'Rio de Janeiro'

@pytest.mark.endereco
def test_cep_formato_numerico_incorreto():
    cep = '000000000'
    assert False == Endereco.consultar_cep(cep)

@pytest.mark.endereco
def test_cep_inexistente():
    cep = '00000000'
    assert False == Endereco.consultar_cep(cep)

@pytest.mark.endereco
def test_falha_na_conexao():
    with pytest.raises(requests.exceptions.ConnectionError) as excinfo:
        cep = '04509002'
        Endereco.consultar_cep(cep)
    assert "Max retries exceeded with url" in str(excinfo.value)

# https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions
@pytest.mark.endereco
def test_cria_endereco_sem_numero():
    with pytest.raises(TypeError) as excinfo:
        cep = '20020030'
        Endereco(cep)
    assert "Endereco.__init__() missing 1 required positional argument: 'numero'" in str(excinfo.value)

