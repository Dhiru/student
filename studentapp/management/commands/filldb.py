''' imports from installed packages '''
from django.core.management.base import BaseCommand, CommandError

''' imports from application folders/files '''
from studentapp.models import behaviour_collection


class Command(BaseCommand):
    help = "This performs activities required for setting up default structure or updating it."
    
    def __init__(self):
        super(Command, self).__init__()
        self.default_behaviours = [
            {'behaviour_name': u'Doing homework','points': 3},
            {'behaviour_name': u'Disrupting class','points': -2},
            {'behaviour_name': u'helping','points': 5},
        ]

    def handle(self, *args, **options):
        behaviours = behaviour_collection.find_one()
        if not behaviours:
            map(self.create_behaviour, self.default_behaviours)
                
    def create_behaviour(self, default_behaviour):
        behaviour = behaviour_collection.collection.Behaviour()
        behaviour.behaviour_name = default_behaviour['behaviour_name']
        behaviour.points = default_behaviour['points']
        behaviour.save()
        print "created ", behaviour.behaviour_name, " behaviour"
        
            
        
