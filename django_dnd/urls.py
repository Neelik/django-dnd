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
    url(r'^api/ability-scores/put-delete/(?P<id>\d+)/$', fe_views.AbilityScoreViewPUT.as_view()),
    url(r'^api/ability-scores/(?P<id>\d+)/saves$', fe_views.SaveViewGET.as_view()),
    url(r'^api/ability-scores/(?P<id>\d+)/skills$', fe_views.SkillsViewGET.as_view()),
    url(r'^api/ability-scores/(?P<id>\d+)/spellcasting$', fe_views.SpellcastingViewGET.as_view()),
    url(r'^api/background$', fe_views.BackgroundViewGET.as_view()),
    url(r'^api/background/create/$', fe_views.BackgroundViewPOST.as_view()),
    url(r'^api/background/put-delete/(?P<id>\d+)/$', fe_views.BackgroundViewPUT.as_view()),
    url(r'^api/characters$', fe_views.CharacterViewGET.as_view()),
    url(r'^api/characters/create/$', fe_views.CharacterViewPOST.as_view()),
    url(r'^api/characters/put-delete/(?P<id>\d+)/$', fe_views.CharacterViewPUT.as_view()),
    url(r'^api/combat-info$', fe_views.CombatInfoViewGET.as_view()),
    url(r'^api/combat-info/create/$', fe_views.CombatInfoViewPOST.as_view()),
    url(r'^api/combat-info/put-delete/(?P<id>\d+)/$', fe_views.CombatInfoViewPUT.as_view()),
    url(r'^api/physical-attack/create/$', fe_views.PhysicalAttackViewPOST.as_view()),
    url(r'^api/physical-attack$', fe_views.PhysicalAttackViewGET.as_view()),
    url(r'^api/save/create/$', fe_views.SaveViewPOST.as_view()),
    url(r'^api/skills/create/$', fe_views.SkillsViewPOST.as_view()),
    url(r'^api/spellcasting/create/$', fe_views.SpellcastingViewPOST.as_view()),
]
