from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import config, reply
import random, copy
import spreadsheet
from spreadsheet import use_id_sheet, EngBot_Sheet
import random

YOUR_CHANNEL_SECRET = config.YOUR_CHANNEL_SECRET
YOUR_CHANNEL_ACCESS_TOKEN = config.YOUR_CHANNEL_ACCESS_TOKEN

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

usersList = []
usersDic = {}
jpn_phrase = ''
eng_phrase = ''

def UpdateUserId(userId):
    #spreadsheetからuser_idのデータベースを取得。
    #[{'user_id': 'waeomclke'}, {'user_id': 'cmwelm'}]のリスト形式でuser_idを取得
    use_ids_record = use_id_sheet.get_all_records()
    #user_idが登録済みではない場合、スプレッドシートに登録する。
    user_id_li = []
    for user_id in use_ids_record:
        #user_id = {'user_id': 'waeomclke'}
        user_id_li.append(user_id['user_id'])

    if userId not in user_id_li:
        row_count = 1
        while use_id_sheet.cell(row_count, 1).value != None:
            row_count += 1
        use_id_sheet.update_cell(row_count, 1, userId)

def GenerateMessage():

    #pushするメッセージを取ってくる。
    #EngBot_Sheet1から、キー「english」をランダムに送信
    jpn_phrases_record = EngBot_Sheet.get_all_records()
    #リストの中に辞書が入っている。
    # [{'id': 1, 'japanese': '将来は弁護士になる予定だ', 'english': "I'm going to become a layer in the future.", 'メモ': ''},
    
    #ランダムに辞書を取り出す
    random_dic = random.choice(jpn_phrases_record)
    #ex random_dic = {'id': 1, 'japanese': '将来は弁護士になる予定だ', 'english': "I'm going to become a layer in the future.", 'メモ': ''}

    jpn_phrase = random_dic['japanese']
    eng_phrase = random_dic['english']

    return jpn_phrase, eng_phrase

#ここに、webhookイベントが発生した時の処理を書く
def TextMessage(event):
    global eng_phrase
    global jpn_phrase

    userId = event.source.user_id
    message = event.message.text

    #ユーザーIDがない場合、登録する
    UpdateUserId(userId)
    #GenerateMessageで、jpn_phrase, eng_phraseを返す 

    # # reply.reply_message(event, message)
    # reply.push_message(userId, message)
    if message == 'わかる':
        return_eng_message = TextSendMessage(eng_phrase)
        reply.push_message(userId, return_eng_message)
    elif message == 'わからない':
        return_eng_message = TextSendMessage(eng_phrase)
        reply.push_message(userId, return_eng_message)
    else:
        #返す日本語のメッセージを作成
        return_message = GenerateMessage()
        return_jpn_message = TextSendMessage(return_message[0])
        reply.push_message(userId, return_jpn_message)

        #global変数jpn_phraseと, eng_phraseにメッセージの内容を格納
        jpn_phrase = return_message[0]
        eng_phrase = return_message[1]
        




def FollowEvent(event):

    #event.source.user_idはuser_id
    profile = line_bot_api.get_profile(event.source.user_id)
    UpdateUserId(profile.user_id)

    #友達追加したユーザにメッセージを送信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="友達追加ありがとうございます😃 毎日英語を少しずつ学んでいきましょう😆")
    )
