<p align="right">
  <a href="https://github.com/strikero-br/Kaishin-Library---Sistema-de-Gestao-de-Biblioteca">
    <img src="https://img.icons8.com/material-outlined/48/000000/github.png" alt="GitHub" width="80" height="80">
  </a>
</p>

# Kaishin Library - Sistema de Gestão de Biblioteca 

**Kaishin Library** é um sistema desenvolvido em **Python** para gerenciar bibliotecas, com funcionalidades robustas, como o cadastro de livros, gerenciamento de usuários e controle de empréstimos. 

---

## 🚀 **Baixe o Setup e Instale o Programa**
### 👉 [Clique aqui para baixar o executável: Kaishin Library](https://drive.google.com/file/d/1XGQ-7CWQrnbaIiEF6rBf8MWZ9qR41QgJ/view?usp=drive_link)

> **⚡ Recomendado**: Ideal para usuários finais que desejam uma instalação simples e prática sem acessar o código-fonte.  
> Basta baixar o arquivo e seguir as instruções do instalador.

---


## **Funcionalidades Principais**

- **Cadastro de Livros:** Adicione, edite e remova informações de livros no sistema.
- **Gerenciamento de Usuários:** Registre e administre usuários, sejam eles clientes ou bibliotecários.
- **Controle de Empréstimos:** Realize o registro e acompanhamento de empréstimos e devoluções de livros.
- **Interface Gráfica:** Interface intuitiva construída com **Tkinter**.
- **Sistema Modularizado:** Código organizado para facilitar a manutenção e futuras melhorias.

---

## **Tecnologias Utilizadas**

- **Python:** Linguagem principal para desenvolvimento.
- **Tkinter:** Biblioteca padrão para criação da interface gráfica.
- **Pillow:** Utilizada para manipulação e redimensionamento de imagens.

---

## **Como Instalar e Executar o Projeto**

### **1. Instalação do Setup (Executável)**
Para usuários finais, recomendamos instalar o programa diretamente com o setup:
1. Acesse o link: [Baixar Setup - Kaishin Library](https://drive.google.com/file/d/1XGQ-7CWQrnbaIiEF6rBf8MWZ9qR41QgJ/view?usp=drive_link)
2. Siga o instalador para instalar o programa no diretório desejado.
3. Após a instalação, execute o atalho criado na área de trabalho.

---

### **2. Execução do Código (Desenvolvedores)**

Caso prefira trabalhar diretamente com o código-fonte:

#### **Pré-requisitos**
- Python 3.10 ou superior.
- Dependências listadas no arquivo `requirements.txt`.

#### **Passos:**
1. Clone o repositório:
   ```bash
   git clone https://github.com/strikero-br/Kaishin-Library---Sistema-de-Gestao-de-Biblioteca.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Kaishin-Library---Sistema-de-Gestao-de-Biblioteca/Kaishin Library
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa:
   ```bash
   python main.py
   ```

---

## **Estrutura do Projeto**

```plaintext
Kaishin Library/
├── arquivos.txt/
│   ├── emprestimos.txt      # Dados de empréstimos
│   ├── livros.txt           # Dados de livros cadastrados
│   └── usuarios.txt         # Dados de usuários
├── imagens/
│   ├── favicon.ico          # Ícone do programa
│   └── logo.png             # Logotipo exibido na interface
├── model/
│   ├── bibliotecario.py     # Módulo para gerenciamento de bibliotecários
│   ├── cliente.py           # Módulo para gerenciamento de clientes
│   ├── emprestimos.py       # Controle de empréstimos
│   ├── livro.py             # Manipulação de dados de livros
│   ├── telaCadastro.py      # Tela de cadastro de usuários
│   ├── telaLogin.py         # Tela de login
│   ├── telaPrincipal.py     # Tela principal da aplicação
│   └── usuario.py           # Classe abstrata para usuários
├── main.py                  # Arquivo principal para execução
├── utils.py                 # Funções utilitárias para manipulação de arquivos
└── dist/
    └── Kaishin Library.exe  # Arquivo executável do programa
```

---

## **Licença**

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## **Contato**

Para dúvidas ou sugestões, entre em contato pelo e-mail: **jonathandelmonte10@gmail.com**.

---

### **Contribuições**
Contribuições são bem-vindas! Caso tenha ideias ou melhorias, sinta-se à vontade para abrir um pull request ou relatar problemas na aba de issues.

