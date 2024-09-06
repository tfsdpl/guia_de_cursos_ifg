from django.db import models
from django.utils.translation import gettext_lazy as _


class NivelCursoModel(models.Model):
    nome_nivelcurso = models.CharField(max_length=200)
    descricao_nivelcurso = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_nivelcurso

CHOICES_ATIVADO_DESATIVADO = (
        (True, _('Ativado')),
        (False, _('Desativado'))
    )
class CampusModel(models.Model):
    nome_campus = models.CharField(max_length=200)
    sigla_campus = models.CharField(max_length=50)
    status_campus = models.BooleanField(default=True, choices=CHOICES_ATIVADO_DESATIVADO)

    # posicao_x_mapa_campus = models.IntegerField()
    # posicao_y_mapa_campus = models.IntegerField()

    def __str__(self):
        return self.nome_campus


CHOICES_SIM_NAO = (
        (True, _('Sim')),
        (False, _('Não'))
    )
class CursosModel(models.Model):
    nome_curso = models.CharField(max_length=200)
    apelido_curso = models.CharField(max_length=200)
    ead_curso = models.BooleanField(default=False, choices=CHOICES_SIM_NAO)
    descritivo_curso = models.CharField(max_length=600)
    area_atuacao_curso = models.CharField(max_length=600)
    pre_requisito_curso = models.CharField(max_length=600)
    ### imagem_curso = models.FileField(null=True,max_length=100)
    nivel_curso = models.ForeignKey(NivelCursoModel, related_name="nivelcurso_curso", on_delete=models.CASCADE)
    campus_curso = models.ForeignKey(CampusModel, related_name="campus_curso", on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_curso
