from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======python的函數庫==========
import tempfile, os
import datetime
import time
#======python的函數庫==========


app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('pb57u0/zE4s7AiY6dZGmaX++jErYM0uFwRDPX3h7DdHAaznUAWHJS4GjsOwYi6BgyegVPbieQ0xEV7ALOjmPujh2nd0fIbi+fhJquM+14k3mtdvYo1+XpvY2668OMuoBHQXX4aoVs1jb2u/CWfEnDQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('c0b34c011fab3b43a8bd24e39e4e0e07')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# 處理訊息
@handler.add(FollowEvent)
def handle_follow(event):
    id = event.source.user_id
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text='user id :' + id)) 

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
