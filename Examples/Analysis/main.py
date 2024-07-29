import logging
from dotenv import load_dotenv
from crewai import Crew
from task import Stock_bot
from agents import Stock_bot_agents
from serp import json_data

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    load_dotenv()

    logging.info("#### -----WELCOME TO STOCK ANALYSIS BOT -----####")
    logging.info("------_____________________________________------")
    logging.info("Enter the stock name you want to analyze:")
    
    stock = input()
    logging.debug(f"Stock name entered: {stock}")

    try:
        stock_data = open('./data.txt')  # json_data(stock)
        logging.debug("Stock data loaded successfully.")
    except Exception as e:
        logging.error(f"Error loading stock data: {e}")
        return

    tasks = Stock_bot()
    agent = Stock_bot_agents()

    # Create agents
    basic_details = agent.stock_anaylsis()
    news_analysis = agent.News_analysis()
    trend_analysis = agent.Trend_analysis()
    financial_analysis = agent.financial_analysis()
    create_stock_report = agent.create_detailed_report()

    # Create tasks
    basic_details_task = tasks.basic_info(basic_details, stock, stock_data)
    news_analysis_task = tasks.stock_news(news_analysis, stock, stock_data)
    trend_analysis_task = tasks.stock_trend(trend_analysis, stock, stock_data)
    financial_analysis_task = tasks.stock_financials(financial_analysis, stock, stock_data)
    create_stock_report_task = tasks.stock_report(create_stock_report, stock, stock_data)

    # Execute tasks
    logging.debug("Creating Crew instance with agents and tasks.")
    crew = Crew(
        agents=[
            basic_details,
            news_analysis,
            trend_analysis,
            financial_analysis,
            create_stock_report
        ],
        tasks=[
            basic_details_task,
            news_analysis_task,
            trend_analysis_task,
            financial_analysis_task,
            create_stock_report_task
        ],
    )

    try:
        result = crew.kickoff()
        logging.info("Crew kickoff executed successfully.")
        logging.debug(f"Result: {result}")
    except Exception as e:
        logging.error(f"Error during crew kickoff: {e}")

    print(result)

if __name__ == '__main__':
    main()
