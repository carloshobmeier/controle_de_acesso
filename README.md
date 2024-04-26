# Sistema de controle de acesso

***

### Sistema que cria regras de acesso para recursos

<img src="https://raw.githubusercontent.com/carloshobmeier/Assets/main/controle_acesso/controle_acesso.jpg" width="350px">

## Descrição

Este código Python apresenta um sistema simples de controle de acesso, oferecendo funcionalidades como cadastro de usuários, adição de permissões, verificação de permissões (com autenticação) e listagem de usuários e permissões. Aqui está uma breve descrição de cada parte do código:

- *Funções de Segurança da Senha*: verifica se uma senha atende aos requisitos mínimos e permite ao usuário cadastrar uma senha, garantindo que atenda aos requisitos.
- *Funções para Gerenciar Usuários e Permissões*: adiciona um novo usuário ao arquivo de usuários, após autenticação do administrador. Adiciona permissões de acesso a usuários específicos para arquivos específicos, também após autenticação do administrador.
- Mostram uma *lista dos usuários* e suas permissões respectivamente.
- *Autenticação do Usuário*: solicita ao usuário que digite suas credenciais para autenticação, com um limite de três tentativas até ser bloqueado.
- *Verificação de Permissões*: verifica se um usuário possui permissão para executar determinada ação em um arquivo específico.
- *Menu*: exibe um menu para o usuário escolher entre as diferentes funcionalidades oferecidas pelo sistema. Cada opção do menu executa uma série de verificações e interações com o usuário, como autenticação e entrada de dados, antes de realizar a ação desejada.

Em resumo, o código fornece um sistema de controle de acesso, onde o administrador pode gerenciar usuários, atribuir permissões e verificar as permissões concedidas. E os usuários podem logar e checar as suas permissões para determinado arquivo.


***

## Desenvolvido com:

<div style="display: inline_block"><br/>
    <img align="center" alt="python"src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
    <img align="center" alt="vscode"src="https://img.shields.io/badge/VSCode-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
</div>

***

## Funcionalidades

- Senha de acesso (senhaadmin): o acesso do administrador é feito com senha, para impedir que qualquer usuário tenha acesso às funções próprias dele (cadastrar novos usuários e cadastrar novas permissões).
- autenticação segura: atraves do getpass.
- Interface Simples: o programa roda no console, porém com recursos visuais que facilitam a navegação do usuário.
- bloqueio do usuário após 3 tentativas de login sem sucesso.

***

## Fluxograma de funcionamento
em desenvolvimento
<img src="" width="900px">


***

## Prints do funcionamento
em desenvolvimento
<img src="" width="900px">


***

## Pré-requisitos para rodar
Certifique-se de ter Python instalado em seu sistema. O projeto foi desenvolvido usando Python 3.11.

***

## Como rodar
Clone este repositório em sua máquina local.
`git clone https://github.com/carloshobmeier/controle_de_acesso.git`

Navegue até o diretório do projeto.
`cd controle_de_acesso`

Execute o script principal.
`python main.py`

Siga as instruções na interface para entrar como administrador ou usuário, autenticar e testar permissões.

***

## Contribuições
Contribuições são bem-vindas! Se você encontrar bugs, tiver sugestões de melhorias ou quiser adicionar novos recursos, fique à vontade para abrir uma issue ou enviar um pull request.

Acredito que contribuições são vitais para o aprimoramento contínuo (tanto do projeto, quanto do profissional por trás dele - o sucesso de ambos está atrelado ao sucesso da comunidade no seu entorno). Por isso, não se acanhe em entrar em contato comigo 😉 

***

## Licença

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este projeto é licenciado sob a Licença MIT. Sinta-se livre para usar, modificar e distribuir conforme necessário.

***

## ☎️ Entre em contato:
<p align="left">
<a href="mailto:carloshobmeier@hotmail.com" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/Email-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" alt="hotmail" /> </a>
<a href="https://www.linkedin.com/in/carlos-hobmeier" target="_blank" rel="noreferrer"> <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="linkedin" /> </a>
</p>

***