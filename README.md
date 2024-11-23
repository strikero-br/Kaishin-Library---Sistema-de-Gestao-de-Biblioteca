<p align="right">
  <a href="https://github.com/strikero-br/Kaishin-Library-Sistema-de-Gestao-de-Biblioteca">
    <img src="https://img.icons8.com/win10/200/228BE6/github.png" alt="GitHub" width="90" height="90">
  </a>
  <a href="https://kaishinlibrary.my.canva.site/">
    <img src="https://cdn.discordapp.com/attachments/1308085240350249081/1308090738373955584/pixelcut-export.png?ex=6743456f&is=6741f3ef&hm=b6ca41284d76e8e3fc99a07958e374cfa080bef2fb9fe1ecdd367b34296536c5&" alt="Kaishin Library" width="75" height="75">
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

## 🌐 **Apresentação do Projeto**
### 👉 [Acesse a apresentação oficial do projeto: Kaishin Library](https://kaishinlibrary.my.canva.site/)

> Conheça mais sobre o projeto, seu funcionamento e o impacto no gerenciamento de bibliotecas.

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
   git clone https://github.com/strikero-br/Kaishin-Library-Sistema-de-Gestao-de-Biblioteca.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd Kaishin-Library-Sistema-de-Gestao-de-Biblioteca/Kaishin Library
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
├── requirements.txt         # Dependências do projeto
└── dist/
    └── Kaishin Library.exe  # Arquivo executável do programa
```

---

## **Nota para Desenvolvedores**

Se você está tendo dificuldades com a instalação do repositório ou deseja uma alternativa, disponibilizamos uma pasta no Google Drive com os seguintes recursos:

- **Arquivo ZIP com o Projeto Completo**: Inclui todo o código-fonte do projeto, organizado e pronto para ser extraído.
- **Setup Instalador do Programa**: Contém o instalador do programa, permitindo a instalação e execução do programa diretamente, sem a necessidade de clonar o repositório ou configurar o ambiente Python.

### 📂 **Acesse a Pasta no Google Drive**: [Kaishin Library - Recursos para Desenvolvedores](https://drive.google.com/drive/folders/19r-Hj3NrSVdm5Nbn87oS-BwpLNeV9f7z?usp=drive_link)


### 📌 **↴**

**Além de executar o código diretamente, o projeto inclui um arquivo executável disponível na pasta `dist/Kaishin Library.exe` dentro do repositório, caso você já tenha clonado o projeto. Esse arquivo permite a execução do programa sem a necessidade de configurar o ambiente Python.**


--- 


## **Licença**

Este projeto está licenciado sob a licença **MIT**. Consulte o arquivo `LICENSE` para mais detalhes.

---

## **Contato**

Para dúvidas ou sugestões, entre em contato pelo e-mail: **kaishinlibrary@gmail.com**.

---

### **Contribuições**
Contribuições são bem-vindas! Caso tenha ideias ou melhorias, sinta-se à vontade para abrir um pull request, relatar problemas na aba de issues ou abrir uma discussão no repositório.
