"""
URL configuration for JobHunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ui import views as ui_views
from candidate import views as cand_views
urlpatterns = [
    path('', ui_views.homepage),
    path('session_save/personal', cand_views.save_personal_in_session),
    path('session_save/edu', cand_views.save_edu_in_session),
    path('session_save/exp', cand_views.save_exp_in_session),
    path('session/get_data', cand_views.get_session_data),
    path('session/delete', cand_views.delete_session),
    path('db/create', cand_views.db_insert),
]
