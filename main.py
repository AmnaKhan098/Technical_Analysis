from source.get_ticker import get_Ticker
from source.get_chart import chart_generation
from source.get_analysis import get_Analysis
from source.get_news import  Get_news
# user query
Query=input("Enter your query :")
ticker=get_Ticker(Query).content
image2= chart_generation(ticker)
analysis= get_Analysis(image2)
newsD=Get_news(ticker)