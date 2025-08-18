from fastapi import FastAPI, Request, HTTPException, Header
from linebot import LineBotApi
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent, ImageMessageContent, LocationMessageContent
from linebot.v3.messaging import (ApiClient,MessagingApi,Configuration,ReplyMessageRequest,TextMessage,FlexMessage,MessagingApiBlob,
                                  ImageMessage,RichMenuRequest, RichMenuArea, RichMenuSize,RichMenuBounds, URIAction, MessageAction)
from fastapi.staticfiles import StaticFiles
from linebot.v3.messaging.models import FlexContainer
import os
from dotenv import load_dotenv
import uvicorn
from Flex import show_pred, not_pomelo
from FruitClass import FruitClassify
import requests
import json

app = FastAPI()
load_dotenv(override=True)

# LINE keys
get_access_token = os.getenv('ACCESS_TOKEN')
get_channel_secret = os.getenv('CHANNEL_SECRET')

configuration = Configuration(access_token=get_access_token)
handler = WebhookHandler(channel_secret=get_channel_secret)

#กำหนด end point ของ webhook
@app.post("/callback")
async def callback(request: Request, x_line_signature: str = Header(None)):
    body = await request.body()
    body_str = body.decode('utf-8')
    try:
        handler.handle(body_str, x_line_signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature.")
    return 'OK'


#API ชั่วคราวไว้ส่งรูปกลับไปให้ user
app.mount("/img", StaticFiles(directory="img"), name="img")
app.mount("/thongdee", StaticFiles(directory="thongdee"), name="thongdee")

# @handler.add(MessageEvent, message=TextMessageContent)
# def handle_message(event: MessageEvent):
#     with ApiClient(configuration) as api_client:
#         line_bot_api = MessagingApi(api_client)

#     user_id = event.source.user_id
#     print(f"User ID: {user_id}")  # หรือส่งกลับให้ user เห็น
#     line_bot_api.reply_message(
#         ReplyMessageRequest(
#             reply_token=event.reply_token,
#             messages=[TextMessage(text=f"Your user ID is: {user_id}")]
#         )
#     )
def loading_animation(user_id: str):
    url = "https://api.line.me/v2/bot/chat/loading/start"
    payload = json.dumps({
    "chatId": user_id
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer %s' %get_access_token
    }
    requests.request("POST", url, headers=headers, data=payload)


@handler.add(MessageEvent, message=ImageMessageContent)
def handle_image_message(event: MessageEvent):
    loading_animation(user_id=event.source.user_id)
    message_id = event.message.id
    url_reply = f'https://e69043f6026f.ngrok-free.app/img/{message_id}.jpg'
    url_thongdee = f'https://e69043f6026f.ngrok-free.app/thongdee/ThongDee.png'
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        blob_api = MessagingApiBlob(api_client)

    content = blob_api.get_message_content(message_id)

    image_path = f"./img/{message_id}.jpg"
    with open(image_path, "wb") as f:
        f.write(content)
    
    Check = FruitClassify(image_path)
    fruit = Check.predict()

    if fruit == "Pomelo":
        # predict, conf = Classify(event)
        flex_pred, predict = show_pred(event, url_reply)
        print(predict)

        # reply_message = TextMessage(text="ได้รูปแล้ว")
        reply_message = FlexMessage(
            alt_text="ผลทำนาย!",
            contents=flex_pred
        )
        line_bot_api.reply_message(
            ReplyMessageRequest(
            reply_token=event.reply_token, 
            messages=[reply_message]
            )
        )
    
    else:
        flex_not = not_pomelo(url_thongdee)

        reply_message = FlexMessage(
            alt_text="ขออภัย",
            contents=flex_not
        )
        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[reply_message]
            )
        )
    
    # else:
    #     reply_message = TextMessage(text= "รบกวนส่งรูปส้มโอมาอีกครั้งได้ไหมคะ")
    #     line_bot_api.reply_message(
    #         ReplyMessageRequest(
    #         reply_token=event.reply_token, 
    #         messages=[reply_message]
    #         )
    #     )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
