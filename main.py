from source.get_ticker import get_Ticker
from source.get_chart import chart_generation
from source.get_analysis import get_Analysis
from source.get_news import  Get_news
# user query
# user query
def process_query(query):
    ticker = get_Ticker(query).content
    image2 = chart_generation(ticker)  # should return a path to image
    analysis = get_Analysis(image2).content
    newsD = Get_news(ticker)
    return image2, analysis, newsD
