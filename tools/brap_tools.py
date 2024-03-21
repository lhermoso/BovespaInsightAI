from crewai_tools import BaseTool

import requests

from textwrap import dedent
from typing import Any, Type
import os
from pydantic.v1 import BaseModel, Field


class BrapToolSchema(BaseModel):
    stock_ticker: str = Field(..., description="Mandatory stock ticker you want to use this tool")


class BalanceTools(BaseTool):
    name: str = "Get Balance Sheet Info"
    description: str = dedent(""" Useful to get Balance Sheet history for a
    given stock.
    """)
    args_schema: Type[BaseModel] = BrapToolSchema

    def _run(self, stock_ticker: str) -> Any:
        params = {
            'range': '6mo',
            'interval': '1d',
            'modules': 'balanceSheetHistory',
            'fundamental': 'true',
            'token': os.getenv("BRAP_API_KEY"),
        }
        url = f"https://brapi.dev/api/quote/{stock_ticker}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Sorry, I couldn't find any Balance Sheet  for this stock, check if the ticker is correct."
        response = response.json()

        fillings = response["results"][0]['balanceSheetHistory']['balanceSheetStatements']
        return fillings


class DividendsTools(BaseTool):
    name: str = "Get Dividends Info"
    description: str = dedent(""" Useful to get Dividends history for a
    given stock.
    """)
    args_schema: Type[BaseModel] = BrapToolSchema

    def _run(self, stock_ticker: str) -> Any:
        params = {
            'range': '6mo',
            'interval': '1d',
            'dividends': 'true',
            'fundamental': 'true',
            'token': os.getenv("BRAP_API_KEY"),
        }
        url = f"https://brapi.dev/api/quote/{stock_ticker}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Sorry, I couldn't find any Dividends for this stock, check if the ticker is correct."
        response = response.json()

        fillings = response["results"][0]['dividendsData']["cashDividends"]
        return fillings


class IncomeStatementTool(BaseTool):
    name: str = "Get Income Statement Info"
    description: str = dedent(""" Useful to get Income Statement history for a
    given stock.
       """)
    args_schema: Type[BaseModel] = BrapToolSchema

    def _run(self, stock_ticker: str) -> Any:
        params = {
            'range': '6mo',
            'interval': '1d',
            'fundamental': 'true',
            'modules': 'incomeStatementHistory',
            'token': os.getenv("BRAP_API_KEY"),
        }
        url = f"https://brapi.dev/api/quote/{stock_ticker}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Sorry, I couldn't find any Income Statement  for this stock, check if the ticker is correct."
        response = response.json()
        fillings = response["results"][0]['incomeStatementHistory']["incomeStatementHistory"]
        return fillings


class FinancialDataTool(BaseTool):
    name: str = "Get Financial Data Info"
    description: str = dedent(""" Useful to get Financial Data for a
    given stock.
    """
                              )
    args_schema: Type[BaseModel] = BrapToolSchema

    def _run(self, stock_ticker: str) -> Any:
        params = {
            'range': '6mo',
            'interval': '1d',
            'fundamental': 'true',
            'modules': 'financialData',
            'token': os.getenv("BRAP_API_KEY"),
        }
        url = f"https://brapi.dev/api/quote/{stock_ticker}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Sorry, I couldn't find any Financial Data for this stock, check if the ticker is correct."
        response = response.json()
        fillings = response["results"][0]['financialData']
        return fillings


class DefaultKeyStatisticsTool(BaseTool):
    name: str = "Get Default Key Statistics "
    description: str = dedent(""" Useful to get Default Key Statistics  for a
    given stock.
    """
                              )
    args_schema: Type[BaseModel] = BrapToolSchema

    def _run(self, stock_ticker: str) -> Any:
        params = {
            'range': '6mo',
            'interval': '1d',
            'fundamental': 'true',
            'modules': 'defaultKeyStatistics',
            'token': os.getenv("BRAP_API_KEY"),
        }
        url = f"https://brapi.dev/api/quote/{stock_ticker}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Sorry, I couldn't find any Financial Data for this stock, check if the ticker is correct."
        response = response.json()
        fillings = response["results"][0]['financialData']
        return fillings


class QuoteTool(BaseTool):
    name: str = "Download quote data"
    description: str = dedent("""Retrieves OHLC (Open, High, Low, Close) data and trading volume"
    """)
    args_schema: Type[BaseModel] = BrapToolSchema

    def _run(self, stock_ticker: str) -> Any:
        params = {
            'range': '6mo',
            'interval': '1d',
            'token': os.getenv("BRAP_API_KEY"),
        }
        url = f"https://brapi.dev/api/quote/{stock_ticker}"
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return "Sorry, I couldn't find any Quote for this stock, check if the ticker is correct."
        response = response.json()
        fillings = response["results"][0]["historicalDataPrice"]
        return fillings
