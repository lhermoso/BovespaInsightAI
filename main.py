from crewai import Crew
from textwrap import dedent

from stock_analysis_agents import StockAnalysisAgents
from stock_analysis_tasks import StockAnalysisTasks

from dotenv import load_dotenv

load_dotenv()


class FinancialCrew:
    def __init__(self, company):
        self.company = company

    def run(self):
        agents = StockAnalysisAgents()
        tasks = StockAnalysisTasks()

        research_analyst_agent = agents.research_analyst()
        financial_analyst_agent = agents.financial_analyst()
        fundamental_analysis_agent = agents.fundamental_analysis_agent()
        investment_advisor_agent = agents.investment_advisor()

        research_task = tasks.research(research_analyst_agent, self.company)
        financial_task = tasks.financial_analysis(financial_analyst_agent)
        fundamental_task = tasks.fundamental_analysis(fundamental_analysis_agent)
        recommend_task = tasks.recommend(investment_advisor_agent)

        crew = Crew(
            agents=[
                research_analyst_agent,
                financial_analyst_agent,
                investment_advisor_agent
            ],
            tasks=[
                research_task,
                financial_task,
                fundamental_task,
                recommend_task
            ],
            verbose=True
        )

        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("## Bem-vindo ao Grupo de Análise Financeira")
    print('-------------------------------')
    company = input(
        dedent("""
      Qual é a empresa que você deseja analisar?
    """))

    financial_crew = FinancialCrew(company)
    result = financial_crew.run()
    print("\n\n########################")
    print("## Aqui está o Relatório")
    print("########################\n")
    print(result)
