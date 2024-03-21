from datetime import datetime

from crewai import Task
from textwrap import dedent


class StockAnalysisTasks:
    def research(self, agent, company):
        return Task(description=dedent(f"""
        Collect and summarize recent news articles, press
        releases, and market analyses related to the stock and
        its industry.
        Pay special attention to any significant events, market
        sentiments, and analysts' opinions. Also include upcoming 
        events like earnings and others.
  
        Your final answer MUST be a report that includes a
        comprehensive summary of the latest news, any notable
        shifts in market sentiment, and potential impacts on 
        the stock.
        Also make sure to return the stock ticker.
        
        {self.__tip_section()}
  
        Make sure to use the most recent data as possible.
  
        Selected company by the customer: {company}
      """),
                    agent=agent,
                    expected_output=dedent("""An executive summary report including a detailed overview of recent significant 
                                    events, market trends, analysts' opinions, and upcoming financial events related 
                                    to the stock of Stock in question. The report should be concise, 
                                    well-structured, and include the stock ticker. It must be backed by data and 
                                    references from credible sources, formatted as a PDF document for professional 
                                    presentation.""")

                    )

    def financial_analysis(self, agent):
        return Task(description=dedent(f"""
        Conduct a thorough analysis of the stock's financial
        health and market performance. 
        This includes examining key financial metrics such as
        P/E ratio, EPS growth, revenue trends, and 
        debt-to-equity ratio. 
        Also, analyze the stock's performance in comparison 
        to its industry peers and overall market trends.

        Your final report MUST expand on the summary provided
        but now including a clear assessment of the stock's
        financial standing, its strengths and weaknesses, 
        and how it fares against its competitors in the current
        market scenario.{self.__tip_section()}

        Make sure to use the most recent data possible.
        
        Also make sure to return the stock ticker.
      """),
                    agent=agent,
                    expected_output=dedent("""A comprehensive financial analysis report on Stock in question, covering key 
                                    financial metrics like P/E ratio, EPS growth, revenue trends, and debt-to-equity 
                                    ratio. The report should compare the stock's performance with industry peers and 
                                    market trends, highlighting strengths, weaknesses, and financial health. The 
                                    document must be data-driven, include visual aids like charts/graphs for 
                                    clarity, and be formatted as a PDF for executive review. Include the stock ticker""")

                    )

    def fundamental_analysis(self, agent):
        return Task(
            description=dedent(f"""
                Perform a thorough fundamental analysis of the specified company. 
                Delve into the company's financial statements, including income statements, 
                balance sheets, and cash flow statements. Analyze the management's discussion 
                and analysis (MD&A) sections for insights into the company's future outlook 
                and strategy. Review any recent news, market trends, and insider trading activities 
                that could indicate the company's financial health. Assess the company's valuation 
                metrics, such as P/E ratio, P/B ratio, dividend yield, and more, to understand its 
                market positioning and potential investment risks or opportunities.

                Your final deliverable should be a comprehensive report that encapsulates 
                all aspects of the company's financial fundamentals, offering clear, actionable 
                insights and recommendations based on your analysis. Highlight any potential red 
                flags or areas of opportunity that could influence investment decisions. 
                Ensure the report is well-structured, easy to understand, and includes the 
                company's stock ticker for reference.
            """),
            agent=agent,
            expected_output=dedent("""
                A detailed fundamental analysis report on the specified company, 
                covering an in-depth review of financial statements, management's 
                outlook, market trends, and valuation metrics. The report should 
                outline significant findings, potential risks, and opportunities, 
                providing actionable insights for investors. It should be presented 
                in a clear, structured format, ideally as a PDF, suitable for strategic 
                decision-making. The report must include the company's stock ticker.
            """)
        )

    def recommend(self, agent):
        return Task(description=dedent(f"""
        Review and synthesize the analyses provided by the
        Financial Analyst and the Research Analyst.
        Combine these insights to form a comprehensive
        investment recommendation. 
        
        You MUST Consider all aspects, including financial
        health, market sentiment, and qualitative data from
        Fundamentalist data.

        Make sure to include a section that shows insider 
        trading activity, and upcoming events like earnings.
        
        Also make sure to return the stock ticker.

        Your final answer MUST be a recommendation for your
        customer. It should be a full super detailed report, providing a 
        clear investment stance and strategy with supporting evidence.
        Make it pretty and well formatted for your customer.
        {self.__tip_section()}
      """),
                    agent=agent,
                    expected_output=dedent("""A final investment recommendation report synthesizing insights from 
                    financial and research analyses, including a review of financial health, market sentiment, 
                    and fundamentalist data. The report should provide a clear investment stance on the selected 
                    company, supported by evidence and analysis. It should cover upcoming earnings events, 
                    and present a strategic investment recommendation. The report must be well-formatted, 
                    visually appealing, and structured as a PDF to guide the client's investment decisions and must 
                    be written in Brazilian Portuguese""")

                    )

    def __tip_section(self):
        return (f"""If you do your BEST WORK, I'll give you a $10,000 commission!
        Current Year: {datetime.now().year} """)
