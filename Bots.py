
import time
from Bot import Bot

class MohammedSabryBot(Bot):
    def __init__(self, token, res):
        self.res = res
        super().__init__(token)

    def run(self):
        if self.res.get("message") or self.res.get("callback_query"):
            user,chat,date,msg,msg_type = self.parse_message(self.res)
            if msg_type == "text":
                if msg.lower() == "/start":
                    bot_msg = f'Hi {user["first_name"]} {user["last_name"]} 👋'
                    img = f'https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg'
                    
                    self.send_chat_action(chat["id"],"typing")
                    time.sleep(1)

                    self.send_message(chat["id"],bot_msg)

                    self.send_chat_action(chat["id"],"typing")
                    time.sleep(1)

                    self.send_message(chat["id"],"👋")

                    self.send_chat_action(chat["id"],"upload_photo")
                    time.sleep(1)

                    self.send_photo(chat["id"],img,"Hey bro")
                
                if msg.lower() == "/button":
                    bot_msg = f'What is the type of buttons you want ?'
                    self.send_button(chat["id"],bot_msg,["inline","normal"],["/inline","/normal"])
                
                if msg.lower() == "/inline":
                    bot_msg = f'What is your favourite social media?'
                    self.send_button(chat["id"],bot_msg,["tiktok","facebook","youtube"],callback_urls=["https://www.tiktok.com/en/","https://www.facebook.com/","https://youtube.com/"])
                
                if msg.lower() == "/normal":
                    bot_msg = f'Do you love eating?'
                    self.send_button(chat["id"],bot_msg,["No","Yes"])
                
                if msg.lower() == "/video":
                    bot_msg = f'https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4'
                    self.send_video(chat["id"],bot_msg)
                
                if msg.lower() == "/audio":
                    bot_msg = f'http://www.largesound.com/ashborytour/sound/brobob.mp3'
                    self.send_audio(chat["id"],bot_msg)
                
                if msg.lower() == "/photo":
                    bot_msg = f'https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg'
                    self.send_photo(chat["id"],bot_msg)
                
                if msg.lower() == "/doc":
                    bot_msg = f'http://www.africau.edu/images/default/sample.pdf'
                    self.send_doc(chat["id"],bot_msg)
                
                if msg.lower() == "/quiz":
                    q1="What is greater than 5?"
                    a1 = ["1","2","3","-6","6"]
                    q2 = "عدد اركان الاسلام"
                    a2 = ["6","7","8","5"]
                    q3 = "متي ولد عمر"
                    a3 = ["2005","2003","1999"]
                    self.send_poll(chat["id"],q1,a1,"6")
                    self.send_poll(chat["id"],q2,a2,"5")
                    self.send_poll(chat["id"],q3,a3,"2005")

            self.save(user["username"],chat["id"],date,msg,msg_type,True)
        
        else:
            print(self.res)


        

        



        