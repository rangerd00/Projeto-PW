from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include # new

app_name = 'portfolio'
name = "home"

urlpatterns = [
    path('', views.home_view),
    path('home', views.home_view, name='home'),
    path('formacao', views.formacao_view, name='formacao'),
    path('educacao', views.educacao_view, name='educacao'),
    path('projetos', views.projetos_view, name='projetos'),
    path('licenciatura', views.licenciatura_view, name='licenciatura'),
    path('blog', views.blog_view, name='blog'),
    path('web', views.web_view, name='web'),
    path('login', views.login_view, name='login'),
    path('novo', views.nova_post_view, name='novo'),
    path('edita/<int:blog_post_id>', views.edita_post_view, name='edita'),
    path('apaga/<int:blog_post_id>', views.apaga_post_view, name='apaga'),
    path('quizz', views.quizz_view, name='quizz'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('trabalhos', views.projetos_view, name='trabalhos'),
    path('novotfc', views.nova_tfc_view, name='novotfc'),





]
