import imp
from django.urls import path, include
from .views import LatestCourseList,LatestModuleList

from course import viewsOLD

urlpatterns = [
    path('latest-lessons/',viewsOLD.LatestLessonList.as_view()),

    path('latest-cat/',viewsOLD.LatestCourseList.as_view()),

    path('latest-mod/',viewsOLD.LatestModuleList.as_view()),

    # path('<slug:course_slug>/',views.CourseDetail.as_view()),

    path('<slug:course_slug>/<slug:module_slug>/',viewsOLD.ModuleDetail.as_view()),

    path('<slug:course_slug>/<slug:module_slug>/<slug:lesson_slug>/',viewsOLD.LessonDetail.as_view()),
       
]