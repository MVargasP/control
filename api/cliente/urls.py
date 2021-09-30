from django.urls import path, include


from .vistas import InsertClienteAPI

urlpatterns = [


    path('importar', InsertClienteAPI.as_view()),



  #  path('listar', Usuario.as_view())
]