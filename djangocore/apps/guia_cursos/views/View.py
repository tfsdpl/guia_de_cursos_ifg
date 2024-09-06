# -*- coding: utf-8 -*-

from django.urls import reverse_lazy
from djangocore.apps.base.custom_views import CustomCreateView, CustomListView, CustomUpdateView
from djangocore.apps.guia_cursos.forms.Form import *
from djangocore.apps.guia_cursos.models.Model import *




class SiteHomeView(CustomListView):
    template_name = 'site/index.html'
    model = CampusModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('guia_cursos:listacursos')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(SiteHomeView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Cursos'
        context['add_url'] = reverse_lazy('guia_cursos:adicionacursos')
        return context



### Cursos ###
class ListCursosView(CustomListView):
    template_name = 'guia_cursos/list.html'  #'exemplo/exemplo_operacao/list.html'
    model = CursosModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('guia_cursos:listacursos')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListCursosView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Cursos'
        context['add_url'] = reverse_lazy('guia_cursos:adicionacursos')
        return context


class AdicionarCursosView(CustomCreateView):
    form_class = CursosForm
    template_name = 'guia_cursos/add.html'  #"exemplo/exemplo_operacao/add.html"
    success_url = reverse_lazy('guia_cursos:listacursos')
    success_message = "Adicionar Exemplo <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCursosView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR CURSO'
        context['return_url'] = reverse_lazy('guia_cursos:listacursos')
        return context


class EditarCursosView(CustomUpdateView):
    form_class = CursosForm
    model = CursosModel
   # template_name = "fiscal/natureza_operacao/natureza_operacao_edit.html"
    template_name = 'guia_cursos/edit.html'  #"exemplo/exemplo_operacao/edit.html"
    success_url = reverse_lazy('guia_cursos:listacursos')
    success_message = "Natureza da operação <b>%(cfop)s </b>editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarCursosView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'guia_cursos:listacursos')
        return context




### Nível Cursos ###
class ListNivelCursoView(CustomListView):
    template_name = 'guia_cursos/list_nivel_curso.html'
    model = NivelCursoModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('guia_cursos:lista_nivel_curso')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListNivelCursoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Nível de Cursos'
        context['add_url'] = reverse_lazy('guia_cursos:adiciona_nivel_curso')
        return context


class AdicionarNivelCursoView(CustomCreateView):
    form_class = NivelCursoForm
    template_name = 'guia_cursos/add.html'
    success_url = reverse_lazy('guia_cursos:lista_nivel_curso')
    success_message = "Adicionar Nível de Curso <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarNivelCursoView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR NÍVEL DE CURSO'
        context['return_url'] = reverse_lazy('guia_cursos:lista_nivel_curso')
        return context


class EditarNivelCursoView(CustomUpdateView):
    form_class = NivelCursoForm
    model = NivelCursoModel
    template_name = 'guia_cursos/edit.html'
    success_url = reverse_lazy('guia_cursos:lista_nivel_curso')
    success_message = "Natureza da operação <b>%(cfop)s </b>editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarNivelCursoView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'guia_cursos:lista_nivel_curso')
        return context




### Câmpus ###
class ListCampusView(CustomListView):
    template_name = 'guia_cursos/list_campus.html'
    model = CampusModel
    context_object_name = 'all_natops'
    success_url = reverse_lazy('guia_cursos:lista_campus')
    permission_codename = 'view_naturezaoperacao'

    def get_context_data(self, **kwargs):
        context = super(ListCampusView, self).get_context_data(**kwargs)
        context['title_complete'] = 'Câmpus'
        context['add_url'] = reverse_lazy('guia_cursos:adiciona_campus')
        return context


class AdicionarCampusView(CustomCreateView):
    form_class = CampusForm
    template_name = 'guia_cursos/add.html'
    success_url = reverse_lazy('guia_cursos:lista_campus')
    success_message = "Adicionar Câmpus <b>%(cfop)s </b>adicionado com sucesso."
    permission_codename = 'add_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(AdicionarCampusView, self).get_context_data(**kwargs)
        context['title_complete'] = 'ADICIONAR CÂMPUS'
        context['return_url'] = reverse_lazy('guia_cursos:lista_campus')
        return context


class EditarCampusView(CustomUpdateView):
    form_class = CampusForm
    model = CampusModel
    template_name = 'guia_cursos/edit.html'
    success_url = reverse_lazy('guia_cursos:lista_campus')
    success_message = "Natureza da operação <b>%(cfop)s </b>editada com sucesso."
    permission_codename = 'change_naturezaoperacao'

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, cfop=self.object.cfop)

    def get_context_data(self, **kwargs):
        context = super(EditarCampusView,
                        self).get_context_data(**kwargs)
        context['return_url'] = reverse_lazy(
            'guia_cursos:lista_campus')
        return context

