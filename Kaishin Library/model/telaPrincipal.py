# telaPrincipal.py
from utils import resource_path
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from model.bibliotecario import Bibliotecario
from model.cliente import Cliente
from datetime import datetime
from tkinter import PhotoImage, Label
from PIL import Image, ImageTk  # Importar Pillow para redimensionamento
import os

class TelaPrincipal(Frame):
    def __init__(self, parent, tipo_usuario, nome_usuario, senha_usuario, gmail_usuario):
        super().__init__(parent)
        self.parent = parent
        self.tipo_usuario = tipo_usuario
        self.nome_usuario = nome_usuario
        self.senha_usuario = senha_usuario
        self.gmail_usuario = gmail_usuario

        # Instância do usuário específico
        if tipo_usuario == "Bibliotecario":
            self.usuario = Bibliotecario(nome_usuario)
        elif tipo_usuario == "Cliente":
            self.usuario = Cliente(nome_usuario)
        else:
            messagebox.showerror("Erro", f"Tipo de usuário desconhecido: {tipo_usuario}")
            parent.destroy()
            return

        # Definição das cores
        self.cor_fundo = '#f0f0f0'        # Cor de fundo padrão
        self.cor_secundaria = '#ffffff'   # Cor secundária branca
        self.cor_botoes = '#d9d9d9'       # Cor padrão para botões
        self.cor_borda = '#000000'        # Preto para bordas e texto
        self.cor_contorno = '#6a9c2d'     # Verde para contornos

        # Configuração do estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.configure('TNotebook.Tab', font=('Helvetica', 18, 'bold'))  # Aumentando o tamanho das abas
        self.style.configure('Header.TLabel', font=('Helvetica', 20, 'bold'))

        # Estilo personalizado para botões com contorno verde e texto em negrito
        self.style.configure('Green.TButton',
                             borderwidth=1,
                             relief='solid',
                             foreground=self.cor_contorno,
                             background=self.cor_fundo,
                             font=('Helvetica', 12, 'bold'))  # Texto em negrito
        self.style.map('Green.TButton',
                       foreground=[('active', self.cor_contorno)],
                       background=[('active', '#e6ffe6')])  # Cor de fundo quando ativo (opcional)

        # Centralizar a janela principal
        self.centralizar_janela(1200, 800)
        self.parent.title("Kaishin Library")
        self.pack(fill='both', expand=True)

        # Cabeçalho com nome e logo
        self.criar_cabecalho()

        # Frame Externo com Contorno Verde
        self.frame_externo = Frame(self, bg=self.cor_contorno, bd=2, relief='solid')
        self.frame_externo.pack(fill='both', expand=True, padx=10, pady=10)

        # Notebook para as seções dentro do frame_externo
        self.notebook = ttk.Notebook(self.frame_externo)
        self.notebook.pack(fill='both', expand=True)

        # Seções diretamente adicionadas ao Notebook
        # Seção Livros
        self.frame_livros = Frame(self.notebook, bg=self.cor_fundo)
        self.notebook.add(self.frame_livros, text="Livros")

        # Seção Empréstimos
        self.frame_emprestimos = Frame(self.notebook, bg=self.cor_fundo)
        self.notebook.add(self.frame_emprestimos, text="Empréstimos")

        # Seção Sobre Nós
        self.frame_sobre = Frame(self.notebook, bg=self.cor_fundo)
        self.notebook.add(self.frame_sobre, text="Sobre Nós")

        # Seção Perfil
        self.frame_perfil = Frame(self.notebook, bg=self.cor_fundo)
        self.notebook.add(self.frame_perfil, text="Perfil")

        # Criar conteúdo das seções
        self.criar_secao_livros()
        self.criar_secao_emprestimos()
        self.criar_secao_sobre()
        self.criar_secao_perfil()

    def centralizar_janela(self, largura, altura):
        """Centraliza a janela principal na tela"""
        self.parent.geometry(f"{largura}x{altura}")
        self.parent.update_idletasks()
        width = self.parent.winfo_width()
        height = self.parent.winfo_height()
        x = (self.parent.winfo_screenwidth() // 2) - (width // 2)
        y = (self.parent.winfo_screenheight() // 2) - (height // 2)
        self.parent.geometry(f'{width}x{height}+{x}+{y}')

    def criar_cabecalho(self):
        """Cria o cabeçalho com o nome e logo da empresa, alinhados ao lado direito inferior"""
        cabecalho = Frame(self.parent, bg=self.cor_fundo)
        cabecalho.pack(fill='x')

        # Criar um frame dentro do cabeçalho alinhado à direita e inferior
        cabecalho_direito = Frame(cabecalho, bg=self.cor_fundo)
        cabecalho_direito.pack(side=RIGHT, anchor='s', padx=10, pady=10)  # 's' para alinhar ao sul (inferior)

        # Carregar a imagem com Pillow
        try:
            caminho_logo = resource_path("imagens", "logo.png")
            image = Image.open(caminho_logo)

            # Manter a proporção da imagem
            desired_height = 50
            aspect_ratio = image.width / image.height
            new_width = int(desired_height * aspect_ratio)
            image = image.resize((new_width, desired_height), Image.LANCZOS)

            # Converter para PhotoImage do Tkinter
            self.logo_image = ImageTk.PhotoImage(image)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar a logo: {e}")
            self.logo_image = None

        # Criar o Label com a imagem (logo) se a imagem foi carregada com sucesso
        if self.logo_image:
            label_logo = Label(cabecalho_direito, image=self.logo_image, bg=self.cor_fundo)
            label_logo.pack(side=LEFT, padx=5, pady=5)
        else:
            label_logo = None  # Se a imagem não for carregada, não exibe nada

        # Criar o Label com o nome da empresa
        label_nome_empresa = Label(cabecalho_direito, text="Kaishin Library", font=('Helvetica', 24, 'bold'),
                                   bg=self.cor_fundo, fg=self.cor_borda)
        label_nome_empresa.pack(side=LEFT, padx=10, pady=5)

    def criar_secao_livros(self):
        """Cria a seção de Livros"""
        label_livros = ttk.Label(self.frame_livros, text=f"Bem-vindo, {self.nome_usuario}!", style='Header.TLabel')
        label_livros.pack(pady=10)

        # Campo de pesquisa e botão "Adicionar Livro"
        search_frame = Frame(self.frame_livros, bg=self.cor_fundo)
        search_frame.pack(pady=10)  # Removido anchor='w' para centralizar

        self.search_var = StringVar()
        entry_search = ttk.Entry(search_frame, textvariable=self.search_var, font=('Helvetica', 12), width=30)
        entry_search.pack(side=LEFT, padx=5)
        entry_search.bind('<Return>', lambda event: self.atualizar_lista_livros())

        btn_search = ttk.Button(search_frame, text="Pesquisar", command=self.atualizar_lista_livros, style='Green.TButton')
        btn_search.pack(side=LEFT, padx=5)

        if self.tipo_usuario == "Bibliotecario":
            btn_add = ttk.Button(search_frame, text="Adicionar Livro", command=self.adicionar_livro, style='Green.TButton')
            btn_add.pack(side=LEFT, padx=5)

        # Implementar rolagem com mouse
        container = Frame(self.frame_livros, bg=self.cor_fundo)
        container.pack(fill='both', expand=True)

        self.canvas_livros = Canvas(container, bg=self.cor_fundo, highlightthickness=0)
        self.scrollbar_livros = ttk.Scrollbar(container, orient=VERTICAL, command=self.canvas_livros.yview)
        self.canvas_livros.configure(yscrollcommand=self.scrollbar_livros.set)

        self.lista_livros_frame = Frame(self.canvas_livros, bg=self.cor_fundo)

        # Crie a janela do Canvas e salve sua referência
        self.canvas_livros_window = self.canvas_livros.create_window((0, 0), window=self.lista_livros_frame, anchor='nw')

        self.canvas_livros.pack(side=LEFT, fill='both', expand=True)
        self.scrollbar_livros.pack(side=RIGHT, fill='y')

        self.lista_livros_frame.bind("<Configure>", lambda event: self.canvas_livros.configure(
            scrollregion=self.canvas_livros.bbox("all")))

        # Ajustar a largura do Frame interno para coincidir com a largura do Canvas
        self.canvas_livros.bind("<Configure>", self._on_canvas_livros_configure)

        # Permitir rolagem com o mouse em qualquer lugar
        self.canvas_livros.bind("<Enter>", self._bound_to_mousewheel_livros)
        self.canvas_livros.bind("<Leave>", self._unbound_to_mousewheel_livros)

        self.atualizar_lista_livros()

    def _on_canvas_livros_configure(self, event):
        """Ajusta a largura do Frame interno para coincidir com a largura do Canvas"""
        canvas_width = event.width
        self.canvas_livros.itemconfig(self.canvas_livros_window, width=canvas_width)

    def _bound_to_mousewheel_livros(self, event):
        self.canvas_livros.bind_all("<MouseWheel>", self._on_mousewheel_livros)

    def _unbound_to_mousewheel_livros(self, event):
        self.canvas_livros.unbind_all("<MouseWheel>")

    def _on_mousewheel_livros(self, event):
        self.canvas_livros.yview_scroll(int(-1*(event.delta/120)), "units")

    def atualizar_lista_livros(self):
        """Atualiza a lista de livros exibida"""
        for widget in self.lista_livros_frame.winfo_children():
            widget.destroy()

        livros = self.usuario.visualizar_livros()
        print(f"Livros retornados: {livros}")  # Depuração
        filtro = self.search_var.get().lower()

        livros_filtrados = [livro for livro in livros if filtro in livro['nome'].lower() or filtro in livro['autor'].lower()]
        print(f"Livros filtrados: {livros_filtrados}")  # Depuração

        if not livros_filtrados:
            label_no_results = ttk.Label(
                self.lista_livros_frame,
                text="Nenhum livro encontrado.",
                font=('Helvetica', 14),
                anchor='center'
            )
            label_no_results.pack(pady=20, fill='x', expand=True)
            return

        for idx, livro in enumerate(livros_filtrados):
            frame_livro = Frame(self.lista_livros_frame, bg=self.cor_secundaria, bd=1, relief='solid')
            frame_livro.pack(fill='x', padx=10, pady=5)

            # Limitar o comprimento do título do livro
            titulo_formatado = (livro['nome'][:497] + '...') if len(livro['nome']) > 500 else livro['nome']
            autor_formatado = (livro['autor'][:97] + '...') if len(livro['autor']) > 100 else livro['autor']

            label_info = ttk.Label(
                frame_livro,
                text=f"{livro['codigo']} - {titulo_formatado} por {autor_formatado}",
                font=('Helvetica', 12),
                wraplength=800,  # Ajuste conforme a largura da janela
                justify=LEFT
            )
            label_info.pack(side=LEFT, padx=10, pady=5, fill='x', expand=True)

            btn_visualizar = ttk.Button(frame_livro, text="Visualizar Livro",
                                        command=lambda l=livro: self.visualizar_livro(l), style='Green.TButton')
            btn_visualizar.pack(side=RIGHT, padx=10, pady=5)

    def visualizar_livro(self, livro):
        """Abre uma nova janela com as opções para o livro selecionado"""
        janela = Toplevel(self.parent)
        janela.title(f"Livro - {livro['nome']}")
        janela.geometry("500x400")  # Tamanho fixo da janela
        janela.configure(bg=self.cor_fundo)

        # Centralizar a janela
        self.centralizar_janela_secundaria(janela)

        # Definir wraplength com base na largura da janela
        wrap_length = 460  # 500 - 40 (margem de 20 pixels de cada lado)

        label_nome = ttk.Label(janela, text=f"Nome: {livro['nome']}", font=('Helvetica', 14, 'bold'),
                               wraplength=wrap_length, background=self.cor_fundo, justify=LEFT)
        label_nome.pack(pady=10, padx=20, anchor='w')

        label_autor = ttk.Label(janela, text=f"Autor: {livro['autor']}", font=('Helvetica', 14, 'bold'),
                                wraplength=wrap_length, background=self.cor_fundo, justify=LEFT)
        label_autor.pack(pady=10, padx=20, anchor='w')

        if self.tipo_usuario == "Cliente":
            btn_alugar = ttk.Button(janela, text="Alugar Livro",
                                    command=lambda: self.alugar_livro(livro['codigo'], janela), style='Green.TButton')
            btn_alugar.pack(pady=20)
        elif self.tipo_usuario == "Bibliotecario":
            btn_editar = ttk.Button(janela, text="Editar Livro",
                                    command=lambda: self.editar_livro(livro['codigo'], janela), style='Green.TButton')
            btn_editar.pack(pady=10)
            btn_excluir = ttk.Button(janela, text="Excluir Livro",
                                     command=lambda: self.excluir_livro(livro['codigo'], janela), style='Green.TButton')
            btn_excluir.pack(pady=10)

        # Adicionar o botão "Voltar"
        btn_voltar = ttk.Button(janela, text="Voltar", command=janela.destroy, style='Green.TButton')
        btn_voltar.pack(pady=20)  # Aumentado o padding para evitar sobreposição

    def centralizar_janela_secundaria(self, janela):
        """Centraliza uma janela secundária"""
        janela.update_idletasks()
        width = janela.winfo_width()
        height = janela.winfo_height()
        x = (janela.winfo_screenwidth() // 2) - (width // 2)
        y = (janela.winfo_screenheight() // 2) - (height // 2)
        janela.geometry(f'{width}x{height}+{x}+{y}')

    def alugar_livro(self, codigo_livro, janela):
        """Função para o cliente alugar um livro"""
        mensagem = self.usuario.realizar_emprestimo(codigo_livro)
        messagebox.showinfo("Empréstimo", mensagem)
        janela.destroy()
        self.atualizar_lista_emprestimos()

    def editar_livro(self, codigo_livro, janela):
        """Função para o bibliotecário editar um livro"""
        def confirmar_edicao():
            novo_codigo = entry_codigo.get().strip()
            novo_nome = entry_nome.get().strip()
            novo_autor = entry_autor.get().strip()

            # Verificar limites de caracteres
            if len(novo_codigo) > 10:
                messagebox.showerror("Erro", "O código do livro não pode exceder 10 caracteres.")
                return
            if len(novo_nome) > 500:
                messagebox.showerror("Erro", "O nome do livro não pode exceder 500 caracteres.")
                return
            if len(novo_autor) > 100:
                messagebox.showerror("Erro", "O autor do livro não pode exceder 100 caracteres.")
                return

            if not novo_codigo or not novo_nome or not novo_autor:
                messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                return
            try:
                self.usuario.editar_livro(codigo_livro, novo_codigo, novo_nome, novo_autor)
                messagebox.showinfo("Editar Livro", "Livro atualizado com sucesso!")
                janela_editar.destroy()
                janela.destroy()
                self.atualizar_lista_livros()
            except ValueError as e:
                messagebox.showerror("Erro ao editar livro", str(e))
                # Não fecha a janela para permitir correções

        janela_editar = Toplevel(self.parent)
        janela_editar.title("Editar Livro")
        janela_editar.geometry("500x400")  # Tamanho fixo da janela
        janela_editar.configure(bg=self.cor_fundo)

        # Centralizar a janela
        self.centralizar_janela_secundaria(janela_editar)

        # Obter dados atuais do livro
        livro_atual = self.usuario.obter_livro(codigo_livro)
        if not livro_atual:
            messagebox.showerror("Erro", f"Livro com código {codigo_livro} não encontrado.")
            janela_editar.destroy()
            return

        label_codigo = ttk.Label(janela_editar, text="Novo Código:", font=('Helvetica', 12, 'bold'),
                                 background=self.cor_fundo)
        label_codigo.pack(pady=5, padx=20, anchor='w')
        entry_codigo = ttk.Entry(janela_editar, font=('Helvetica', 12), width=40)
        entry_codigo.pack(pady=5, padx=20, anchor='w')
        entry_codigo.insert(0, livro_atual['codigo'])

        label_nome = ttk.Label(janela_editar, text="Novo Nome:", font=('Helvetica', 12, 'bold'),
                               background=self.cor_fundo)
        label_nome.pack(pady=5, padx=20, anchor='w')
        entry_nome = ttk.Entry(janela_editar, font=('Helvetica', 12), width=40)
        entry_nome.pack(pady=5, padx=20, anchor='w')
        entry_nome.insert(0, livro_atual['nome'])

        label_autor = ttk.Label(janela_editar, text="Novo Autor:", font=('Helvetica', 12, 'bold'),
                                background=self.cor_fundo)
        label_autor.pack(pady=5, padx=20, anchor='w')
        entry_autor = ttk.Entry(janela_editar, font=('Helvetica', 12), width=40)
        entry_autor.pack(pady=5, padx=20, anchor='w')
        entry_autor.insert(0, livro_atual['autor'])

        btn_confirmar = ttk.Button(janela_editar, text="Salvar Alterações", command=confirmar_edicao, style='Green.TButton')
        btn_confirmar.pack(pady=20)

        # Adicionar o botão "Voltar" na janela de edição
        btn_voltar = ttk.Button(janela_editar, text="Voltar", command=janela_editar.destroy, style='Green.TButton')
        btn_voltar.pack(pady=10)  # Aumentado o padding para evitar sobreposição

    def excluir_livro(self, codigo_livro, janela):
        """Função para o bibliotecário excluir um livro"""
        resposta = messagebox.askyesno("Excluir Livro", "Tem certeza que deseja excluir este livro?")
        if resposta:
            try:
                self.usuario.excluir_livro(codigo_livro)
                messagebox.showinfo("Excluir Livro", "Livro excluído com sucesso!")
            except ValueError as e:
                messagebox.showerror("Erro ao excluir livro", str(e))
            finally:
                self.atualizar_lista_livros()

    def adicionar_livro(self):
        """Adiciona um livro (apenas para Bibliotecário)"""
        if self.tipo_usuario == "Bibliotecario":
            def confirmar_adicao():
                codigo = entry_codigo.get().strip()
                nome = entry_nome.get().strip()
                autor = entry_autor.get().strip()

                # Verificar limites de caracteres
                if len(codigo) > 10:
                    messagebox.showerror("Erro", "O código do livro não pode exceder 10 caracteres.")
                    return
                if len(nome) > 500:
                    messagebox.showerror("Erro", "O nome do livro não pode exceder 500 caracteres.")
                    return
                if len(autor) > 100:
                    messagebox.showerror("Erro", "O autor do livro não pode exceder 100 caracteres.")
                    return

                if not codigo or not nome or not autor:
                    messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                    return
                try:
                    self.usuario.adicionar_livro(codigo, nome, autor)
                    messagebox.showinfo("Adicionar Livro", "Livro adicionado com sucesso!")
                    janela_adicionar.destroy()
                    self.atualizar_lista_livros()
                except ValueError as e:
                    messagebox.showerror("Erro ao adicionar livro", str(e))
                    # Não fecha a janela para permitir correções

            janela_adicionar = Toplevel(self.parent)
            janela_adicionar.title("Adicionar Livro")
            janela_adicionar.geometry("500x400")  # Tamanho fixo da janela
            janela_adicionar.configure(bg=self.cor_fundo)

            # Centralizar a janela
            self.centralizar_janela_secundaria(janela_adicionar)

            label_titulo = ttk.Label(janela_adicionar, text="Adicionar Novo Livro", style='Header.TLabel')
            label_titulo.pack(pady=10)

            frame_form = Frame(janela_adicionar, bg=self.cor_fundo)
            frame_form.pack(pady=10)

            label_codigo = ttk.Label(frame_form, text="Código:", font=('Helvetica', 12, 'bold'),
                                     background=self.cor_fundo)
            label_codigo.grid(row=0, column=0, padx=10, pady=5, sticky='e')
            entry_codigo = ttk.Entry(frame_form, font=('Helvetica', 12), width=40)
            entry_codigo.grid(row=0, column=1, padx=10, pady=5)
            entry_codigo.insert(0, "")

            label_nome = ttk.Label(frame_form, text="Nome:", font=('Helvetica', 12, 'bold'),
                                   background=self.cor_fundo)
            label_nome.grid(row=1, column=0, padx=10, pady=5, sticky='e')
            entry_nome = ttk.Entry(frame_form, font=('Helvetica', 12), width=40)
            entry_nome.grid(row=1, column=1, padx=10, pady=5)
            entry_nome.insert(0, "")

            label_autor = ttk.Label(frame_form, text="Autor:", font=('Helvetica', 12, 'bold'),
                                    background=self.cor_fundo)
            label_autor.grid(row=2, column=0, padx=10, pady=5, sticky='e')
            entry_autor = ttk.Entry(frame_form, font=('Helvetica', 12), width=40)
            entry_autor.grid(row=2, column=1, padx=10, pady=5)
            entry_autor.insert(0, "")

            btn_frame = Frame(janela_adicionar, bg=self.cor_fundo)
            btn_frame.pack(pady=20)

            btn_confirmar = ttk.Button(btn_frame, text="Adicionar", command=confirmar_adicao, style='Green.TButton')
            btn_confirmar.grid(row=0, column=0, padx=10)

            btn_cancelar = ttk.Button(btn_frame, text="Cancelar", command=janela_adicionar.destroy, style='Green.TButton')
            btn_cancelar.grid(row=0, column=1, padx=10)

            # Adicionar o botão "Voltar" na janela de adição
            btn_voltar = ttk.Button(janela_adicionar, text="Voltar", command=janela_adicionar.destroy, style='Green.TButton')
            btn_voltar.pack(pady=10)  # Aumentado o padding para evitar sobreposição

            janela_adicionar.grab_set()
            janela_adicionar.mainloop()

    def criar_secao_emprestimos(self):
        """Cria a seção de Empréstimos"""
        label_emprestimos = ttk.Label(self.frame_emprestimos, text="Empréstimos", style='Header.TLabel')
        label_emprestimos.pack(pady=10)

        # Campo de pesquisa para empréstimos
        search_frame = Frame(self.frame_emprestimos, bg=self.cor_fundo)
        search_frame.pack(pady=10)

        self.search_emprestimo_var = StringVar()
        entry_search_emprestimo = ttk.Entry(search_frame, textvariable=self.search_emprestimo_var, font=('Helvetica', 12), width=30)
        entry_search_emprestimo.pack(side=LEFT, padx=5)
        entry_search_emprestimo.bind('<Return>', lambda event: self.atualizar_lista_emprestimos())

        btn_search_emprestimo = ttk.Button(search_frame, text="Pesquisar", command=self.atualizar_lista_emprestimos, style='Green.TButton')
        btn_search_emprestimo.pack(side=LEFT, padx=5)

        # Implementar rolagem com mouse
        container = Frame(self.frame_emprestimos, bg=self.cor_fundo)
        container.pack(fill='both', expand=True)

        self.canvas_emprestimos = Canvas(container, bg=self.cor_fundo, highlightthickness=0)
        self.scrollbar_emprestimos = ttk.Scrollbar(container, orient=VERTICAL, command=self.canvas_emprestimos.yview)
        self.canvas_emprestimos.configure(yscrollcommand=self.scrollbar_emprestimos.set)

        self.lista_emprestimos_frame = Frame(self.canvas_emprestimos, bg=self.cor_fundo)

        # Crie a janela do Canvas e salve sua referência
        self.canvas_emprestimos_window = self.canvas_emprestimos.create_window((0, 0), window=self.lista_emprestimos_frame, anchor='nw')

        self.canvas_emprestimos.pack(side=LEFT, fill='both', expand=True)
        self.scrollbar_emprestimos.pack(side=RIGHT, fill='y')

        self.lista_emprestimos_frame.bind("<Configure>", lambda event: self.canvas_emprestimos.configure(
            scrollregion=self.canvas_emprestimos.bbox("all")))

        # Ajustar a largura do Frame interno para coincidir com a largura do Canvas
        self.canvas_emprestimos.bind("<Configure>", self._on_canvas_emprestimos_configure)

        # Permitir rolagem com o mouse em qualquer lugar
        self.canvas_emprestimos.bind("<Enter>", self._bound_to_mousewheel_emprestimos)
        self.canvas_emprestimos.bind("<Leave>", self._unbound_to_mousewheel_emprestimos)

        self.atualizar_lista_emprestimos()

    def _on_canvas_emprestimos_configure(self, event):
        """Ajusta a largura do Frame interno para coincidir com a largura do Canvas"""
        canvas_width = event.width
        self.canvas_emprestimos.itemconfig(self.canvas_emprestimos_window, width=canvas_width)

    def _bound_to_mousewheel_emprestimos(self, event):
        self.canvas_emprestimos.bind_all("<MouseWheel>", self._on_mousewheel_emprestimos)

    def _unbound_to_mousewheel_emprestimos(self, event):
        self.canvas_emprestimos.unbind_all("<MouseWheel>")

    def _on_mousewheel_emprestimos(self, event):
        self.canvas_emprestimos.yview_scroll(int(-1*(event.delta/120)), "units")

    def atualizar_lista_emprestimos(self):
        """Atualiza a lista de empréstimos exibida"""
        for widget in self.lista_emprestimos_frame.winfo_children():
            widget.destroy()

        emprestimos = self.usuario.visualizar_emprestimos()
        print(f"Empréstimos retornados: {emprestimos}")  # Depuração
        filtro = self.search_emprestimo_var.get().lower()

        emprestimos_filtrados = [emprestimo for emprestimo in emprestimos if filtro in emprestimo.lower()]
        print(f"Empréstimos filtrados: {emprestimos_filtrados}")  # Depuração

        if not emprestimos_filtrados:
            label_no_results = ttk.Label(
                self.lista_emprestimos_frame,
                text="Nenhum empréstimo encontrado.",
                font=('Helvetica', 14),
                anchor='center'
            )
            label_no_results.pack(pady=20, fill='x', expand=True)
            return

        for emprestimo in emprestimos_filtrados:
            campos = emprestimo.strip().split(",")
            if len(campos) < 6:
                print(f"Linha de empréstimo mal formatada ou com campos insuficientes: '{emprestimo}'")
                continue  # Pula para a próxima iteração

            # Formatar datas para o formato brasileiro com segundos
            data_emprestimo = campos[3]
            data_devolucao = campos[4]
            renovacoes = campos[5]

            try:
                data_emprestimo = datetime.strptime(data_emprestimo, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
                data_devolucao = datetime.strptime(data_devolucao, '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
            except ValueError:
                pass  # Mantém a data original se o formato não for reconhecido

            frame_emprestimo = Frame(self.lista_emprestimos_frame, bg=self.cor_secundaria, bd=1, relief='solid')
            frame_emprestimo.pack(fill='x', padx=10, pady=5)

            info = (f"Código Empréstimo: {campos[0]}, Cliente: {campos[1]}, Livro: {campos[2]}, "
                    f"Data Empréstimo: {data_emprestimo}, Data Devolução: {data_devolucao}, "
                    f"Renovações: {renovacoes}")
            label_info = ttk.Label(frame_emprestimo, text=info, font=('Helvetica', 12), wraplength=800, justify=LEFT)
            label_info.pack(side=LEFT, padx=10, pady=5, fill='x', expand=True)

            if self.tipo_usuario == "Bibliotecario":
                btn_frame = Frame(frame_emprestimo, bg=self.cor_secundaria)
                btn_frame.pack(side=RIGHT, padx=10)

                btn_renovar = ttk.Button(btn_frame, text="Renovar",
                                         command=lambda c=campos[0]: self.renovar_emprestimo(c), style='Green.TButton')
                btn_renovar.pack(side=TOP, pady=2)

                btn_excluir = ttk.Button(btn_frame, text="Excluir",
                                         command=lambda c=campos[0]: self.excluir_emprestimo(c), style='Green.TButton')
                btn_excluir.pack(side=TOP, pady=2)
            elif self.tipo_usuario == "Cliente":
                btn_renovar = ttk.Button(frame_emprestimo, text="Renovar",
                                         command=lambda c=campos[0]: self.renovar_emprestimo_cliente(c), style='Green.TButton')
                btn_renovar.pack(side=RIGHT, padx=10, pady=5)

    def renovar_emprestimo(self, codigo_emprestimo):
        """Função para o bibliotecário renovar um empréstimo"""
        mensagem = self.usuario.renovar_emprestimo(codigo_emprestimo)
        messagebox.showinfo("Renovar Empréstimo", mensagem)
        self.atualizar_lista_emprestimos()

    def excluir_emprestimo(self, codigo_emprestimo):
        """Função para o bibliotecário excluir um empréstimo"""
        resposta = messagebox.askyesno("Excluir Empréstimo", "Tem certeza que deseja excluir este empréstimo?")
        if resposta:
            try:
                self.usuario.excluir_emprestimo(codigo_emprestimo)
                messagebox.showinfo("Excluir Empréstimo", "Empréstimo excluído com sucesso!")
            except ValueError as e:
                messagebox.showerror("Erro ao excluir empréstimo", str(e))
            finally:
                self.atualizar_lista_emprestimos()

    def renovar_emprestimo_cliente(self, codigo_emprestimo):
        """Função para o cliente renovar seu empréstimo"""
        mensagem = self.usuario.renovar_emprestimo(codigo_emprestimo)
        messagebox.showinfo("Renovar Empréstimo", mensagem)
        self.atualizar_lista_emprestimos()

    def criar_secao_sobre(self):
        """Cria a seção Sobre Nós"""
        # Contêiner para implementar rolagem
        container = Frame(self.frame_sobre, bg=self.cor_fundo)
        container.pack(fill='both', expand=True, padx=10, pady=10)

        self.canvas_sobre = Canvas(container, bg=self.cor_fundo, highlightthickness=0)
        self.scrollbar_sobre = ttk.Scrollbar(container, orient=VERTICAL, command=self.canvas_sobre.yview)
        self.canvas_sobre.configure(yscrollcommand=self.scrollbar_sobre.set)

        self.sobre_frame = Frame(self.canvas_sobre, bg=self.cor_fundo)

        # Crie a janela do Canvas e salve sua referência
        self.canvas_sobre_window = self.canvas_sobre.create_window((0, 0), window=self.sobre_frame, anchor='nw')

        self.canvas_sobre.pack(side=LEFT, fill='both', expand=True)
        self.scrollbar_sobre.pack(side=RIGHT, fill='y')

        self.sobre_frame.bind("<Configure>", lambda event: self.canvas_sobre.configure(scrollregion=self.canvas_sobre.bbox("all")))
        self.canvas_sobre.bind("<Configure>", self._on_canvas_sobre_configure)

        # Permitir rolagem com o mouse em qualquer lugar
        self.canvas_sobre.bind("<Enter>", self._bound_to_mousewheel_sobre)
        self.canvas_sobre.bind("<Leave>", self._unbound_to_mousewheel_sobre)

        # Adicionar conteúdo na seção
        label_sobre_titulo = ttk.Label(
            self.sobre_frame,
            text="Kaishin Library: Uma biblioteca dedicada ao aprendizado.",
            style='Header.TLabel'
        )
        label_sobre_titulo.pack(pady=20)

        historia_texto = (
            "A Kaishin Library nasceu em 2024, criada por um grupo de estudantes movidos pelo desejo de transformar o acesso ao conhecimento. "
            "Mais do que um projeto, somos uma iniciativa comprometida com a ideia de que o aprendizado é um direito universal e não um privilégio reservado a poucos. "
            "Inspirados por essa visão, nossa missão é clara: reunir e oferecer conhecimento de forma acessível e organizada, para que qualquer pessoa, em qualquer lugar, tenha a oportunidade de aprender e crescer.\n\n"
            "Começamos com um sistema básico de biblioteca, capaz de organizar e facilitar o acesso a livros e informações. Entretanto, nossos objetivos vão além. Queremos construir uma plataforma que vá muito além da gestão de empréstimos: uma comunidade vibrante que centralize o saber e o torne acessível a todos, sem abrir mão da qualidade.\n\n"
            "Vivemos em um mundo onde a maior parte do conhecimento está disponível na internet, mas encontrar conteúdo de qualidade é um desafio constante. "
            "A Kaishin Library foi idealizada para solucionar essa lacuna, reunindo informações de forma clara, confiável e acessível. Nosso objetivo principal é democratizar o aprendizado, permitindo que qualquer pessoa, independentemente de suas condições financeiras, tenha acesso a temas que vão desde ciências humanas até artes, tecnologia e muito mais.\n\n"
            "Nosso sonho é grande, mas nosso compromisso é ainda maior. A Kaishin Library é, por enquanto, uma ideia em construção, mas acreditamos firmemente que, com esforço e dedicação, ela se tornará um marco no acesso à cultura e ao conhecimento. "
            "Porque, no final das contas, o que nos impulsiona é a certeza de que o aprendizado compartilhado é a chave para uma sociedade mais justa, evoluída e conectada."
        )

        label_sobre_historia = ttk.Label(
            self.sobre_frame,
            text=historia_texto,
            justify=LEFT,
            wraplength=1000,  # Ajustado para melhor visualização
            font=('Helvetica', 12)
        )
        label_sobre_historia.pack(pady=10)

        # Adicionando a seção "Nossa Equipe"
        label_nossa_equipe = ttk.Label(self.sobre_frame, text="Nossa Equipe", style='Header.TLabel')
        label_nossa_equipe.pack(pady=20)

        equipe_texto = (
            "Jonathan Pereira - Delmonte - Arquiteto de Software\n"
            "Nicolas Isaac P. de Jesus - Desenvolvedor Front-end\n"
            "Iann Mariano Carvalho - Desenvolvedor Back-end\n"
            "Mateus Guilherme Xavier Barbosa - Testador (QA) / Suporte Técnico\n"
            "Renato Ramos Teófilo - Analista de Sistema / Designer de Experiência do Usuário (UX)"
        )

        label_equipe = ttk.Label(
            self.sobre_frame,
            text=equipe_texto,
            justify=LEFT,
            font=('Helvetica', 12),
            wraplength=1000  # Ajustado para melhor visualização
        )
        label_equipe.pack(pady=10)

    def _on_canvas_sobre_configure(self, event):
        """Ajusta a largura do Frame interno para coincidir com a largura do Canvas"""
        canvas_width = event.width
        self.canvas_sobre.itemconfig(self.canvas_sobre_window, width=canvas_width)

    def _bound_to_mousewheel_sobre(self, event):
        self.canvas_sobre.bind_all("<MouseWheel>", self._on_mousewheel_sobre)

    def _unbound_to_mousewheel_sobre(self, event):
        self.canvas_sobre.unbind_all("<MouseWheel>")

    def _on_mousewheel_sobre(self, event):
        self.canvas_sobre.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def criar_secao_perfil(self):
        """Cria a seção Perfil"""
        label_titulo_perfil = ttk.Label(self.frame_perfil, text="Informações do Perfil", style='Header.TLabel')
        label_titulo_perfil.pack(pady=20)

        label_nome = ttk.Label(self.frame_perfil, text=f"Nome: {self.nome_usuario}", font=('Helvetica', 14))
        label_nome.pack(pady=5)

        label_gmail = ttk.Label(self.frame_perfil, text=f"Gmail: {self.gmail_usuario}", font=('Helvetica', 14))
        label_gmail.pack(pady=5)

        label_senha = ttk.Label(self.frame_perfil, text=f"Senha: {self.senha_usuario}", font=('Helvetica', 14))
        label_senha.pack(pady=5)

        label_tipo_usuario = ttk.Label(self.frame_perfil, text=f"Tipo de Usuário: {self.tipo_usuario}",
                                       font=('Helvetica', 14))
        label_tipo_usuario.pack(pady=5)

        btn_sair = ttk.Button(self.frame_perfil, text="Sair", command=self.sair, style='Green.TButton')
        btn_sair.pack(pady=20)

    def sair(self):
        """Função para sair e voltar à tela de login"""
        self.parent.destroy()
        from model.telaLogin import telaLogin
        telaLogin()
