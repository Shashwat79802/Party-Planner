from crewai import Task
from textwrap import dedent
from datetime import date


class PartyTasks():


    def identify_party_task(self, agent, location, guest_list, theme):
      return Task(description=dedent(f"""
        Analyze and select the best venue for the party based 
        on specific criteria such as location, capacity, amenities,
        and cost. This task involves comparing multiple venues,
        considering factors like availability, suitability for the
        theme, and overall budget.
        
        Your final answer must be a detailed report on the chosen
        venue, including information about its features, pricing,
        and availability.
        {self.__tip_section()}

        Party Location: {location}
        Guest List: {guest_list}
        Party Theme: {theme}
      """),
                agent=agent)


    def plan_party_task(self, agent, location, theme, guests, date_range):
      return Task(description=dedent(f"""
        Expand the party guide into a detailed party itinerary
        with a schedule of activities, including setup time,
        entertainment slots, and food serving times. Include
        recommendations for party games, music playlists, and
        special surprises.
        
        Your final answer must be a complete party plan, formatted
        as markdown, encompassing all aspects of the party, from
        setup to cleanup, integrating the party guide information
        with practical party logistics.
        
        Be specific and give reasons why you chose each activity
        and how it contributes to creating the best party ever!
        {self.__tip_section()}

        Party Location: {location}
        Party Theme: {theme}
        Guest List: {guests}
        Date Range: {date_range}
      """),
                agent=agent)


    def __tip_section(self):
      return "If you do your BEST WORK, I'll tip you $100!"
