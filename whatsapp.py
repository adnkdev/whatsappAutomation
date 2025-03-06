import pywhatkit
from datetime import *

#send whatsapp information to group chat

def send_news_whatsapp(group_id, new_str):

    curr_hour = int(datetime.now().hour)
    cur_min = int(datetime.now().minute + 1)
    
    pywhatkit.sendwhatmsg_to_group(group_id, new_str, curr_hour, cur_min)
