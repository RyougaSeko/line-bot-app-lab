from linebot import (
    LineBotApi, WebhookHandler
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, RichMenu, RichMenuSize, RichMenuArea, 
    RichMenuBounds, MessageAction, URIAction
)

from lineapphandle import GenerateMessage
line_bot_api = LineBotApi('1BDCusHAfyLU9N+yl8EB1HQC4VFSgGs2AtLMQkwcg43qdf9STwQfONWPCM40W76h74Ad003w5ddcZdVSNoNcDH7h/opvM3UfoLasHEVRn1x13PrSx9kcGVz6w2SNxa02ne0VbNwZgf8Z0LLODSIK7AdB04t89/1O/w1cDnyilFU=')

# 全てのリッチメニューを削除する
def delete_richmenu(line_bot_api):
    print("delete user richmenu")
    menu_list = line_bot_api.get_rich_menu_list()

    for richmenu in menu_list:
        print("delete user richmenu "+richmenu.rich_menu_id)
        line_bot_api.delete_rich_menu(richmenu.rich_menu_id)

def createRichmenu():
    result = False

    try:
        #既存リッチメニューをキャンセル
        line_bot_api.cancel_default_rich_menu()
        #既存のリッチメニューを削除
        delete_richmenu(line_bot_api)

        # define a new richmenu
        rich_menu_to_create = RichMenu(
            size = RichMenuSize(width=1200, height=405),
            selected = True,
            name = 'richmenu for randomchat',
            chat_bar_text = 'TAP',
            areas=[
                
                RichMenuArea(
                    #1200x405を2分割
                    bounds=RichMenuBounds(x=0, y=0, width=400, height=405),
                    action=MessageAction(label = 'next', text = 'Next')
                )
                ,
                RichMenuArea(
                    bounds=RichMenuBounds(x=400, y=0, width=400, height=405),
                    action=MessageAction(label = 'わかる', text = 'わかる')
                ),
                RichMenuArea(
                    #1200x405を2分割
                    bounds=RichMenuBounds(x=800, y=0, width=400, height=405),
                    action=MessageAction(label = 'わからない', text = 'わからない')
                )
                
            ]
        )
        richMenuId = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
        print(richMenuId)


        # upload an image for rich menu
        path = 'pic/richmenu_3.png'

        #ファイル読み込み
        with open(path, 'rb') as f:
            line_bot_api.set_rich_menu_image(richMenuId, "image/png", f)
        
            # set the default rich menu
            line_bot_api.set_default_rich_menu(richMenuId)
        result = True

    except Exception:
        result = False
        import traceback
        traceback.print_exc()

    return result

delete_richmenu(line_bot_api)
createRichmenu()