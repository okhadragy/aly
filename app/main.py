from flask import Response,request,Flask
from Bots import MohammedSabryBot

# helping website https://www.pragnakalp.com/create-telegram-bot-using-python-tutorial-with-examples/
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>Welcome!</h1>"


@app.route('/mohamedsabry', methods=['GET', 'POST'])
def mohamed_sabry():
    if request.method == 'POST':
        res = request.get_json()
        TOKEN = "5635111743:AAFwNyYG0rE0xZUDdkWEPcjj3Xon2P3bW2g"
        MohammedSabryBot(TOKEN,res)
        return Response('ok', status=200)
    else:
        return "<h1>Welcome to mohamedsabry</h1>"
 