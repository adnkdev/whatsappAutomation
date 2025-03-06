from api import *
from whatsapp import *

def main():
    send_news_whatsapp("group_id",get_AI_news())


if __name__ == '__main__':
    main()
    