"""stepik_hh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from headhunter.views import MainView, VacanciesView, CompanyView, VacancyView, custom404, custom503, custom500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('vacancies', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:specialization>', VacanciesView.as_view(), name='specialization'),
    path('companies/<int:company_id>', CompanyView.as_view(), name='company'),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view(), name='vacancy')
]

handler404 = custom404
handler500 = custom500
handler503 = custom503
