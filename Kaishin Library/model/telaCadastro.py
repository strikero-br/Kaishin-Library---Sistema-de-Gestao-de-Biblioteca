# model/telaCadastro.py
from utils import resource_path
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

class TelaCadastro(ttk.Frame):
    def __init__(self, parent, voltar_callback):
        super().__init__(parent)
        self.parent = parent
        self.voltar_callback = voltar_callback
        self.configure(style='TFrame', padding=20)

        # Estilo
        self.style = ttk.Style()
        self.style.configure('TFrame', background="#f0f0f0")
        self.style.configure('Header.TLabel', font=('Helvetica', 24, 'bold'), background="#f0f0f0")
        self.style.configure('TLabel', font=('Helvetica', 12), background="#f0f0f0")
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TEntry', font=('Helvetica', 12))

        # Título
        self.label_titulo = ttk.Label(self, text="Cadastro", style='Header.TLabel')
        self.label_titulo.pack(pady=(10, 10))

        # Logomarca
        self.carregar_logo()

        # Container para campos
        self.container = ttk.Frame(self)
        self.container.pack(pady=20)

        # Gmail
        self.label_gmail = ttk.Label(self.container, text="Gmail:")
        self.label_gmail.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entrada_gmail = ttk.Entry(self.container, width=30)
        self.entrada_gmail.grid(row=0, column=1, padx=5, pady=5)

        # Usuário
        self.label_usuario = ttk.Label(self.container, text="Usuário:")
        self.label_usuario.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entrada_usuario = ttk.Entry(self.container, width=30)
        self.entrada_usuario.grid(row=1, column=1, padx=5, pady=5)

        # Senha
        self.label_senha = ttk.Label(self.container, text="Senha:")
        self.label_senha.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entrada_senha = ttk.Entry(self.container, width=30, show="*")
        self.entrada_senha.grid(row=2, column=1, padx=5, pady=5)

        # Confirmar Senha
        self.label_confirmar_senha = ttk.Label(self.container, text="Confirmar Senha:")
        self.label_confirmar_senha.grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.entrada_confirmar_senha = ttk.Entry(self.container, width=30, show="*")
        self.entrada_confirmar_senha.grid(row=3, column=1, padx=5, pady=5)

        # Tipo de Usuário
        self.label_tipo_usuario = ttk.Label(self.container, text="Tipo de Usuário:")
        self.label_tipo_usuario.grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.combo_tipo_usuario = ttk.Combobox(self.container, values=["Bibliotecario", "Cliente"], state="readonly", width=28)
        self.combo_tipo_usuario.grid(row=4, column=1, padx=5, pady=5)
        self.combo_tipo_usuario.set("Cliente")

        # Ajustar as colunas para centralizar o conteúdo
        self.container.columnconfigure(0, weight=1)
        self.container.columnconfigure(1, weight=1)

        # Botões
        self.botao_cadastrar = ttk.Button(self, text="Cadastrar", command=self.realizar_cadastro)
        self.botao_cadastrar.pack(pady=10)

        self.botao_voltar = ttk.Button(self, text="Voltar", command=self.voltar_callback)
        self.botao_voltar.pack(pady=5)

    def carregar_logo(self):
        """Carrega e exibe a logomarca abaixo do título"""
        try:
            caminho_logo = resource_path("imagens", "logo.png")
            imagem = Image.open(caminho_logo)
            imagem = imagem.resize((200, 200), Image.LANCZOS)  # Substituição de ANTIALIAS por LANCZOS
            self.logo = ImageTk.PhotoImage(imagem)

            self.label_logo = Label(self, image=self.logo, background="#f0f0f0")
            self.label_logo.image = self.logo  # Manter referência da imagem
            self.label_logo.pack(pady=(0,10))
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Arquivo da logo não encontrado: {caminho_logo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar a logo: {e}")

    def realizar_cadastro(self):
        """Realiza o cadastro do novo usuário"""
        gmail = self.entrada_gmail.get().strip()
        usuario_nome = self.entrada_usuario.get().strip()
        senha = self.entrada_senha.get().strip()
        confirmar_senha = self.entrada_confirmar_senha.get().strip()
        tipo_usuario = self.combo_tipo_usuario.get().strip()

        if not self.validar_entradas(gmail, usuario_nome, senha, confirmar_senha, tipo_usuario):
            return

        try:
            arquivo_path = os.path.join("arquivos.txt", "usuarios.txt")
            ultimo_id, usuarios_existentes, emails_existentes = self.carregar_dados_existentes(arquivo_path)

            if usuario_nome.lower() in usuarios_existentes:
                messagebox.showerror("Erro ao cadastrar", "Usuário já existe!")
                return

            if gmail.lower() in emails_existentes:
                messagebox.showerror("Erro ao cadastrar", "E-mail já cadastrado!")
                return

            novo_id = ultimo_id + 1
            with open(arquivo_path, "a") as arquivo:
                arquivo.write(f"{novo_id};{gmail};{usuario_nome};{senha};{tipo_usuario}\n")

            messagebox.showinfo("Cadastro realizado", "Usuário cadastrado com sucesso! Bem-vindo(a)!")
            self.limpar_campos()
            self.voltar_callback()  # Volta para a tela de login
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar os dados: {e}")

    def validar_entradas(self, gmail, usuario_nome, senha, confirmar_senha, tipo_usuario):
        """Valida as entradas de cadastro"""
        if "@gmail.com" not in gmail:
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")
            return False
        if len(usuario_nome) < 3:
            messagebox.showerror("Erro", "O nome de usuário deve ter pelo menos 3 caracteres.")
            return False
        if len(senha) < 6:
            messagebox.showerror("Erro", "A senha deve ter pelo menos 6 caracteres.")
            return False
        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return False
        if tipo_usuario not in ["Bibliotecario", "Cliente"]:
            messagebox.showerror("Erro", "Selecione um tipo de usuário válido.")
            return False
        return True

    def carregar_dados_existentes(self, arquivo_path):
        """Carrega dados existentes de usuários"""
        try:
            with open(arquivo_path, "r") as arquivo:
                linhas = [linha.strip() for linha in arquivo if linha.strip()]
                ultimo_id = 0
                usuarios_existentes = []
                emails_existentes = []
                for linha_num, linha in enumerate(linhas, start=1):
                    campos = linha.split(";")
                    if len(campos) < 5:
                        print(f"Linha {linha_num} mal formatada ou com campos insuficientes: '{linha}'")
                        continue  # Pula linhas mal formatadas
                    id_usuario = int(campos[0])
                    gmail = campos[1].lower()
                    nome_usuario = campos[2].lower()
                    ultimo_id = max(ultimo_id, id_usuario)
                    usuarios_existentes.append(nome_usuario)
                    emails_existentes.append(gmail)
                return ultimo_id, usuarios_existentes, emails_existentes
        except FileNotFoundError:
            return 0, [], []

    def limpar_campos(self):
        """Limpa os campos de entrada após cadastro"""
        self.entrada_gmail.delete(0, END)
        self.entrada_usuario.delete(0, END)
        self.entrada_senha.delete(0, END)
        self.entrada_confirmar_senha.delete(0, END)
        self.combo_tipo_usuario.set("Cliente")
