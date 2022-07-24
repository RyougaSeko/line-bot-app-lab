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

    if not userId in usersList:
        usersList.append(userId)

    # reply
    message = TextSendMessage("Hello")
    # reply.reply_message(event, message)
    reply.push_message(userId, message)