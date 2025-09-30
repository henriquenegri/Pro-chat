# 🧠✨ NeuroChat: Desvendando Universos, Conectando Pessoas ✨🧠

[![Licença: MIT](https://img.shields.io/badge/Licença-MIT-9942A8?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Status: Em Desenvolvimento](https://img.shields.io/badge/STATUS-EM%20DESENVOLVIMENTO-GREEN?style=for-the-badge)](https://github.com/henriquenegri/Pro-chat)
[![Contribuições: Bem-vindas!](https://img.shields.io/badge/CONTRIBUIÇÕES-BEM--VINDAS-ORANGE?style=for-the-badge)](https://github.com/henriquenegri/Pro-chat/blob/main/CONTRIBUTING.md)

<p align="center">
  <em>"A diversidade de cérebros não é um bug, é uma feature. Nossa missão é criar o manual de instruções."</em>
</p>

## 🚀 O que é o NeuroChat?

O **NeuroChat** é mais do que um script. Ele é um assistente virtual, rodando diretamente no seu terminal, projetado para ser um ponto de partida seguro e acolhedor para quem busca entender e apoiar a comunidade neurodivergente.

Utilizando o poder do Google Gemini, este projeto oferece respostas claras e diretas para questões sobre autismo, TDAH, dislexia e outras condições, com o objetivo de centralizar informações confiáveis, oferecer apoio prático e direcionar para ajuda qualificada.

### 🎯 Nossos Pilares:

* **INFORMAR:** Traduzir a complexidade da neurodiversidade em uma linguagem clara e humana.
* **APOIAR:** Fornecer dicas práticas e acionáveis sobre como ajudar e criar ambientes mais acolhedores.
* **DIRECIONAR:** Ajudar a localizar o profissional certo para cada situação.

## ✨ Funcionalidades

* 💬 **Interface de Linha de Comando:** Uma interação direta e sem distrações, direto no seu terminal.
* 🧠 **Inteligência Artificial de Ponta:** Respostas geradas pelo modelo `gemini-1.0-pro` do Google.
* 📚 **Base de Conhecimento Abrangente:** Acesso a uma vasta gama de informações para tirar dúvidas complexas.
* 💖 **Configuração de Segurança Aberta:** Projetado para discutir tópicos sensíveis sem bloqueios desnecessários (para fins de informação e apoio).

## 🛠️ Stack Tecnológica (O que tem sob o capô)

Este projeto é construído com uma abordagem minimalista e poderosa:

* **Linguagem:** `Python`
* **Inteligência Artificial:** `Google Gemini Pro`
* **Biblioteca Principal:** `google-generativeai`

## 🏃‍♂️ Guia de Início Rápido (Getting Started)

Pronto para rodar o projeto na sua máquina? Siga os passos abaixo!

### Pré-requisitos

* **Python 3.8+** instalado na sua máquina.
* **pip** (gerenciador de pacotes do Python).
* Uma chave de API do **Google AI Studio**. Você pode obter a sua gratuitamente [aqui](https://aistudio.google.com/app/apikey).

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/henriquenegri/Pro-chat.git](https://github.com/henriquenegri/Pro-chat.git)
    ```

2.  **Navegue até o diretório:**
    ```bash
    cd Pro-chat
    ```

3.  **Instale as dependências:**
    * Primeiro, crie um arquivo chamado `requirements.txt` na raiz do projeto.
    * Dentro dele, adicione a seguinte linha:
        ```
        google-generativeai
        ```
    * Agora, instale a biblioteca com o pip:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Configure sua API Key:**
    * Abra o arquivo de script Python (ex: `main.py`).
    * Encontre a linha:
        ```python
        GOOGLE_API_KEY = "(Sua API)"
        ```
    * Substitua `(Sua API)` pela sua chave de API do Google que você gerou.

## 🚀 Como Usar

Com tudo configurado, basta executar o script no seu terminal!

1.  **Execute o arquivo Python:**
    ```bash
    python seu_script.py 
    # (substitua 'seu_script.py' pelo nome real do seu arquivo)
    ```

2.  **Interaja com o Chat:**
    O programa primeiro pedirá seu nome e sua dúvida inicial. Depois, entrará em um loop onde você pode conversar livremente.

    **Exemplo de interação no terminal:**

    ```text
    Bem-vindo à Pró-chat! Somos uma plataforma de chat dedicada a ajudar a entender o mundo neural.
    Pró-chat é uma plataforma de chat que utiliza inteligência artificial para responder perguntas e fornecer suporte personalizado para qualquer um.
    Entre em contato conosco para mais informações ou suporte: proservechat@gmail.com

    Olá! Qual é o seu nome?
    > Henrique
    Qual é a dúvida que você veio tirar?
    > Dislexia

    Entendido, Henrique. Estamos aqui para ajudá-lo(a) com sua dúvida sobre 'Dislexia'.

    Aguardando pergunta: Como posso ajudar meu filho com as tarefas da escola?
    Resposta:  Existem várias estratégias! Tente usar audiobooks para acompanhar a leitura, utilize softwares de texto para fala, e divida grandes tarefas em passos menores e mais gerenciáveis. O reforço positivo é sempre muito importante.

    Aguardando pergunta: fim
    ```

3.  Para encerrar a conversa, simplesmente digite `fim` e pressione Enter.

## 🤝 Quer Contribuir?

Este é um projeto de código aberto e de coração aberto. Toda ajuda é bem-vinda! Sinta-se à vontade para abrir uma `Issue` para relatar bugs ou sugerir melhorias, ou fazer um `Fork` e enviar um `Pull Request`.

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Feito com ❤️, muito código e empatia por <strong>henriquenegri</strong>.
</p>
