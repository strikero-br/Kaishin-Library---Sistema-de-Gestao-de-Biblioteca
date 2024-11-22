# emprestimos.py
import os
import random
from datetime import datetime, timedelta

PASTA_ARQUIVOS = "arquivos.txt"  # Atualizado de "arquivos" para "arquivos.txt"
ARQUIVO_EMPRESTIMOS = os.path.join(PASTA_ARQUIVOS, "emprestimos.txt")

# Garantir que a pasta e o arquivo existam
os.makedirs(PASTA_ARQUIVOS, exist_ok=True)
if not os.path.exists(ARQUIVO_EMPRESTIMOS):
    with open(ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8") as f:
        pass


class Emprestimos:
    @staticmethod
    def listar_emprestimos():
        """Lista todos os empréstimos realizados."""
        with open(ARQUIVO_EMPRESTIMOS, "r", encoding="utf-8") as f:
            return [linha.strip() for linha in f if linha.strip()]

    @staticmethod
    def listar_emprestimos_cliente(codigo_cliente):
        """Lista os empréstimos específicos de um cliente."""
        emprestimos = Emprestimos.listar_emprestimos()
        return [e for e in emprestimos if e.split(",")[1] == codigo_cliente]

    @staticmethod
    def adicionar_emprestimo(codigo_cliente, codigo_livro):
        """Adiciona um novo empréstimo."""
        codigo_emprestimo = Emprestimos.gerar_codigo_emprestimo()
        dias_emprestimo = random.randint(10, 15)
        data_emprestimo = datetime.now()
        data_devolucao = data_emprestimo + timedelta(days=dias_emprestimo)
        renovacoes = 0  # Início com zero renovações
        with open(ARQUIVO_EMPRESTIMOS, "a", encoding="utf-8") as f:
            linha = f"{codigo_emprestimo},{codigo_cliente},{codigo_livro},{data_emprestimo.strftime('%Y-%m-%d %H:%M:%S')},{data_devolucao.strftime('%Y-%m-%d %H:%M:%S')},{renovacoes}\n"
            f.write(linha)
        return codigo_emprestimo

    @staticmethod
    def renovar_emprestimo(codigo_emprestimo):
        """
        Renova um empréstimo existente.
        Regras:
        - Um empréstimo pode ser renovado até 3 vezes.
        """
        emprestimos = Emprestimos.listar_emprestimos()
        emprestimo_encontrado = False
        emprestimos_atualizados = []

        for emprestimo in emprestimos:
            campos = emprestimo.strip().split(",")
            if campos[0] == codigo_emprestimo:
                emprestimo_encontrado = True
                # Verificar o número de renovações
                if len(campos) >= 6:
                    renovacoes = int(campos[5])
                else:
                    renovacoes = 0  # Se não houver campo de renovação, assumir zero

                if renovacoes >= 3:
                    return "O empréstimo já foi renovado 3 vezes e não pode ser renovado novamente."

                # Atualizar data de devolução
                data_devolucao_atual = datetime.strptime(campos[4], "%Y-%m-%d %H:%M:%S")
                nova_data_devolucao = data_devolucao_atual + timedelta(days=10)
                campos[4] = nova_data_devolucao.strftime("%Y-%m-%d %H:%M:%S")
                campos[5] = str(renovacoes + 1)
                emprestimo_atualizado = ",".join(campos)
                emprestimos_atualizados.append(emprestimo_atualizado)
            else:
                emprestimos_atualizados.append(emprestimo)

        if not emprestimo_encontrado:
            return "Empréstimo não encontrado."

        # Salvar os empréstimos atualizados
        with open(ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8") as f:
            for emprestimo in emprestimos_atualizados:
                f.write(emprestimo + "\n")

        return "Empréstimo renovado com sucesso!"

    @staticmethod
    def excluir_emprestimo(codigo_emprestimo):
        """Exclui um empréstimo existente."""
        emprestimos = Emprestimos.listar_emprestimos()
        emprestimos_atualizados = [e for e in emprestimos if not e.startswith(codigo_emprestimo + ",")]

        with open(ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8") as f:
            for emprestimo in emprestimos_atualizados:
                f.write(emprestimo + "\n")

    @staticmethod
    def gerar_codigo_emprestimo():
        """Gera um código único para cada empréstimo."""
        emprestimos = Emprestimos.listar_emprestimos()
        if not emprestimos:
            return "001"
        else:
            codigos = [int(e.split(",")[0]) for e in emprestimos]
            ultimo_codigo = max(codigos)
            return f"{ultimo_codigo + 1:03}"

    @staticmethod
    def atualizar_codigo_livro(codigo_antigo, codigo_novo):
        """Atualiza o código do livro nos registros de empréstimos."""
        emprestimos = []
        with open(ARQUIVO_EMPRESTIMOS, "r", encoding="utf-8") as f:
            for linha in f:
                emprestimos.append(linha.strip())

        with open(ARQUIVO_EMPRESTIMOS, "w", encoding="utf-8") as f:
            for emprestimo in emprestimos:
                campos = emprestimo.strip().split(",")
                if len(campos) >= 6:
                    if campos[2] == codigo_antigo:
                        campos[2] = codigo_novo
                    f.write(",".join(campos) + "\n")
                else:
                    f.write(emprestimo + "\n")