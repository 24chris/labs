# import imp
# from django.urls import path, include
# from .viewsOLD import LatestCourseList,ModuleSerializer,LessonSerializer,LatestLessonList,EnrollToCourse,EnrollChosen,CourseStudy,CourseDetail,AddComment

# from course import viewsOLD

# urlpatterns = [
    
#     #Course
#     path('latest-cat/',viewsOLD.LatestCourseList.as_view()),
#     path('choose-course/',viewsOLD.EnrollChosen.as_view()),
#     # path('<slug:course_slug>/',views.CourseDetail.as_view()),

#     #Check if course is ready to be studied or not
#     path('course-study/',viewsOLD.CourseStudy.as_view()),
    

#     #Module
#     # path('latest-mod/',views.LatestModuleList.as_view()),
#     path('<slug:course_slug>/<slug:module_slug>/',viewsOLD.ModuleDetail.as_view()),

#     #Lesson
#     path('<slug:course_slug>/<slug:module_slug>/<slug:lesson_slug>/',viewsOLD.LessonDetail.as_view()),
#     path('latest-lessons/',viewsOLD.LatestLessonList.as_view()),

#     #enroll
#     # path("enroll/", views.enroll, name="enroll"),
#     # path("dashboard",views.Dashboard.as_view()),
#     path("enroll-user/",viewsOLD.EnrollToCourse.as_view()),

#     # Comments
#     path("comment/<slug:course_slug>/",viewsOLD.AddComment.as_view()),


#     # path('latest-mod/',views.LatestModuleList.as_view()),

#     # path('<slug:course_slug>/',CourseDetail.as_view()),
   
       
# ]