# Script de Geração de Ideias de Startups usando a API GPT-3.5-turbo da OpenAI.

## Este script utiliza a API do OpenAI para gerar ideias de startups com base nas informações fornecidas pelo usuário.

### Requisitos:
  Python 3.x
  Biblioteca requests (instalável via 'pip install requests')
  Biblioteca da openAI (pip install openai)

### Como usar:
  1. Obtenha uma chave de API da OpenAI em https://platform.openai.com/signup.
  2. Substitua a variável API_KEY abaixo com a sua chave de API.
  3. Coloque sua autentificação na variavel "headers" https://platform.openai.com/docs/api-reference/authentication
  4. Coloque sua API na variavel API_KEY no arquivo "senha"


Inputs do Usuário:
    - O script solicitará as seguintes informações ao usuário:
    - Nome: Seu nome para personalizar a interação.
    - Experiências: Suas habilidades ou experiências relevantes.
    - Investimento: O valor que você está disposto a investir em uma startup.

Saída:
    - O script envia uma requisição à API do OpenAI e recebe uma resposta com ideias de startups geradas pelo modelo GPT-3.5-turbo.
    - A resposta é exibida no terminal.
