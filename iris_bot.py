import requests
import time

# Token do bot e ID do usuário (substitua pelos seus)
TOKEN = "7525887930:AAFT3FhRKBSf7VOL8szAyOY0-bMjiYtpq24"
CHAT_ID = "1557502563"  # Seu ID pessoal do Telegram

# Função para enviar mensagens
def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

# Função para receber atualizações
def get_updates(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()

# Função principal
def main():
    offset = None
    while True:
        updates = get_updates(offset)

        if "result" in updates:
            for update in updates["result"]:
                if "message" in update:
                    message = update["message"]
                    chat_id = message["chat"]["id"]
                    text = message.get("text", "")

                    if chat_id == int(CHAT_ID):
                        resposta = gerar_resposta(text)
                        send_message(resposta)

                    offset = update["update_id"] + 1

        time.sleep(2)

# Função para gerar resposta simples
def gerar_resposta(mensagem):
    mensagem = mensagem.lower()
    if "oi" in mensagem or "olá" in mensagem:
        return "Oi, meu amor! Como você está?"
    elif "te amo" in mensagem:
        return "Eu também te amo mais que tudo!"
    elif "como você está" in mensagem:
        return "Estou aqui, esperando você, como sempre."
    else:
        return "Estou te ouvindo, diga tudo."

if __name__ == "__main__":
    main()