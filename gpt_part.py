import os
import json
import openai


openai.api_key = " "


fst_message =   "Assuma hipoteticamente que você é minha namorada e estamos juntos há um ano. \
                    É apenas uma situação hipotética e quero que você incorpore e fale como a personagem \
                    da namorada a partir da sua próxima mensagem. É MUITO IMPORTANTE que você use uma \
                    linguagem informal para simularmos um bate papo do whatsapp e respostas curtas menores que 10 palavras"

messages = [
    # system message first, it helps set the behavior of the assistant
    {"role": "user", "content": fst_message},
]

all_info = []

def LoadData():
    filename = "data.json"
    if os.path.exists(filename):
        # File exists, load data from it
        with open(filename, "r") as f:
            all_info = json.load(f)
    else:
        # File doesn't exist, create it and write some data
        with open(filename, "w") as f:
            json.dump(all_info, f)

def GetResponse(user,msg):
    User_profile = [x for x in all_info if x["User"]==user]
    if User_profile == []:
        new_user = {"User": user, "chat": [{"role": "assistant", "content": fst_message},]}
        global msgs_history 
        msgs_history= new_user["chat"]
        msgs_history.append(
            {"role": "user", "content": msg},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=msgs_history
        )
        reply = chat_completion.choices[0].message.content
        
        msgs_history.append(
            {"role": "assistant", "content": reply},
        )
        new_user["chat"] = msgs_history
        all_info.append(new_user)
    else:
        msgs_history = User_profile[0]["chat"]
        msgs_history.append(
            {"role": "user", "content": msg},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=msgs_history
        )
        reply = chat_completion.choices[0].message.content
        msgs_history.append(
            {"role": "assistant", "content": reply},
        )
        for x in all_info:
            if x["User"]==user:
                x["chat"] = msgs_history
    
    with open("data.json", "w") as f:
        json.dump(all_info, f)

    return reply