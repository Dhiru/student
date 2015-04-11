from django.conf.urls import patterns, include, url
from tastypie.api import Api
from studentapp.views import *
from studentapp.app import *

from django.contrib import admin
admin.autodiscover()

useraccount_resource = UserAccountResource()

v1_api = Api(api_name='v1')
v1_api.register(UserAccountResource())
v1_api.register(AttendenceResource())
v1_api.register(BehaviourResource())
v1_api.register(PointsResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'student.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainView.as_view(), name="main"),
    url(r'^students/$', CreateAndGetStudent.as_view(), name="students"),
    url(r'^addstudent/$', CreateAndGetStudent.as_view(), name="add_student"),
    url(r'^givepoints/$', SetStudentPoints.as_view(), name="give_points"),
    url(r'^getstudentsandbehaviours/$', GetStudentsAndBehaviours.as_view(), name="students_behaviours"),
    url(r'^mainpage/$', GetMainPage.as_view(), name="main_page"),
    url(r'^api/', include(v1_api.urls)),
)
