import os
import sys
# sys.path.append("/Users/hoop105ryouga/Documents/LineBot/.venv/lib/python3.9/site-packages")

#spredsheet.pyをmyspredとしてインポート

from flask import Flask, request, abort, send_file
import json
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
MessageEvent, TextMessage, LocationMessage, LocationSendMessage,TextSendMessage, StickerSendMessage, MessageImagemapAction, ImagemapArea, ImagemapSendMessage, BaseSize
)

from io import BytesIO, StringIO
#from PIL import Image
import requests
import urllib.parse
import xml.etree.ElementTree as ET

sys.path.append("spreadsheet.py")
import spreadsheet as myspred
 
app = Flask(__name__)



import sys
# sys.path.append("/Users/hoop105ryouga/Documents/LineBot/.venv/lib/python3.9/site-packages")
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# use creds to create a client to interact with the Google Drive API
scope =['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("飲食店DB").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
restaurant_info = list_of_hashes[0]
info = ""
for myvalue in restaurant_info.values():
    info += myvalue



#環境変数取得
# LINE Developersで設定されているアクセストークンとChannel Secretをを取得し、設定します。
 
line_bot_api = LineBotApi('1BDCusHAfyLU9N+yl8EB1HQC4VFSgGs2AtLMQkwcg43qdf9STwQfONWPCM40W76h74Ad003w5ddcZdVSNoNcDH7h/opvM3UfoLasHEVRn1x13PrSx9kcGVz6w2SNxa02ne0VbNwZgf8Z0LLODSIK7AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('71b252f9a0355dc60dd372de730204bf')


#王蟲返しapp

## 1 ##
#Webhookからのリクエストをチェックします。
@app.route("/callback", methods=['POST'])
def callback():
    # リクエストヘッダーから署名検証のための値を取得します。
    signature = request.headers['X-Line-Signature']
 
    # リクエストボディを取得します。
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    # handle webhook body
# 署名を検証し、問題なければhandleに定義されている関数を呼び出す。
    try:
        #revert_json_py(body)
        handler.handle(body, signature)
# 署名検証で失敗した場合、例外を出す。
    except InvalidSignatureError:
        abort(400)
# handleの処理を終えればOK
    return 'OK'
 
## 2 ##
###############################################
#LINEのメッセージの取得と返信内容の設定(オウム返し)
###############################################
 
#LINEでMessageEvent（普通のメッセージを送信された場合）が起こった場合に、
#def以下の関数を実行します。
#reply_messageの第一引数のevent.reply_tokenは、イベントの応答に用いるトークンです。 
#第二引数には、linebot.modelsに定義されている返信用のTextSendMessageオブジェクトを渡しています。
 
 #メッセージを受け取った時にする処理
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text="Hi")) #ここでオウム返しのメッセージを返します。
 
@handler.add(MessageEvent, message=LocationMessage)
def handle_message(event):
#   geo_info = f"{event.message.latitude} {event.message.longitude}"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(info))#ここでメッセージを返します。
# def revert_json_py(s):
#     d = json.loads(request.json)

# #タプルを取得
# def func1(myspred):
#     list1 = []
#     list2 = []
#     list3 = []
#     for a, b in myspred:
#         list1.append(a)
#         list2.append(b)
#     return list1, list2

# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)