# cliente.py
from model.livro import Livro
from model.emprestimos import Emprestimos

class Cliente:
    def __init__(self, nome):
        self.nome = nome

    # Funções relacionadas a empréstimos
    def visualizar_emprestimos(self):
        """Retorna os empréstimos específicos do cliente."""
        return Emprestimos.listar_emprestimos_cliente(self.nome)

    def realizar_emprestimo(self, codigo_livro):
        """
        Realiza um empréstimo de um livro.
        Regras:
        - Apenas 1 empréstimo por livro por cliente.
        - Validade inicial do empréstimo: 10 a 15 dias.
        """
        emprestimos_cliente = self.visualizar_emprestimos()
        if any(codigo_livro == emprestimo.split(",")[2] for emprestimo in emprestimos_cliente):
            return f"O livro com código {codigo_livro} já foi alugado por você."

        codigo_emprestimo = Emprestimos.adicionar_emprestimo(self.nome, codigo_livro)
        return f"Empréstimo realizado com sucesso! Código do empréstimo: {codigo_emprestimo}"

    def renovar_emprestimo(self, codigo_emprestimo):
        """
        Renova o empréstimo do cliente.
        """
        emprestimos_cliente = self.visualizar_emprestimos()
        if any(codigo_emprestimo == emprestimo.split(",")[0] for emprestimo in emprestimos_cliente):
            mensagem = Emprestimos.renovar_emprestimo(codigo_emprestimo)
            return mensagem
        else:
            return "Empréstimo não encontrado ou não pertence a este cliente."

    # Funções relacionadas a livros
    def visualizar_livros(self):
        """Retorna a lista de livros disponíveis na biblioteca."""
        return Livro.listar_livros()
