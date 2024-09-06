from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    # login/
    url(r'^$', views.UserFormView.as_view(), name='loginview'),

    # login/registrar/
    url(r'registrar/$', views.UserRegistrationFormView.as_view(),
        name='registrarview'),

    # login/esqueceu/:
    url(r'^esqueceu/$', views.ForgotPasswordView.as_view(), name='esqueceuview'),

    #SolicitarAcessoiew
    url(r'^solicitaracesso/$', views.SolicitarAcessoView.as_view(), name='solicitaracessoview'),

    url(r'^editarsenha/$', views.PasswordResetConfirmView.as_view(), name='editarsenha'),

    # login/trocarsenha/:
    url(r'^trocarsenha/$',
        views.TrocarSenhaView.as_view(), name='trocarsenhaview'),

    url(r'^changepassword/', views.ChangePasswordView.as_view(), name='change_password'),

    # logout
    url(r'^logout/$', views.UserLogoutView.as_view(), name='logoutview'),

    # login/perfil/
    url(r'^perfil/$', views.MeuPerfilView.as_view(), name='perfilview'),

    # login/editarperfil/
    url(r'^editarperfil/$', views.EditarPerfilView.as_view(), name='editarperfilview'),

    # login/usuarios/
    url(r'^usuarios/$', views.UsuariosListView.as_view(), name='usuariosview'),

    # login/usuarios/(id_usuario)
    url(r'usuarios/(?P<pk>[0-9]+)/$',
        views.UsuarioDetailView.as_view(), name='usuariodetailview'),

    # deletar usuario
    url(r'deletaruser/(?P<pk>[0-9]+)/$',
        views.DeletarUsuarioView.as_view(), name='deletarusuarioview'),

    # permissoes usuario
    url(r'permissoesusuario/(?P<pk>[0-9]+)/$',
        views.EditarPermissoesUsuarioView.as_view(), name='permissoesusuarioview'),


]
