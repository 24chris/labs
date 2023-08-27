import imp
from django.urls import path, include
from course import views
from .views import LatestCourseList,CourseDetail,ModuleDetail,LessonDetail,AddComment


urlpatterns = [
    
    #Course
    path('latest-cat/',views.LatestCourseList.as_view()),
    path('<slug:course_slug>/',views.CourseDetail.as_view()),

    #Module
    path('all-modules/latest-mod/',views.LatestModuleList.as_view()),
    path('<slug:course_slug>/<slug:module_slug>/',views.ModuleDetail.as_view()),

    # Lesson
    path('all/lessons/latest-lessons/',views.LatestLessonList.as_view()),
    path('<slug:course_slug>/<slug:module_slug>/<slug:lesson_slug>/',views.LessonDetail.as_view()),


    #Comment - to sort
    #path('comment/<slug:lesson_slug>/',views.AddComment.as_view()),
         
       
]