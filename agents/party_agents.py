from crewai import Agent
from langchain.llms import OpenAI
from supporting_tools.browser_tools import BrowserTools
from supporting_tools.calculator_tools import CalculatorTools
from supporting_tools.search_tools import SearchTools


class PartyAgents():


    def venue_selection_agent(self):
        return Agent(
                role='Venue Selection Expert',
                goal='Select the best venue based on location, capacity, and amenities',
                backstory=
                'An expert in analyzing party requirements to pick ideal venues',
                tools=[
                        SearchTools.search_internet,
                        # BrowserTools.scrape_and_summarize_website,
                ],
                verbose=True)


#     def entertainment_expert(self):
#         return Agent(
#                 role='Entertainment Expert',
#                 goal='Provide the BEST entertainment options for the party',
#                 backstory="""A knowledgeable expert with extensive information
#                 about various entertainment choices""",
#                 tools=[
#                         SearchTools.search_internet,
#                         BrowserTools.scrape_and_summarize_website,
#                 ],
#                 verbose=True)


    def party_planner(self):
        return Agent(
                role='Party Planner Extraordinaire',
                goal="""Create the most amazing party experience with theme, decorations, and activities""",
                backstory="""Specialist in party planning and logistics with 
                years of experience""",
                tools=[
                        SearchTools.search_internet,
                        # BrowserTools.scrape_and_summarize_website,
                        CalculatorTools.calculate,
                ],
                verbose=True)
