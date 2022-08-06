# from linebot import (
#     LineBotApi, WebhookHandler
# )

# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage, RichMenu, RichMenuSize, RichMenuArea, 
#     RichMenuBounds, MessageAction, URIAction
# )

# from lineapphandle import GenerateMessage
# line_bot_api = LineBotApi('1BDCusHAfyLU9N+yl8EB1HQC4VFSgGs2AtLMQkwcg43qdf9STwQfONWPCM40W76h74Ad003w5ddcZdVSNoNcDH7h/opvM3UfoLasHEVRn1x13PrSx9kcGVz6w2SNxa02ne0VbNwZgf8Z0LLODSIK7AdB04t89/1O/w1cDnyilFU=')


# def createRichmenu():
#     result = False
#     try:
#         # define a new richmenu
#         rich_menu_to_create = RichMenu(
#             size = RichMenuSize(width=1200, height=405),
#             selected = True,
#             name = 'richmenu for randomchat',
#             chat_bar_text = 'TAP HERE',
#             areas=[
                
#                 RichMenuArea(
#                     #1200x405を2分割
#                     bounds=RichMenuBounds(x=0, y=0, width=600, height=405),
#                     action=MessageAction(label = 'hello', text = 'わからない')
#                 ),
#                 RichMenuArea(
#                     bounds=RichMenuBounds(x=600, y=0, width=600, height=405),
#                     action=MessageAction(label = 'hello', text = 'わかる')
#                 )
                
#             ]
#         )
#         richMenuId = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)

#         # upload an image for rich menu
#         path = '../pic/know-or-dont.png'

#         #ファイル読み込み
#         with open(path, 'rb') as f:
#             line_bot_api.set_rich_menu_image(richMenuId, "image/jpeg", f)

#         # set the default rich menu
#         line_bot_api.set_default_rich_menu(richMenuId)

#         result = True

#     except Exception:
#         result = False


#     return result