
# WhatsApp Message Automation

Bem-vindo ao repositório **WhatsApp Message Automation**! Este projeto tem como objetivo automatizar o envio de mensagens para múltiplos contatos do WhatsApp, facilitando a comunicação em massa com eficiência e sem complicação.

Este repositório utiliza a biblioteca **[WhatsApp Web API](https://github.com/mukulhase/WebWhatsapp-Wrapper)** ou outras ferramentas relacionadas para enviar mensagens para uma lista de contatos de maneira simples e programática. Ideal para campanhas, atualizações ou automação de comunicação.

## 🚀 Descrição do Projeto

Este projeto oferece uma solução para envio automatizado de mensagens no WhatsApp a partir de uma lista de contatos. Usando a API do WhatsApp Web, o sistema permite que você envie mensagens personalizadas, por grupos ou individualmente, de maneira programada e eficiente.

Com este projeto, você pode:

-   **Enviar mensagens em massa** para vários contatos ou grupos.
-   **Automatizar o envio de mensagens** de forma programada, reduzindo o esforço manual.
-   **Personalizar a mensagem** para cada destinatário usando dados de uma lista (ex: nome, data, etc.).
-   **Monitorar os envios** e verificar se as mensagens foram entregues.

## 🛠️ Funcionalidades

-   **Envio de mensagens em massa**: Envie mensagens para uma lista de contatos em uma única execução.
-   **Personalização das mensagens**: Personalize o conteúdo das mensagens para cada contato usando placeholders (ex: `{{nome}}`).
-   **Agendamento de envio**: Defina horários específicos para o envio das mensagens.
-   **Logs de envio**: Registre o status de envio das mensagens (enviadas, não entregues, etc.).
-   **Suporte a múltiplos formatos de mensagem**: Envie mensagens de texto, imagens, documentos e mais.

## 📝 Requisitos

Antes de rodar o projeto, certifique-se de que você tem o ambiente correto configurado:

-   **Python** 3.8 ou superior
-   **Bibliotecas**:
    -   `selenium` (para automação do navegador)
    -   `pandas` (para gerenciamento de listas de contatos)
    -   `time` (para controle de delays)
    -   **[WhatsApp Web API](https://github.com/mukulhase/WebWhatsapp-Wrapper)** ou biblioteca equivalente

Instale as dependências usando `pip`:

`pip install -r requirements.txt` 

## 📁 Estrutura do Projeto

A estrutura do projeto é a seguinte:

whatsapp-message-automation/
│
├── contacts/              # Lista de contatos (pode ser CSV, JSON, etc.)
│   ├── contacts.csv       # Exemplo de arquivo com contatos
│
├── messages/              # Modelos de mensagens
│   ├── template.txt       # Template da mensagem a ser enviada
│
├── src/                   # Código-fonte do projeto
│   ├── send_message.py    # Função principal para envio das mensagens
│   ├── utils.py           # Funções auxiliares (ex: ler contatos, configurar o navegador)
│   └── ...
│
├── logs/                  # Logs de envio das mensagens
│   └── send_log.txt       # Log dos envios realizados
│
├── requirements.txt       # Dependências do Python
├── README.md              # Este arquivo
└── .gitignore             # Arquivos a serem ignorados pelo Git


## 🔧 Instruções de Uso

### 1. **Configuração Inicial**

#### 1.1. **Instalação das Dependências**

Primeiro, instale as dependências do projeto com o seguinte comando:

`pip install pywhatkit`
`pip install -r requirements.txt` 

#### 1.2. **Configuração do WebDriver**

Este projeto utiliza **Selenium WebDriver** para automação do WhatsApp Web. Certifique-se de ter o driver adequado para o navegador de sua preferência:

-   **Google Chrome**: Baixe o ChromeDriver
-   **Firefox**: [Baixe o GeckoDriver](https://github.com/mozilla/geckodriver/releases)

Após o download, extraia o arquivo e coloque o executável na mesma pasta onde o código está ou defina o caminho corretamente no código-fonte.

### 2. **Preparação dos Dados**

Você precisa de um arquivo com os contatos para quem as mensagens serão enviadas. O arquivo pode estar no formato CSV ou JSON, e deve conter pelo menos os seguintes campos:

-   **Nome**: Nome do contato (opcional, mas útil para personalizar a mensagem).
-   **Número**: Número de telefone do contato, incluindo o código do país (ex: +5511998765432).

**Exemplo de `contacts.csv`**:

    Nome,Numero
    João,+5511998765432
    Maria,+5511987654321


### 3. **Personalização da Mensagem**

O template de mensagem pode ser editado no arquivo `messages/template.txt`. Utilize placeholders como `{{nome}}` para personalizar a mensagem para cada contato.

**Exemplo de `template.txt`**:

    Olá {{nome}}, tudo bem?
    Estamos enviando essa mensagem para informá-lo sobre nossa nova promoção! Não perca a oportunidade!

### 4. **Enviando Mensagens**

Para enviar as mensagens para os contatos, basta rodar o script principal `send_message.py`.

Execute o script da seguinte maneira:

`python src/send_message.py` 

O script abrirá o WhatsApp Web, solicitará que você escaneie o QR Code e, em seguida, começará a enviar as mensagens para os contatos listados. O progresso será registrado no arquivo de log `logs/send_log.txt`.

### 5. **Agendamento de Mensagens**

Se quiser agendar o envio das mensagens para um horário específico, pode usar o Python `schedule` ou agendadores do sistema operacional como `cron` (Linux/Mac) ou o **Agendador de Tarefas** no Windows.

**Exemplo de agendamento com `schedule`**:

    import schedule

    import time

    from src.send_message import send_messages

# Agende o envio para as 9:00 AM todos os dias

    schedule.every().day.at("09:00").do(send_messages)

    while True:
        schedule.run_pending()
        time.sleep(1)

### 6. **Logs e Monitoramento**

O status de envio das mensagens será registrado no arquivo de log `logs/send_log.txt`. O log inclui informações sobre mensagens enviadas, erros e mensagens não entregues.

## 🔒 Licença

Este projeto está licenciado sob a MIT License.



