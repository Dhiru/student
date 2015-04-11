from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.template.response import SimpleTemplateResponse
import json

from studentapp.models import *


class CreateAndGetStudent(View):
    def get(self, request):
        users_list = []
        result = dict()
        users = user_collection.find()
        for user in users:
            user_details = dict()
            user_details['name'] = user.name
            user_details['age'] = user.age
            user_details['class'] = user.student_class
            point = points_collection.find_one({"user_set._id": user._id})
            if point:
                user_details['behaviour_name'] = point.points['behaviour_name']
                user_details['points'] = point.points['points']
            users_list.append(user_details)
        success = True
        message = "Students list"
        result['users'] = users_list
        result['success'] = success
        result["message"] = message
        return HttpResponse(json.dumps(result))

    def post(self, request):
        name = request.POST.get('name', '')
        age = int(request.POST.get('age', ''))
        student_class = request.POST.get('class', '')
        result = dict()
        user = user_collection.collection.UserAccount()
        user.name = name
        user.age = age
        user.student_class = student_class
        user.save()
        success = True
        message = "Student added successfully"
        result['success'] = success
        result["message"] = message
        return HttpResponse(json.dumps(result))


class SetStudentPoints(View):
    def post(self, request):
        student = request.POST.get('student', '')
        behaviour = request.POST.get('behaviour', '')
        result = dict()
        user = user_collection.find_one({'_id': ObjectId(student)})
        today = datetime.datetime.now()
        if user:
            point = points_collection.find_one({'user_set._id': user._id})
            behaviour = behaviour_collection.find_one({'_id': ObjectId(behaviour)})
            attendence = attendence_collection.find_one({'user_set._id': user._id, 'date': today})
            if point:
                point.points = behaviour
                point.save()
            else:
                point = points_collection.collection.Points()
                point.user_set = user
                point.points = behaviour
                point.save()
            if not attendence:
                attendence = attendence_collection.collection.Attendence()
                attendence.user_set = user
                attendence.date = today
                attendence.save()
            success = True
            message = "Points set successfully"
        else:
            success = False
            message = "Student not found"
        result['success'] = success
        result["message"] = message
        return HttpResponse(json.dumps(result))


class GetStudentsAndBehaviours(View):
    def get(self, result):
        users = user_collection.find()
        behaviours = behaviour_collection.find()
        users_list = [{'id': str(user._id), 'name': user.name} for user in users]
        behaviours_list = [{'id': str(behaviour._id), 'name': behaviour.behaviour_name} for behaviour in behaviours]
        success = True
        message = "list of students and behaviours"
        result = dict()
        result['students'] = users_list
        result['behaviours'] = behaviours_list
        result['success'] = success
        result["message"] = message
        return HttpResponse(json.dumps(result))


class MainView(View):
    def get(self, request):
        return render(request, 'main.html')


class GetMainPage(View):
    def get(self, request):
        return SimpleTemplateResponse('MainContent.html')


