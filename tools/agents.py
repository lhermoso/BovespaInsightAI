from crewai import Agent

from tools.quote_tools import QuoteTool

from crewai_tools import (

    SerperDevTool,
    WebsiteSearchTool
)


quote_tool = QuoteTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

from langchain.tools.yahoo_finance_news import YahooFinanceNewsTool


class StockAnalysisAgents():
  def financial_analyst(self):
    return Agent(
      role='The Best Financial Analyst',
      goal="""Impress all customers with your financial data 
      and market trends analysis""",
      backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
      verbose=True,
      tools=[
        quote_tool,
        search_tool,
        web_rag_tool,
        YahooFinanceNewsTool()
      ]
    )
