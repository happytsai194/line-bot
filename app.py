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

app = Flask(__name__)

line_bot_api = LineBotApi('av9kJG/rK2DY3BKPiEwVsTHz8xYeA9lK2xhGhMuN2LTRo85lQHS+2oaBytiODi5KB3DSMxWsHp+9mmlEZvQbBr4Cd104Pb3M9UXX0AwztFln3ky63Ee9Q/7CXS4ZTM5OV6g5ZwIqIYJmMkCzI1KJFAdB04t89/1O/w1cDnyilFU=+QNUBK0qHk06I4yz2yCUc4VF+VdHLwQLIAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f45e0f7761b2f7c333d7471bcc5d06e1')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='吃飽沒'))


if __name__ == "__main__":
    app.run()