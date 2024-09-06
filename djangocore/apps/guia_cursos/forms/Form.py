# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext_lazy as _
import datetime
from djangocore.apps.guia_cursos.models.Model import *

#from djangocore.apps.flavio.models.Model import *

class CursosForm(forms.ModelForm):
    class Meta:
        model = CursosModel
        fields = ('nome_curso', 'apelido_curso', 'ead_curso', 'descritivo_curso', 'area_atuacao_curso',
                  'pre_requisito_curso', 'nivel_curso', 'campus_curso')
        widgets = {
            'nome_curso': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'apelido_curso': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'ead_curso': forms.Select(attrs={'class': 'form-control'}),
            'descritivo_curso': forms.TextInput(attrs={'class': 'form-control', 'size': '600'}),
            'area_atuacao_curso': forms.TextInput(attrs={'class': 'form-control', 'size': '600'}),
            'pre_requisito_curso': forms.TextInput(attrs={'class': 'form-control', 'size': '600'}),
            'nivel_curso': forms.Select(attrs={'class': 'form-control select-produto'}),
            'campus_curso': forms.Select(attrs={'class': 'form-control select-produto'}),
        }
        labels = {
            'nome_curso': _('Nome'),
            'apelido_curso': _('Apelido'),
            'ead_curso': _('EaD'),
            'descritivo_curso': _('Descritivo'),
            'area_atuacao_curso': _('Área de Atuação'),
            'pre_requisito_curso': _('Pré-requisito'),
            'nivel_curso': _('Nível'),
            'campus_curso': _('Câmpus'),
        }


class NivelCursoForm(forms.ModelForm):
    class Meta:
        model = NivelCursoModel
        fields = ('nome_nivelcurso', 'descricao_nivelcurso')
        widgets = {
            'nome_nivelcurso': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'descricao_nivelcurso': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
        }
        labels = {
            'nome_nivelcurso': _('Nome'),
            'descricao_nivelcurso': _('Descrição'),
        }


class CampusForm(forms.ModelForm):
    class Meta:
        model = CampusModel
        fields = ('nome_campus', 'sigla_campus', 'status_campus')
        widgets = {
            'nome_campus': forms.TextInput(attrs={'class': 'form-control', 'size': '200'}),
            'sigla_campus': forms.TextInput(attrs={'class': 'form-control', 'size': '50'}),
            'status_campus': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome_campus': _('Nome'),
            'sigla_campus': _('Sigla'),
            'status_campus': _('Ativado/Desativado'),
        }

