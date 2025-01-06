
# WhatsApp Automation Messages

Bem-vindo ao repositório **WhatsApp Automation Messages**! Este projeto permite o envio de mensagens automatizadas via WhatsApp para uma lista de funcionários cadastrados, com validação de números e uma interface simples para selecionar os destinatários.

Este script utiliza a biblioteca **pywhatkit** para enviar mensagens instantâneas via WhatsApp Web, tornando o processo de comunicação mais eficiente e sem complicações.

## 🚀 Descrição do Projeto

Este projeto foi desenvolvido para enviar mensagens de texto automaticamente para uma lista de contatos cadastrados (funcionários) no WhatsApp. Através de uma interface interativa, o usuário pode escolher os destinatários e enviar uma mensagem personalizada para vários contatos simultaneamente.

-   **Envia mensagens para contatos cadastrados**.
-   **Valida o número de telefone** para garantir que o formato esteja correto.
-   **Permite escolher múltiplos destinatários** e enviar mensagens para eles simultaneamente.
-   **Usa a biblioteca `pywhatkit`** para enviar mensagens instantâneas via WhatsApp Web.

## 🛠️ Funcionalidades

-   **Cadastro de Funcionários**: Adicione funcionários e seus números de WhatsApp ao dicionário `funcionarios`.
-   **Validação de Números**: Verifique se os números de telefone seguem o formato correto para envio pelo WhatsApp.
-   **Envio de Mensagens**: Envie mensagens para um ou mais funcionários selecionados, diretamente via WhatsApp Web.
-   **Suporte a múltiplos destinatários**: Selecione vários contatos para enviar a mesma mensagem.
-   **Exibição de Logs**: Acompanhe o sucesso ou falha de cada envio de mensagem.

## 📝 Requisitos

Certifique-se de ter os seguintes requisitos instalados antes de rodar o projeto:

-   **Python** 3.8 ou superior
-   **Bibliotecas**:
    -   `pywhatkit` (para automação do WhatsApp)
    -   `datetime` (para manipulação de datas e horas)
    -   `time` (para gerenciamento de pausas)

Instale as dependências usando `pip`:

`pip install pywhatkit` 

## 📁 Estrutura do Projeto

A estrutura do projeto é simples:

whatsapp-automation-messages/
│
├── main.py            # Arquivo principal com a lógica de envio de mensagens
│
├── DB.txt       # Dependências do Python
|
├── README.md              # Este arquivo
|
└── .gitignore             # Arquivo para ignorar arquivos do Git


## 🔧 Instruções de Uso

### 1. **Instalar as Dependências**

Primeiro, instale a biblioteca `pywhatkit` que é utilizada para enviar mensagens via WhatsApp Web:

`pip install pywhatkit` 

### 2. **Adicionar Funcionários**

No arquivo `main.py`, adicione os funcionários e seus números no formato internacional (incluindo o código do país) ao dicionário `funcionarios`:

```py
funcionarios = {
    "João": "+55 11 91234-5678",
    "Maria": "+55 21 98765-4321"
}
```

### 3. **Rodando o Script**

Para rodar o script, basta executar o arquivo `main.py`:

`python src/main.py` 

### 4. **Interação no Console**

Ao rodar o script, será solicitado ao usuário que:

1.  Digite a mensagem que será enviada.
2.  Escolha os funcionários (através de números correspondentes, separados por vírgula) para quem deseja enviar a mensagem.

Por exemplo, a saída será algo assim:

```
Funcionários disponíveis para receber a mensagem:
1. João - +55 11 91234-5678
2. Maria - +55 21 98765-4321

Digite os números correspondentes aos funcionários (separados por vírgula):
```

Após escolher os funcionários, o script enviará a mensagem para os selecionados. A cada envio, o script aguardará 2 segundos antes de continuar o próximo envio.

### 5. **Validação de Números**

O script valida se os números de telefone estão no formato correto para serem utilizados pelo WhatsApp Web. Caso algum número esteja incorreto, o script exibirá um erro e não tentará enviar a mensagem para aquele contato.

### 6. **Pauses entre Envio**

O script irá fazer uma pausa de 2 segundos entre o envio de mensagens para não sobrecarregar o processo de automação e garantir a eficiência.

## 🔒 Licença

Este projeto está licenciado sob a MIT License.
