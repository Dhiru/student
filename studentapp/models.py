from django.db import models
from django_mongokit import connection
from django_mongokit import get_database
from django_mongokit.document import DjangoDocument
import datetime
try:
    from bson import ObjectId
except ImportError:  # old pymongo
    from pymongo.objectid import ObjectId

db = get_database()

@connection.register
class UserAccount(DjangoDocument):
    '''
        Models for User Account which store students
        Name, Age, Student_class.
    '''
    objects = models.Manager()
    collection_name = 'useraccount'
    structure = {
        'name': unicode,
        'age': int,
        'student_class': unicode
    }
    use_dot_notation = True

@connection.register
class Attendence(DjangoDocument):
    '''
        Models for Attendence which store UserAccount attendence
    '''
    objects = models.Manager()
    collection_name = 'attendence'
    structure = {
        'user_set': UserAccount,
        'date': datetime.datetime,
    }
    use_dot_notation = True

    
@connection.register
class Behaviour(DjangoDocument):
    '''
        Models for Behaviour structure which content behaviour title with contains points
    '''
    objects = models.Manager()
    collection_name = 'behaviour'
    structure = {
        'behaviour_name': unicode,
        'points': int,
    }
    use_dot_notation = True
    

@connection.register
class Points(DjangoDocument):
    '''
        Records points for UserAccount.
    '''    
    objects = models.Manager()
    collection_name = 'points'
    structure = {
        'user_set': UserAccount,
        'points': Behaviour,
    }
    use_dot_notation = True


# DATABASE Variables
user_collection = db[UserAccount.collection_name].UserAccount
attendence_collection = db[Attendence.collection_name].Attendence
behaviour_collection = db[Behaviour.collection_name].Behaviour
points_collection = db[Points.collection_name].Points


    


