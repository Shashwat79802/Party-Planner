from crewai import Crew
from textwrap import dedent
from agents.party_agents import PartyAgents
from agents.party_tasks import PartyTasks

from dotenv import load_dotenv
load_dotenv()

class PartyCrew:

  def __init__(self, location, guests, date_range, theme):
    self.location = location
    self.guests = guests
    self.date_range = date_range
    self.theme = theme

  def run(self):
    agents = PartyAgents()
    tasks = PartyTasks()

    venue_selector_agent = agents.venue_selection_agent()
    party_planner_agent = agents.party_planner()
    # entertainment_agent = agents.entertainment_expert()

    identify_task = tasks.identify_party_task(
      venue_selector_agent,
      self.location,
      self.guests,
      self.theme,
    )
    plan_task = tasks.plan_party_task(
      party_planner_agent,
      self.location,
      self.guests,
      self.theme,
      self.date_range
    )
    # entertainment_task = tasks.gather_party_task(
    #   entertainment_agent,
    #   self.location,
    #   self.guests,
    #   self.theme,
    #   self.date_range
    # )

    crew = Crew(
      agents=[
        venue_selector_agent, party_planner_agent
      ],
      tasks=[identify_task, plan_task],
      verbose=True
    )

    result = crew.kickoff()
    return result

if __name__ == "__main__":
  print("## Welcome to Party Planner Crew")
  print('-------------------------------')
  location = input(
    dedent("""
      Where will the party be held?
    """))
  guests = input(
    dedent("""
      How many guests are you expecting?
    """))
  date_range = input(
    dedent("""
      What is the date range for the party?
    """))
  theme = input(
    dedent("""
      What is the theme of the party?
    """))
  
  party_crew = PartyCrew(location, guests, date_range, theme)
  result = party_crew.run()
  print("\n\n########################")
  print("## Here is your Party Plan")
  print("########################\n")
  print(result)
