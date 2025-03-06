from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
from datetime import datetime
from datetime import timedelta



def get_AI_news():

    #load api key 
    load_dotenv()
    api_key= os.getenv("API_KEY")


    # Init
    newsapi = NewsApiClient(api_key=api_key)

    # calculate dates for the past two days 
    today = datetime.now().date()
    two_days_ago = today - timedelta(days=2)


    # /v2/top-headlines
    top_headlines_AI = newsapi.get_everything(q='AI',
                                            language='en', 
                                            from_param=f"{str(two_days_ago)}",
                                            to=f"{str(today)}",
                                            )

    top_headlines_AIcompany = newsapi.get_everything(q='AI company',
                                            language='en', 
                                            from_param=f"{str(two_days_ago)}",
                                            to=f"{str(today)}",
                                            )
    
    format_news(top_headlines_AI)



def format_news(news_JSON):

     for article in news_JSON["articles"]:
        print(f"{article["title"]}\n")
        print(f"{article["url"]}\n\n")






