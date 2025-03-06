from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
from datetime import datetime
from datetime import timedelta
import requests


def get_AI_news():

    #load api key 
    load_dotenv()
    api_key= os.getenv("API_KEY")


    # Init
    newsapi = NewsApiClient(api_key=api_key)

    # calculate dates for the past two days 
    today = datetime.now().date()
    two_days_ago = today - timedelta(days=2)


    # retrieve AI news from news API
    top_headlines_AI = newsapi.get_everything(q='AI company',
                                            language='en', 
                                            from_param=f"{str(two_days_ago)}",
                                            to=f"{str(today)}",
                                            sort_by='relevancy'
                                            )
    
    if(top_headlines_AI["status"] == "ok" and len(top_headlines_AI["articles"]) > 0):

        return format_news(top_headlines_AI["articles"])
    else:
        return "something went wrong with API"


    

#converst JSON into a news string

def format_news(news_JSON):
     
     news_string = '*AI News Today*\n\n'
     current_article_num = 1

     if len(news_JSON) < 10: 
         
         for article in news_JSON :
             
            news_string += f"{current_article_num}. {article["title"]}\n{article["url"]}\n"
            current_article_num += 1

         return news_string
   
     else:

        for article in news_JSON :

            if "AI" in article["title"] and "Research" not in article["title"] and current_article_num < 11:

                news_string += f"{current_article_num}. {article["title"]}\n{shorten(article["url"])}\n"
                current_article_num += 1

        return news_string
     

# shorten the url 

def shorten(url):
  base_url = 'http://tinyurl.com/api-create.php?url='
  response = requests.get(base_url+url)
  short_url = response.text
  return short_url



    






