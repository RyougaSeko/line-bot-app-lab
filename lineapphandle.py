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
from spreadsheet import sheet

YOUR_CHANNEL_SECRET = config.YOUR_CHANNEL_SECRET
YOUR_CHANNEL_ACCESS_TOKEN = config.YOUR_CHANNEL_ACCESS_TOKEN

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

usersList = []
usersDic = {}

#ここに、webhookイベントが発生した時の処理を書く
def TextMessage(event):
    userId = event.source.user_id
    message = event.message.text

    #spreadsheetからuser_idのデータベースを取得。
    #[{'user_id': 'waeomclke'}, {'user_id': 'cmwelm'}]のリスト形式でuser_idを取得
    use_ids_record = sheet.get_all_records()
    #user_idが登録済みではない場合、スプレッドシートに登録する。
    user_id_li = []
    for user_id in use_ids_record:
        #user_id = {'user_id': 'waeomclke'}
        user_id_li.append(user_id['user_id'])

    if userId not in user_id_li:
        row_count = 1
        while sheet.cell(row_count, 1).value != None:
            row_count += 1
            sheet.update_cell(row_count, 1, userId)
    # reply
    message = TextSendMessage("Hello")
    # reply.reply_message(event, message)
    reply.push_message(userId, message)