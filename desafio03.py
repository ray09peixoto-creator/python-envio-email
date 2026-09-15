import requests
import csv
from email.message import EmailMessage
import smtplib
import os

# ==========================================
# 1. ACESSAR A API
# ==========================================

url = "https://reqres.in/api/users"


def buscar_usuarios():
 try:

    resposta = requests.get(url)

    # Verifica se a API respondeu com erro
    resposta.raise_for_status()

    # Transforma o JSON em Python
    dados = resposta.json()

 except requests.RequestException:
    print("Erro ao acessar a API")
 return dados['data']

usuarios = buscar_usuarios()


#==========================================
# 2. CRIAR O ARQUIVO CSV
# =========================================

def criar_csv(usuarios):
 campos = ['id',
    'email',
    'first_name',
    'last_name',
    'avatar']

 with open('usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
    # Cria o escritor de dicionários
    writer = csv.DictWriter(
        arquivo,
        fieldnames=campos
    )

    # Escreve os nomes das colunas
    writer.writeheader()

    # Escreve os usuários
    writer.writerows(usuarios)

criar_csv(usuarios)


# ==========================================
# 3. TESTAR OS USUÁRIOS
# ==========================================

for usuario in usuarios:

    print(usuario['first_name'])
    print(usuario['email'])


# ==========================================
# 4. CRIAÇÃO DO E-MAIL
# ==========================================
def enviar_email():
   mensagem = EmailMessage()
   mensagem['From'] = "2026.rayssa.costa@teslando.org.br"
   mensagem["To"] = "ray09peixoto@gmail.com"
   mensagem['Subject'] = "Lista-de-Usuarios"
   mensagem.set_content('Segue anexo com lista de usuários')
   servidor = smtplib.SMTP('smtp.gmail.com', 587)
   servidor.starttls()
   senha = os.getenv('SENHA_EMAIL')
   servidor.login('2026.rayssa.costa@teslando.org.br', senha)
   

   with open('usuarios.csv', 'rb') as arquivo:
      dados_arquivo = arquivo.read()
   mensagem.add_attachment(
      dados_arquivo,
      maintype ='text',
      subtype = 'csv',
      filename ='usuarios.csv'
   )
   servidor.send_message(mensagem)
   servidor.quit()
enviar_email()
