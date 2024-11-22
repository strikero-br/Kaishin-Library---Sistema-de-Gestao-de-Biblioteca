# model/telaLogin.py
from utils import resource_path
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from model.telaCadastro import TelaCadastro  # Classe correta com maiúscula


class telaLogin:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Kaishin Library - Login")
        self.janela.configure(bg="#f0f0f0")

        # Define o tamanho da janela
        window_width = 500
        window_height = 700
        self.center_window(self.janela, window_width, window_height)

        self.janela.resizable(False, False)

        # Estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TLabel', font=('Helvetica', 12), background="#f0f0f0")
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TEntry', font=('Helvetica', 12))
        self.style.configure('Header.TLabel', font=('Helvetica', 24, 'bold'), background="#f0f0f0")

        # Título
        self.label_titulo = ttk.Label(self.janela, text="Bem-Vindo à Kaishin Library", style='Header.TLabel')
        self.label_titulo.pack(pady=(20, 10))

        # Logomarca
        self.carregar_logo()

        # Container para campos
        self.container = Frame(self.janela, bg="#f0f0f0")
        self.container.pack(pady=20)

        # Usuário
        self.label_usuario = ttk.Label(self.container, text="Usuário:")
        self.label_usuario.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entrada_usuario = ttk.Entry(self.container, width=30)
        self.entrada_usuario.grid(row=0, column=1, padx=5, pady=5)

        # Senha
        self.label_senha = ttk.Label(self.container, text="Senha:")
        self.label_senha.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entrada_senha = ttk.Entry(self.container, width=30, show="*")
        self.entrada_senha.grid(row=1, column=1, padx=5, pady=5)

        # Botões
        self.botao_login = ttk.Button(self.janela, text="Entrar", command=self.realizar_login)
        self.botao_login.pack(pady=10)

        self.botao_criar_conta = ttk.Button(self.janela, text="Criar Conta", command=self.abrir_cadastro)
        self.botao_criar_conta.pack(pady=5)

        self.janela.mainloop()

    def center_window(self, window, width, height):
        """Centraliza a janela na tela do usuário."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        window.geometry(f'{width}x{height}+{x}+{y}')

    def carregar_logo(self):
        """Carrega e exibe a logomarca abaixo do título"""
        try:
            caminho_logo = resource_path("imagens", "logo.png")
            imagem = Image.open(caminho_logo)
            imagem = imagem.resize((200, 200), Image.LANCZOS)  # Substituição de ANTIALIAS por LANCZOS
            self.logo = ImageTk.PhotoImage(imagem)

            self.label_logo = Label(self.janela, image=self.logo, bg="#f0f0f0")
            self.label_logo.image = self.logo  # Manter referência da imagem
            self.label_logo.pack(pady=(0, 10))
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Arquivo da logo não encontrado: {caminho_logo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao carregar a logo: {e}")

    def realizar_login(self):
        """Valida as credenciais de login"""
        usuario_nome = self.entrada_usuario.get().strip().lower()
        senha = self.entrada_senha.get().strip()

        try:
            arquivo_path = os.path.join("arquivos.txt", "usuarios.txt")
            with open(arquivo_path, "r") as arquivo:
                for linha_num, linha in enumerate(arquivo, start=1):
                    linha = linha.strip()
                    if not linha:
                        continue  # Pula linhas vazias

                    campos = linha.split(";")
                    if len(campos) < 5:
                        print(f"Linha {linha_num} mal formatada ou com campos insuficientes: '{linha}'")
                        continue  # Pula linhas mal formatadas

                    id_usuario = campos[0]
                    gmail = campos[1]
                    nome_registrado = campos[2]
                    senha_registrada = campos[3]
                    tipo_usuario = campos[4]

                    if nome_registrado.lower() == usuario_nome and senha_registrada == senha:
                        messagebox.showinfo("Login realizado com sucesso", f"Bem-vindo, {nome_registrado}!")
                        self.abrir_tela_principal(tipo_usuario, nome_registrado, senha_registrada, gmail)
                        return

                messagebox.showerror("Erro ao fazer login", "Usuário ou senha incorretos!")
        except FileNotFoundError:
            messagebox.showerror("Erro", "Arquivo de usuários não encontrado. Nenhum usuário cadastrado!")
        except Exception as e:
            import traceback
            traceback.print_exc()
            messagebox.showerror("Erro", f"Ocorreu um erro ao validar o login: {e}")

    def abrir_tela_principal(self, tipo_usuario, nome_usuario, senha_usuario, gmail_usuario):
        """Abre a Tela Principal após login bem-sucedido"""
        self.janela.destroy()  # Fecha a janela atual

        # Importação local para evitar importação circular
        from model.telaPrincipal import TelaPrincipal

        # Criar a nova janela do programa principal
        root = Tk()
        root.title("Kaishin Library - Programa Principal")
        root.geometry("1200x800")
        root.configure(bg="#f0f0f0")

        # Centralizar a janela principal
        self.center_window_main(root, 1200, 800)

        tela_principal = TelaPrincipal(root, tipo_usuario, nome_usuario, senha_usuario, gmail_usuario)
        tela_principal.pack(fill="both", expand=True)

        root.mainloop()

    def center_window_main(self, window, width, height):
        """Centraliza a janela principal na tela do usuário."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        window.geometry(f'{width}x{height}+{x}+{y}')

    def abrir_cadastro(self):
        """Abre a Tela de Cadastro"""
        self.janela.withdraw()  # Esconde a janela de login
        self.cadastro_window = Toplevel()
        self.cadastro_window.title("Kaishin Library - Cadastro")
        window_width = 500
        window_height = 700
        self.center_window_toplevel(self.cadastro_window, window_width, window_height)
        self.cadastro_window.resizable(False, False)
        self.cadastro_window.configure(bg="#f0f0f0")

        # Importação local para evitar importação circular
        from model.telaCadastro import TelaCadastro

        # Cria uma instância da TelaCadastro dentro do Toplevel
        self.tela_cadastro = TelaCadastro(parent=self.cadastro_window, voltar_callback=self.voltar_login)
        self.tela_cadastro.pack(fill="both", expand=True)

    def center_window_toplevel(self, window, width, height):
        """Centraliza a janela Toplevel na tela do usuário."""
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        window.geometry(f'{width}x{height}+{x}+{y}')

    def voltar_login(self):
        """Volta para a Tela de Login a partir da Tela de Cadastro"""
        self.cadastro_window.destroy()
        self.janela.deiconify()  # Mostra novamente a janela de login
