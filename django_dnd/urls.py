"""django_dnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework import routers
from apps.fifth_edition import views as fe_views

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    # Base admin site url
    url(r'^admin/', admin.site.urls),

    # fifth_edition
    url(r'^api/ability-scores$', fe_views.AbilityScoreViewGET.as_view()),
    url(r'^api/ability-scores/(?P<id>\d+)/spellcasting$', fe_views.SpellcastingViewGET.as_view()),
    url(r'^api/characters$', fe_views.CharacterViewGET.as_view()),
    url(r'^api/characters/create/$', fe_views.CharacterViewPOST.as_view()),
    url(r'^api/skills/create/$', fe_views.SkillsViewPOST.as_view()),
    url(r'^api/spellcasting/create/$', fe_views.SpellcastingViewPOST.as_view()),
]
