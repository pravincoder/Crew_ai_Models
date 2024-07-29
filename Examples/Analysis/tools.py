# We will create a tool class that will contain all the tools that we will use for analysis
from langchain.agents import tool

class GoogleFinance():
    @tool
    def analyze(stock: str):
        """"Analyzing the stock using Google Finance"""
        data = open('./data.txt')
        return data
       
    @tool
    def get_stock_news(stock: str):
        """Get the latest news about the stock using Google Finance"""
        news = open('./data.txt')
        return news
    @tool
    def create_stock_report(stock: str):
        """Create a stock report using Google Finance"""
        return [GoogleFinance.analyze(stock),GoogleFinance.get_stock_report(stock)]
    
    def tools():
        return [GoogleFinance.analyze,
                GoogleFinance.get_stock_news,
                GoogleFinance.create_stock_report
                ]