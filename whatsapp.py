import pywhatkit
from datetime import *

def send_news_whatsapp(new_str):

    hour = int(datetime.now().hour)
    min = int(datetime.now().minute + 1)
    
    pywhatkit.sendwhatmsg("+61433794469", new_str, hour, min)
