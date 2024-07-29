import logging
from textwrap import dedent
from crewai import Task  # Assuming Task is defined in some_module

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class Stock_bot:
    def basic_info(self, agent, stock_name, json_data):
        """Do basic analysis of the stock"""
        description = dedent(f"""
            Your task is to give brief information about the {stock_name} stock.
            like the current price, market cap, P/E ratio, etc. in a structured format.
            also provide a small paragraph about the company like what they do, etc.
            all the data about {stock_name} stock is provided in the json_data.
            {json_data} only use the required data.
            Try making the output as structured as possible.
        """)
        expected_output = dedent(f"""
            All basic details about the {stock_name} stock and a small paragraph about the company.
            Try making the output as structured as possible.
        """)

        logging.debug("Creating basic_info task")
        logging.debug(f"description: {description}")
        logging.debug(f"expected_output: {expected_output}")

        print("Description:", description)
        print("Expected Output:", expected_output)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )

    def stock_trend(self, agent, stock_name, json_data):
        """Do trend analysis of the stock"""
        description = dedent(f"""
            Your task is to give a trend analysis of the {stock_name} stock.
            like the stock price trend for the last 1 year, 6 months, 3 months, etc.
            all the data about {stock_name} stock is provided in the json_data.
            {json_data} only use the required data.
            Try making the output as structured as possible.
        """)
        expected_output = dedent(f"""
            Trend analysis of the {stock_name} stock.
            like the stock price trend for the last 1 year, 6 months, 3 months, etc.
            Try making the output as structured as possible.
        """)

        logging.debug("Creating stock_trend task")
        logging.debug(f"description: {description}")
        logging.debug(f"expected_output: {expected_output}")

        print("Description:", description)
        print("Expected Output:", expected_output)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )

    def stock_news(self, agent, stock_name, json_data):
        """Do news analysis of the stock"""
        description = dedent(f"""
            Your task is to give news analysis of the {stock_name} stock.
            like the latest news about the company, any major events, etc.
            all the data about {stock_name} stock is provided in the json_data.
            {json_data} only use the required data.
            Try making the output as structured as possible.
        """)
        expected_output = dedent(f"""
            News analysis of the {stock_name} stock.
            like the latest news about the company, any major events, etc.
            Try making the output as structured as possible.
        """)

        logging.debug("Creating stock_news task")
        logging.debug(f"description: {description}")
        logging.debug(f"expected_output: {expected_output}")

        print("Description:", description)
        print("Expected Output:", expected_output)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )

    def stock_financials(self, agent, stock_name, json_data):
        """Do financial analysis of the stock"""
        description = dedent(f"""
            Your task is to give financial analysis of the {stock_name} stock.
            like the revenue, profit, etc. in a structured format.
            all the data about {stock_name} stock is provided in the json_data.
            {json_data} only use the required data.
            Try making the output as structured as possible.
        """)
        expected_output = dedent(f"""
            Financial analysis of the {stock_name} stock.
            like the revenue, profit, etc. in a structured format.
            Try making the output as structured as possible.
        """)

        logging.debug("Creating stock_financials task")
        logging.debug(f"description: {description}")
        logging.debug(f"expected_output: {expected_output}")

        print("Description:", description)
        print("Expected Output:", expected_output)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )

    def stock_report(self, agent, stock_name, json_data):
        """Create a stock report of the stock"""
        description = dedent(f"""
            Your task is to create a stock report of the {stock_name} stock.
            like the basic details, trend analysis, news analysis, financial analysis, etc.
            all the data about {stock_name} stock is provided in the json_data.
            {json_data} only use the required data.
            Try making the output as structured as possible.
        """)
        expected_output = dedent(f"""
            Stock report of the {stock_name} stock.
            like the basic details, trend analysis, news analysis, financial analysis, etc.
            Try making the output as structured as possible.
        """)

        logging.debug("Creating stock_report task")
        logging.debug(f"description: {description}")
        logging.debug(f"expected_output: {expected_output}")

        print("Description:", description)
        print("Expected Output:", expected_output)

        return Task(
            description=description,
            expected_output=expected_output,
            agent=agent
        )
