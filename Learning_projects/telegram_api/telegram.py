import requests
import os

TOKEN = 'TOKEN_ID'
CHAT_ID = 'CHAT_ID'
CURRENT_PATH = os.path.dirname(__file__)
IMAGE_PATH = os.path.join(CURRENT_PATH, 'test.jpg')
print(CURRENT_PATH)

def send_message(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + TOKEN + '/sendMessage?chat_id=' + CHAT_ID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def send_photo(image_path):
    try:
        files={'photo':open(image_path,'rb')}
        requests.post('https://api.telegram.org/bot'+TOKEN+'/sendPhoto?chat_id='+CHAT_ID, files=files)
    except Exception as e:
        print(e)

def send_document(document_path):
    try:
        files={'document':open(document_path,'rb')}
        requests.post('https://api.telegram.org/bot'+TOKEN+'/sendDocument?chat_id='+CHAT_ID, files=files)
    except Exception as e:
        print(e)

send_message("This is a testing message!! 😋")

send_photo(IMAGE_PATH)