from django.urls import path
from.import views

urlpatterns=[ 
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('',views.view,name="view"),
    path("detailedview/<str:pk>",views.detailview,name="detailedview"),
    path('update/<str:pk>',views.update,name="update"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('welcome/',views.welcome,name="welcome"),
    path('userlog/',views.userlog,name="userlog"),
    path('logoutuser/',views.logoutuser,name="logoutuser")
]