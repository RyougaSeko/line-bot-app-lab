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


#ここに、webhookイベントが発生した時の処理を書く
def TextMessage(event):
    userId = event.source.user_id
    message = event.message.text

    #ユーザーIDがない場合、登録する
    UpdateUserId(userId)

    #pushするメッセージを取ってくる。
    #EngBot_Sheet1から、キー「english」をランダムに送信
    eng_phrases_record = EngBot_Sheet.get_all_records()
    eng_phrases_li = []
    #eng_phrases_recordの中身を取り出す。
    for eng_phrase in eng_phrases_record:
        #eng_phrase = {'english': 'waeomclke'}
        eng_phrases_li.append(eng_phrase['english'])

    message = TextSendMessage(random.choice(eng_phrases_li))

    # reply.reply_message(event, message)
    reply.push_message(userId, message)

def FollowEvent(event):

    #event.source.user_idはuser_id
    profile = line_bot_api.get_profile(event.source.user_id)
    UpdateUserId(profile.user_id)

    #友達追加したユーザにメッセージを送信
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="友達追加ありがとうございます\n")
    )
