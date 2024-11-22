# bibliotecario.py
from model.livro import Livro
from model.emprestimos import Emprestimos

class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome

    # Funções relacionadas a empréstimos
    def visualizar_emprestimos(self):
        """Retorna todos os empréstimos realizados."""
        return Emprestimos.listar_emprestimos()

    def adicionar_emprestimo(self, codigo_cliente, codigo_livro):
        """Adiciona um novo empréstimo."""
        return Emprestimos.adicionar_emprestimo(codigo_cliente, codigo_livro)

    def renovar_emprestimo(self, codigo_emprestimo):
        """
        Renova um empréstimo existente.
        Regras:
        - Um empréstimo pode ser renovado até 3 vezes.
        """
        mensagem = Emprestimos.renovar_emprestimo(codigo_emprestimo)
        return mensagem

    def excluir_emprestimo(self, codigo_emprestimo):
        """Exclui um empréstimo existente."""
        Emprestimos.excluir_emprestimo(codigo_emprestimo)

    def visualizar_livros(self):
        """Retorna a lista de livros cadastrados."""
        return Livro.listar_livros()

    def obter_livro(self, codigo):
        """Retorna as informações de um livro específico pelo código."""
        return Livro.obter_livro(codigo)

    def adicionar_livro(self, codigo, nome, autor):
        """Adiciona um novo livro à biblioteca."""
        Livro.adicionar_livro(codigo, nome, autor)

    def editar_livro(self, codigo_atual, novo_codigo=None, novo_nome=None, novo_autor=None):
        """Edita as informações de um livro, incluindo o código."""
        Livro.editar_livro(codigo_atual, novo_codigo, novo_nome, novo_autor)

    def excluir_livro(self, codigo):
        """Exclui um livro da biblioteca."""
        Livro.remover_livro(codigo)