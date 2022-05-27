# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSportDescription(Action):

    def name(self) -> Text:
        return "action_sport_description"
         

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
            entities = tracker.latest_message["entities"]
             
            for entity in entities:
                if(entity["entity"]=="game"):
             	    game = entity["value"]

                if(entity["entity"]=="material_type"):
                    material_type = entity["value"]

            if game == "Athletics":
             	if material_type == "explanation":
             		dispatcher.utter_message(text="https://www.sportzcraazy.com/athletics-games")
                    
            if game == "Water sports":
                if material_type == "explanation":
                    dispatcher.utter_message(text="https://nomadparadise.com/water-sports")
                
            if game == "Combat sports":
                if material_type == "explanation":
                    dispatcher.utter_message(text="https://www.rookieroad.com/sports-lists/list-of-combat-sports-a-z")

            if game == "Ball sports":
                if material_type == "explanation":
                    dispatcher.utter_message(text="https://englishstudyonline.org/sports-balls")

            if game == "Board sports":
                if material_type == "explanation":
                    dispatcher.utter_message(text="https://thegromlife.com/surfing/a-complete-list-of-board-sports-water-street-and-snow")
            return []
