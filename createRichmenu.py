from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, RichMenu, RichMenuSize, RichMenuArea, 
    RichMenuBounds, MessageAction, URIAction
)

from config import line_bot_api

from lineapphandle import GenerateMessage

def createRichmenu():
    result = False
    try:
        # define a new richmenu
        rich_menu_to_create = RichMenu(
            size = RichMenuSize(width=1200, height=405),
            selected = True,
            name = 'richmenu for randomchat',
            chat_bar_text = 'TAP HERE',
            areas=[
                RichMenuArea(
                    bounds=RichMenuBounds(x=0, y=0, width=1200, height=405),
                    action=URIAction(label='Go to line.me', uri='https://line.me')
                    # action=MessageAction(text=GenerateMessage())
                    # action=MessageAction(label = 'hello', text = 'hello')
                )
            ]
        )
        richMenuId = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

        # upload an image for rich menu
        path = 'Learnwords.png'

        #ファイル読み込み
        with open(path, 'rb') as f:
            line_bot_api.set_rich_menu_image(richMenuId, "image/jpeg", f)

        # set the default rich menu
        line_bot_api.set_default_rich_menu(richMenuId)

        result = True

    except Exception:
        result = False


    return result