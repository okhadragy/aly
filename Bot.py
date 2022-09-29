import requests,json,os

class Bot:

    def __init__(self,token):
        self.token = token
        self.url = f'https://api.telegram.org/bot{self.token}/'

    def parse_message(self,message):
        if message.get("message"):
            user = message.get('message').get('from')
            chat = message.get('message').get('chat')
            date = message.get('message').get('date')
            msg = ""
            msg_type = "text"

            if message.get('message').get('text'):
                msg = message.get('message').get('text')
                msg_type = "text"
                if message.get('message').get('reply_markup'):
                    msg = {"text":message.get('message').get('text'),"reply_markup":message.get('message').get('reply_markup')}
                    if message.get('message').get('reply_markup').get('inline_keyboard'):
                        if message.get('message').get('reply_markup').get('inline_keyboard')[0][0].get("url"):
                            msg_type = "inline_url_buttons"
                        else:
                            msg_type = "inline_buttons"
                    else:
                        msg_type = "buttons"
                
            elif message.get('message').get('video'):
                msg = message.get('message').get('video')
                msg_type = "video"

            elif message.get('message').get('voice'):
                msg = message.get('message').get('voice')
                msg_type = "voice"

            elif message.get('message').get('document'):
                if message.get('message').get('animation'):
                    msg = message.get('message').get('animation')
                    msg_type = "animation"
                else:
                    msg = message.get('message').get('document')
                    msg_type = "document"

            elif message.get('message').get('photo'):
                msg = message.get('message').get('photo')
                msg_type = "photo"
            
            elif message.get('message').get('video_note'):
                msg = message.get('message').get('video_note')
                msg_type = "video_note"
            
            elif message.get('message').get('location'):
                msg = message.get('message').get('location')
                msg_type = "location"
            
            elif message.get('message').get('poll'):
                msg = message.get('message').get('poll')
                msg_type = "poll"
            
            elif message.get('message').get('contact'):
                msg = message.get('message').get('contact')
                msg_type = "contact"
            
            elif message.get('message').get('sticker'):
                msg = message.get('message').get('sticker')
                msg_type = "sticker"


            
        elif message.get('callback_query'):
            user = message.get('callback_query').get('from')
            chat = message.get('callback_query').get("message").get('chat')
            date = message.get('callback_query').get("message").get('date')
            msg = message.get('callback_query').get('data')
            msg_type = "text"

        return user,chat,date,msg,msg_type
    
    def get_user_profile_photos(self,user_id, **more):
        payload = {
            'user_id': user_id,
            **more
        }
        r = requests.post(self.url+"getUserProfilePhotos",json=payload)
        return r

    def forward_message(self,chat_id, from_chat_id, msg_id, disable_notification=False):
        payload = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': msg_id,
            'disable_notification':disable_notification
        }
        r = requests.post(self.url+"forwardMessage",json=payload)
        return r 

    def send_chat_action(self,chat_id, action):
        payload = {
            'chat_id': chat_id,
            'action': action,
        }
        r = requests.post(self.url+"sendChatAction",json=payload)
        return r

    def send_message(self,chat_id, text, **more):
        payload = {
            'chat_id': chat_id,
            'text': text,
            **more
        }
        r = requests.post(self.url+"sendMessage",json=payload)
        return r
    
    def send_audio(self,chat_id,audio_url, **more):
        payload = {
            'chat_id': chat_id,
            "audio": audio_url,
            **more
        }
        r = requests.post(self.url+"sendAudio", json=payload)
        return r
    
    def send_voice(self,chat_id,voice_url, **more):
        payload = {
            'chat_id': chat_id,
            "audio": voice_url,
            **more
        }
        r = requests.post(self.url+"sendVoice", json=payload)
        return r
    
    def send_photo(self,chat_id,photo_url,caption="", **more):
        payload = {
            'chat_id': chat_id,
            'photo': photo_url,
            'caption': caption,
            **more
        }
        r = requests.post(self.url+"sendPhoto", json=payload)
        return r
    
    def send_video(self,chat_id,video_url, **more):
        payload = {
            'chat_id': chat_id,
            'video': video_url,
            **more
        }
        r = requests.post(self.url+"sendVideo", json=payload)
        return r

    def send_doc(self,chat_id,doc_url, **more):
        payload = {
            'chat_id': chat_id,
            'document': doc_url,
            **more
        }
        r = requests.post(self.url+"sendDocument", json=payload)
        return r
    
    def send_sticker(self,chat_id,sticker_url, **more):
        payload = {
            'chat_id': chat_id,
            'sticker': sticker_url,
            **more
        }
        r = requests.post(self.url+"sendSticker", json=payload)
        return r

    def send_loc(self,chat_id,latitude,longitude, **more):
        payload = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            **more
        }
        r = requests.post(self.url+"sendLocation", json=payload)
        return r

    def send_poll(self,chat_id,question,options,correct_val,type="quiz",is_anonymous=False):
        payload = {
        'chat_id': chat_id,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": is_anonymous,
        "type": type,
        "correct_option_id": options.index(correct_val)
        }

        r = requests.post(self.url+"sendPoll", json=payload)
        return r

    def send_button(self,chat_id, text, button_text, callback_data=[], callback_urls=[]):
        if len(callback_data) == 0 and len(callback_urls) == 0:
            buttons = {'keyboard': [[{'text': txt} for txt in button_text]]}
        else:
            if len(callback_urls) == 0:
                if len(callback_data) == len(button_text):
                    buttons = {'inline_keyboard': [[{'text': button_text[i],"callback_data": callback_data[i]} for i in range(len(button_text))]]}
                else:
                    buttons = None
                    print("Number of CallBack data not equal number of buttons")

            elif len(callback_data) == 0:
                if len(callback_urls) == len(button_text):
                    buttons = {'inline_keyboard': [[{'text': button_text[i],"url": callback_urls[i]} for i in range(len(button_text))]]}
                else:
                    buttons = None
                    print("Number of CallBack urls not equal number of buttons")

        if buttons:
            payload = {
                'reply_markup': buttons
            }
            self.send_message(chat_id, text, **payload)
        else:
            self.send_message(chat_id, "Sorry Server Error")
    
    def download_file(self,file_id):
        url = f'{self.url}getFile?file_id={file_id}'
        a = requests.post(url)
        json_resp = json.loads(a.content)
        file_path = json_resp['result']['file_path']
        print(file_path)
    
        url_1 = f'https://api.telegram.org/file/bot{self.token}/{file_path}'
        b = requests.get(url_1)
        file_content = b.content

        self.create_folder(file_path.split("/")[0])
        with open("files/"+file_path, "wb") as f:
            f.write(file_content)
    
    def save_data(self,file_name,**data):
        try:
            with open("files/"+file_name+".json","r") as file:
                try:
                    json_data = json.loads(file.read())
                except json.JSONDecodeError:
                    json_data = []
        except FileNotFoundError:
            json_data = []

        json_data.append(data)           
        json_data = json.dumps(json_data)  

        with open("files/"+file_name+".json","w") as file:
            file.write(json_data)

    def save(self,username,chat_id,date,msg,msg_type,high_quality_photos=False):
        if msg_type != "poll" and msg_type != "buttons" and msg_type != "inline_buttons" and msg_type != "inline_url_buttons": 
            if msg_type == "photo":
                if high_quality_photos:
                    photo_index = -1
                else:
                    photo_index = 0
                file_id = msg[photo_index].get("file_id")
                self.download_file(file_id)
            elif msg_type == "location":
                data = {"username":username,"chat_id":chat_id,"date":date,"location":msg}
                self.save_data("locations",**data)
            elif msg_type == "text":
                data = {"username":username,"chat_id":chat_id,"date":date,"text":msg}
                self.save_data("chat",**data)
            elif msg_type == "contact":
                data = {"username":username,"chat_id":chat_id,"date":date} | msg
                self.save_data("contacts",**data)
            else:
                file_id = msg.get("file_id")
                self.download_file(file_id)
    
    def create_folder(self,folder):
        try:
            os.mkdir(f'{os.getcwd()}/files/{folder}')
        except FileExistsError:
            pass

