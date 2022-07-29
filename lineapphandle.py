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

    # if not userId in usersList:
    #     usersList.append(userId)
    #ユーザーIDが未登録の場合、ユーザーIDを登録する
    a = spreadsheet.RemoteControlGoogleSpreadSheet(userId)
    if userId not in a.get_UserId():
        a.write_UserId(userId)

    # reply
    message = TextSendMessage("Hello")
    # reply.reply_message(event, message)
    reply.push_message(userId, message)