from textwrap import dedent
from crewai import Agent
from tools import GoogleFinance
class Stock_bot_agents():
    def stock_anaylsis(self):
        return Agent(
            role = "Stock Analysis",
            goal = "To give basic details and analysis of the stock.",
            tools = GoogleFinance.tools(),
            backstory=dedent("""
            As a stock analyst you are working for a stock market analysis company.
            you have been assigned to give basic details and analysis of the stock.
            for this task you have been provided with the stock name and the data about the stock.
            """),
            verbose=True
        )
    def News_analysis(self):
        return Agent(
            role = "Stock News Analysis",
            goal = "To give news analysis of the stock.",
            tools = GoogleFinance.tools(),
            backstory=dedent("""
            As a stock analyst you are working for a stock market analysis company.
            you have been assigned to give news analysis of the stock.
            try to give the latest news about the company, any major events, etc. with its impact on the stock.
            """),
            verbose=True
        )
    def Trend_analysis(self):
        return Agent(
            role = "Stock Trend Analysis",
            goal = "To give trend analysis of the stock.",
            tools = GoogleFinance.tools(),
            backstory=dedent("""
            As a stock analyst you  are working for a stock market analysis company.
            you have been assigned to give trend analysis of the stock.
            for this task you have been provided with the stock name and the data about the stock.
            try to give the stock price trend for the last 1 year, 6 months, 3 months, etc.
            """),
            verbose=True,
        )
    def financial_analysis(self):
        return Agent(
            role = "Stock Financial Analysis",
            goal = "To give financial analysis of the stock.",
            tools = GoogleFinance.tools(),
            backstory=dedent("""
            As a stock analyst you are working for a stock market analysis company.
            you have been assigned to give financial analysis of the stock.
            for this task you have been provided with the stock name and the data about the stock.
            try to get all the financial data of the stock and give a detailed analysis of the stock.
            also generate some graphs and charts for better understanding where required.
            """),
            verbose=True,
        )
    def create_detailed_report(self):
        return Agent(
            role = "Stock Detailed Report",
            goal = "To create a detailed report of the stock.",
            tools = GoogleFinance.tools(),
            backstory=dedent("""
            As a stock analyst you are working for a stock market analysis company.
            you have been assigned to create a detailed report of the stock.
            for this task you have been provided with the stock name and the data about the stock.
            try to create a detailed report of the stock including basic details, trend analysis, news analysis, financial analysis, etc.
            """),
            verbose=True,
        ) 