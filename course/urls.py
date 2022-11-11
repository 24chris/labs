import imp
from django.urls import path, include
from .views import LatestCourseList,LatestModuleList

from course import views

urlpatterns = [
    path('latest-lessons/',views.LatestLessonList.as_view()),

    path('latest-cat/',views.LatestCourseList.as_view()),

    path('latest-mod/',views.LatestModuleList.as_view()),

    # path('<slug:course_slug>/',views.CourseDetail.as_view()),

    path('<slug:course_slug>/<slug:module_slug>/',views.ModuleDetail.as_view()),

    path('<slug:course_slug>/<slug:module_slug>/<slug:lesson_slug>/',views.LessonDetail.as_view()),
       
]