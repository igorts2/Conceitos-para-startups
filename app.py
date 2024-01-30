from senha import API_KEY
import requests
import json


# Dicionario para autentificação da API "https://platform.openai.com/docs/api-reference/authentication"
# Define um dicionário chamado headers que será usado para autenticação na API do OpenAI. 
headers = {"Authorization": f"Bearer {API_KEY}", "content-Type": "application/json"}

# Define a URL da API do OpenAI e o identificador do modelo, que é "gpt-3.5-turbo".
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

# inputs para informações do usuario.
nome = input('Digite seu nome: ')
print(f"olá, {nome}.\nVou te auxiliar para ter algumas ideias de startups. ")
experiencia = input("Quais as suas experiencias ou habilidades? ")
investimento = int(input("qual seria o valor que você poderia investir?"))

#Cria um corpo de mensagem em formato JSON para enviar à API do OpenAI
body_mensagem = {
    "model": id_modelo,
    "messages": [{"role": "user", "content": f"""Meu nome é: {nome} e minhas experiencias são:
                   {experiencia}. tenho o valor de {investimento}. Poderia me fornecer ideias de startup. """}]
}
body_mensagem = json.dumps(body_mensagem)

requisicao = requests.post(link, headers=headers, data=body_mensagem)
#print(requisicao)

resposta= requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)

