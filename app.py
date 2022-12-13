from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    QuickReplyButton, MessageAction, QuickReply,
    FollowEvent,
    )
from dotenv import load_dotenv
import db
import os

load_dotenv()

app = Flask(__name__)

CHANNEL_ACCESS_TOKEN = "bqmeLzbJXaUVnqtfy6lznRTO/D7AD9uXvPd4ZNiMk6DyaToLUYSIkK5P9CZjytbvkzTiOFUA3+Wnp4R4RV2sdR6bEJRAIiMEnRW7nj23BPrLwUAiNS4yK5hfBQB6eubVJq/ZeXzOnKRAxVltbaRPDQdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = os.getenv("CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("CHANNEL_SECRET")


line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

command_list = ["使い方", "新しい情報", "組織設定"]
items = [QuickReplyButton(action=MessageAction(label=f"{command}", text=f"{command}")) for command in command_list]


@app.route("/")
def hello_world():
  return "deploy check"

@app.route("/callback", methods=['POST'])
def callback():
  signature = request.headers['X-Line-Signature']
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)

  return 'OK'

@handler.add(FollowEvent)
def handle_follow(event):

    profile = line_bot_api.get_profile(event.source.user_id)

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=profile.display_name + "さん、はじめまして！\n" +
        "友だち追加ありがとうございます。wiz落とし物botです。\n" +
        "はじめてのご利用される方は、下のコマンドから使い方をご確認ください。",
        quick_reply=QuickReply(items=items)
        )
    )



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

  messages = TextSendMessage(text="コマンドを入力",
                              quick_reply=QuickReply(items=items))



  line_bot_api.reply_message(event.reply_token, messages=messages)




if __name__ == "__main__":
  app.run(host="0.0.0.0",port=5000)
