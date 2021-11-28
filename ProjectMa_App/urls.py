from django.urls import path
from ProjectMa_App import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path("login",views.LoginView.as_view(),name="login"),
    path("register",views.SignUpView.as_view(),name="register"),
    path("confirmation",views.ConfirmationView.as_view(),name="Confirmation"),
    path("Project_Dashboard",views.ProjectDashboardView.as_view(),name="Dashboard"),
    path("Group-Details",views.GroupFormView.as_view(),name="GroupDetailsForm"),
    path('Project-Form',views.ProjectFormView.as_view(),name="ProjectForm"),
    path("Project-Report&PPT",views.ProjectReportPPTFormView.as_view(),name="ReportForm"),
    #path('view',views.vview)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


