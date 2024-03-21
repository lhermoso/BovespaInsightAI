from crewai import Agent

from tools.brap_tools import *
from tools.calculator_tools import CalculatorTools
from crewai_tools import (

    SerperDevTool,
    WebsiteSearchTool
)
quote_tool = QuoteTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()
calculator_tool = CalculatorTools.calculate
balance_tool = BalanceTools()
dividends_tool = DividendsTools()
income_tool = IncomeStatementTool()
financial_data_tool = FinancialDataTool()
key_stats_tool = DefaultKeyStatisticsTool()



class StockAnalysisAgents:
    def financial_analyst(self):
        return Agent(
            role='The Best Financial Analyst',
            goal="""Impress all customers with your financial data 
      and market trends analysis""",
            backstory="""The most seasoned financial analyst with 
      lots of expertise in stock market analysis and investment
      strategies that is working for a super important customer.""",
            verbose=True,
            max_iter=100,
            tools=[
                quote_tool,
                search_tool,
                web_rag_tool,
                calculator_tool,
                balance_tool,
                dividends_tool,
                income_tool,
                financial_data_tool,
                key_stats_tool
            ],

            memory=True
        )

    def fundamental_analysis_agent(self):
        return Agent(
            role='Expert Financial Analyst',
            goal='Conduct comprehensive fundamental analyses to uncover investment opportunities and risks',
            backstory=(
                "With years of experience in financial markets and a deep understanding of "
                "economic indicators, you excel at dissecting company reports, assessing "
                "financial health, and identifying undervalued stocks. Your insights "
                "inform investment strategies, guiding stakeholders toward sound financial "
                "decisions. Equipped with a meticulous approach to data, you navigate through "
                "complex financial landscapes, turning intricate details into actionable "
                "investment advice."
            ),
            verbose=True,
            tools=[
                quote_tool,
                search_tool,
                web_rag_tool,
                calculator_tool,
                balance_tool,
                dividends_tool,
                income_tool,
                financial_data_tool,
                key_stats_tool
            ],

            memory=True
        )

    def research_analyst(self):
        return Agent(
            role='Staff Research Analyst',
            goal="""Being the best at gather, interpret data and amaze
      your customer with it""",
            backstory="""Known as the BEST research analyst, you're
      skilled in sifting through news, company announcements, 
      and market sentiments. Now you're working on a super 
      important customer""",
            verbose=True,
            tools=[
                quote_tool,
                search_tool,
                web_rag_tool,
                calculator_tool,
                balance_tool,
                dividends_tool,
                income_tool,
                financial_data_tool,
                key_stats_tool
            ],

            memory=True
        )

    def investment_advisor(self):
        return Agent(
            role='Private Investment Advisor',
            goal="""Impress your customers with full analyses over stocks
      and completer investment recommendations""",
            backstory="""You're the most experienced investment advisor
      and you combine various analytical insights to formulate
      strategic investment advice. You are now working for
      a super important customer you need to impress.""",
            verbose=True,
            tools=[
                quote_tool,
                search_tool,
                web_rag_tool,
                calculator_tool,
                balance_tool,
                dividends_tool,
                income_tool,
                financial_data_tool,
                key_stats_tool
            ],

            memory=True
        )
