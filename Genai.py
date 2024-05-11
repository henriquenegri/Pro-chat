import google.generativeai as genai

class ProChat:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def welcome_message(self):
        return f"Bem-vindo à {self.name}! Somos uma plataforma de chat dedicada a ajudar a entender o mundo neural.\n"

    def about(self):
        return f"{self.name} é uma plataforma de chat que utiliza inteligência artificial para responder perguntas e fornecer suporte personalizado para qualquer um.\n"

    def contact_us(self):
        return "Entre em contato conosco para mais informações ou suporte: proservechat@gmail.com\n"

# Criando uma instância da empresa Pró-chat
pro_chat = ProChat("Pró-chat", "Plataforma de chat para ajudar a entender as dificuldades e como podemos ajudar as pessoas com baixo desenvolvimento neural.\n")

# Imprimindo mensagem de boas-vindas e informações sobre a empresa
print(pro_chat.welcome_message())
print(pro_chat.about())
print(pro_chat.contact_us())

# Solicitando o nome do usuário e a dúvida que o usuário veio tirar apenas na primeira vez
user_name = input("Olá! Qual é o seu nome?\n")
reason = input("Qual é a dúvida que você veio tirar?\n")
print(f"\nEntendido, {user_name}. Estamos aqui para ajudá-lo(a) com sua dúvida sobre '{reason}'.\n")

# Substitua com a sua chave de API
GOOGLE_API_KEY = "(Sua API)"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count": 1,
    "temperature": 0.5,
}
safety_settings = {
    "Harassment": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}
model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config,
                             safety_settings=safety_settings)

chat = model.start_chat(history=[f"Olá, {user_name}! Como posso te ajudar hoje com sua dúvida sobre '{reason}'?"])


chat = model.start_chat(history=[])
prompt = input("Aguardando pergunta: ")
while prompt != "fim":
    response = chat.send_message(prompt)
    print("Resposta: ", response.text, "\n")
    prompt = input("Aguardando pergunta: ")

    # Formatando a saída para o terminal
    for i, message in enumerate(chat.history):
        if i % 2 == 0:  # Mensagens do usuário
            print(f"> {message.parts[0].text}")
        else:  # Respostas do modelo
            print(f"{message.parts[0].text}\n")

    print('-------------------------------------------')
