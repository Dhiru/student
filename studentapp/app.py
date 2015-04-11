from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import Authorization
from tastypie_mongodb.resources import MongoDBResource
from studentapp.models import *


class UserAccountResource(MongoDBResource):

    id = fields.CharField(attribute="_id")
    name = fields.CharField(attribute="name", null=True)
    age = fields.IntegerField(attribute="age", null=True)
    student_class = fields.CharField(attribute="student_class", null=True)

    class Meta:
        queryset = user_collection.find()
        resource_name = "useraccount"
        list_allowed_methods = ["delete", "get", "post"]
        authorization = Authorization()
        object_class = UserAccount
        collection = UserAccount.collection_name # collection name

    def get_collection(self):
        return user_collection


class AttendenceResource(MongoDBResource):
    id = fields.CharField(attribute="_id")
    user = fields.ToOneField(UserAccountResource, 'user')
    class Meta:
        queryset = attendence_collection.find()
        resource_name = 'attendence'
        list_allowed_methods = ["delete", "get", "post"]
        authorization = Authorization()
        object_class = Attendence

    def get_collection(self):
        return attendence_collection


class BehaviourResource(MongoDBResource):
    id = fields.CharField(attribute="_id")
    behaviour_name = fields.CharField(attribute="behaviour_name", null=True)
    points = fields.IntegerField(attribute="points", null=True)
    class Meta:
        queryset = behaviour_collection.find()
        resource_name = 'behaviour'
        list_allowed_methods = ["delete", "get", "post"]
        authorization = Authorization()
        object_class = Behaviour

    def get_collection(self):
        return behaviour_collection


class PointsResource(MongoDBResource):
    id = fields.CharField(attribute="_id")
    user = fields.ToOneField(UserAccountResource, 'useraccount')
    behaviour = fields.ToOneField(BehaviourResource, 'behaviour')
    class Meta:
        queryset = points_collection.find()
        resource_name = 'points'
        list_allowed_methods = ["delete", "get", "post"]
        authorization = Authorization()
        object_class = Points

    def get_collection(self):
        return points_collection
