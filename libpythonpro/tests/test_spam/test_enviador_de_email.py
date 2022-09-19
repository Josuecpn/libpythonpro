import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com', 'josuecpn93@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'maraolik23@hotmail.com',
        'Cursos Python Pro',
        'Primeira turma Guido Van Rossum aberta.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'josuecpn']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'maraolik23@hotmail.com',
            'Cursos Python Pro',
            'Primeira turma Guido Van Rossum aberta.'
        )
