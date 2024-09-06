# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

app_name = 'guia_cursos'
urlpatterns = [
    # Cursos #
    url(r'guia_cursos/lista/$', views.ListCursosView.as_view(), name='listacursos'),
    url(r'guia_cursos/adicionar/$', views.AdicionarCursosView.as_view(), name='adicionacursos'),
    url(r'guia_cursos/editar/(?P<pk>[0-9]+)/$', views.EditarCursosView.as_view(), name='editacursos'),

    # Nivel Cursos #
    url(r'guia_cursos/lista_nivel_curso/$', views.ListNivelCursoView.as_view(), name='lista_nivel_curso'),
    url(r'guia_cursos/adicionar_nivel_curso/$', views.AdicionarNivelCursoView.as_view(), name='adiciona_nivel_curso'),
    url(r'guia_cursos/editar_nivel_curso/(?P<pk>[0-9]+)/$', views.EditarNivelCursoView.as_view(), name='edita_nivel_curso'),

    # Câmpus #
    url(r'guia_cursos/lista_campus/$', views.ListCampusView.as_view(), name='lista_campus'),
    url(r'guia_cursos/adicionar_campus/$', views.AdicionarCampusView.as_view(), name='adiciona_campus'),
    url(r'guia_cursos/editar_campus/(?P<pk>[0-9]+)/$', views.EditarCampusView.as_view(), name='edita_campus'),

    url(r'site/home/$', views.SiteHomeView.as_view(), name='sitehome'),

]
