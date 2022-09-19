import pytest

from libpython.spam.db import Conexao


# o scope é usado para definir quantas vezes irá ser usado por situação
@pytest.fixture(scope='session')
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear Down
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessa()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()
