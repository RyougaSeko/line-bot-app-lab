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
import config
#import linepphandl


YOUR_CHANNEL_SECRET = config.YOUR_CHANNEL_SECRET
YOUR_CHANNEL_ACCESS_TOKEN = config.YOUR_CHANNEL_ACCESS_TOKEN

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)


def reply_message(event, message):
    line_bot_api.reply_message(
        event.reply_token,
        message
    )

def push_message(toUserId, message):
    line_bot_api.push_message(
        toUserId,
        message
    )