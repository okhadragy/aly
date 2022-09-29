from flask import Response,request,Flask
import time
from Bot import Bot
from Bots import MohammedSabryBot

# helping website https://www.pragnakalp.com/create-telegram-bot-using-python-tutorial-with-examples/
TOKEN = "5635111743:AAFwNyYG0rE0xZUDdkWEPcjj3Xon2P3bW2g"
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>Welcome!</h1>"


@app.route('/mohamedsabry', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        res = request.get_json()
        mohamed_sabry = MohammedSabryBot(TOKEN,res)
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(threaded=True)