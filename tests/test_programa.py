from models import Programa
import pytest

class TestePrograma:

  @pytest.fixture
  def programa(self):
    return Programa("Silvio Santos", 2015)

  def test_print_nome(self, programa:Programa):
    esperado = "Silvio Santos"

    resultado = programa.nome # When

    assert resultado == esperado # Then

  def test_print_ano(self, programa:Programa):
    esperado = 2015

    resultado = programa.ano

    assert resultado == esperado

  def test_print_likes(self, programa:Programa):
    esperado = 2

    programa.dar_like(quantidade=2)
    resultado = programa.likes

    assert resultado == esperado

  def test_print_programa(self, programa:Programa):
    esperado = "\nNome: Silvio Santos\nAno: 2015\nLikes: 0"
    resultado = programa.__str__()

    assert resultado == esperado

  def test_novo_nome(self, programa:Programa):
    entrada = "Programa do Ratinho"
    esperado = "Programa do Ratinho"

    programa.nome = entrada
    resultado = programa.nome

    assert resultado == esperado

  @pytest.mark.exceptions
  def test_novo_nome_erro(self, programa:Programa):
    with pytest.raises(Exception):
      entrada = "Silvio Santos"

      programa.nome = entrada