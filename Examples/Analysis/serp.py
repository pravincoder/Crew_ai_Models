# Data providing functions using SerpApi 
from serpapi import search
import json
import os
from dotenv import load_dotenv
load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
def stock_data(stock: str):
    params = {
                "engine": "google_finance",
                "q": stock,
                "api_key": SERPAPI_API_KEY
    }
    sear = search(params)
    results = sear
    return results # Results will be a dictionary

def stock_news(stock: str):
    params = {
        "engine": "google_news",
        "q": "Top news about "+stock,
        "api_key": SERPAPI_API_KEY
    }
    sear = search(params)
    results = sear
    return results # Results will be a dictionary

def json_data(stock: str):
    return {
        "stock_name": stock,
        "stock_data": stock_data(stock).as_dict(),
        "stock_news": stock_news(stock).as_dict()
    }
