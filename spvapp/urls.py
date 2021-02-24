from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.residents_list),
    path('occupantslist', views.occupants_list),
    path('stafflist', views.staff_list),
    path('residentsregistrationform', views.residents_form),
    path('occupantsregistrationform', views.occupants_form),
    path('staffregistrationform', views.staff_form)

]
