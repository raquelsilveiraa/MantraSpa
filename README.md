# Mantra SPA - Sistema de Gerenciamento

## Descrição

Este é um protótipo de um sistema de gerenciamento para o Mantra SPA. Ele permite gerenciar serviços, funcionários, vendas, agendamentos, promoções e avaliações. O sistema foi desenvolvido utilizando Python e Tkinter para a interface gráfica, e SQLite para o banco de dados.

## Requisitos

- Python 3.12 ou superior

## Instalação

1. Clone o repositório para o seu computador:

    ```sh
    git clone https://github.com/raquelsilveiraa/MantraSpa.git
    ```

2. Navegue até o diretório do projeto:

    ```sh
    cd MantraSpa
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```sh
    python -m venv venv
    source venv/bin/activate  # Para Linux e macOS
    venv\Scripts\activate  # Para Windows
    ```

4. Instale as dependências do projeto:

   - Para esse projeto não será necessário, foi usado tudo disponivel no: 
       - Python 3.12 ou superior

## Uso

1. Inicie o aplicativo:

    ```sh
    python main.py
    ```

2. Faça login com as credenciais:

    - **Usuário:** admin
    - **Senha:** 123456

## Estrutura do Projeto

- `main.py`: Script principal para iniciar o aplicativo.
- `gerenciador_app.py`: Classe principal que gerencia a aplicação e navegação entre os menus.
- `gerenciadorservicos.py`: Classe para gerenciar serviços.
- `gerenciadorfuncionario.py`: Classe para gerenciar funcionários.
- `gerenciadorvendas.py`: Classe para gerenciar vendas.
- `gerenciadoragendamentos.py`: Classe para gerenciar agendamentos.
- `gerenciadorpromocoes.py`: Classe para gerenciar promoções.
- `gerenciadoravaliacoes.py`: Classe para gerenciar avaliações.
- `Servico.py`: Modelo para serviços.
- `Funcionario.py`: Modelo para funcionários.
- `Vendas.py`: Modelo para vendas.
- `Agenda.py`: Modelo para agendamentos.
- `database.py`: Classe para gerenciar a conexão e estrutura do banco de dados SQLite.

## Banco de Dados

O projeto utiliza SQLite como banco de dados. O arquivo do banco de dados (`mantra_spa.db`) será criado automaticamente na primeira execução do aplicativo, e as tabelas necessárias serão configuradas.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o projeto.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
