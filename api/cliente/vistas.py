from rest_framework import generics, permissions
from rest_framework.response import Response
import pandas as pd
import re
import numpy as np
import json
from tqdm import tqdm
from .serializer import ClienteSerializer
from cliente.models import Chofer,Distrito,Empresa

class InsertClienteAPI(generics.GenericAPIView):
    #permission_classes = [  permissions.IsAuthenticated ]
    serializer_class = ClienteSerializer

    def post(self, request):   
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)     
        file_uploaded = request.FILES.get('documento')
        content_type = file_uploaded.content_type
        df = pd.read_excel(file_uploaded,converters={'co_alumno':str,'nro_docum':str,'flota':str} )
    
        fecha=serializer.data['fecha_inicio_tarjeta']
        distrito=1
        fecha_fin_tarjeta=serializer.data['fecha_fin_tarjeta']
       
        try:
            distrito=Distrito.objects.get(distrito=distrito)                    
        except Exception as e:
            distrito=Distrito.objects.create(distrito="LOS OLIVOS")  

        df = df.to_dict('records')
        lista_chofer = []
        

        for row in tqdm(df):
            try:
                empresa=Empresa.objects.get(empresa=row['empresa'])
                
            except Exception as e:
                  
                empresa=Empresa.objects.create(empresa=row['empresa'])

            chofer=Chofer(
                dni=row['nro_docum'],
                apellido=row['ap_alumno'],
                nombre=row['no_alumno'],
                foto=f"fotos/{row['nro_docum']}.jpg",
                placa=row['placa'],
                civ=row['flota'],
                fecha_inicio_licencia=fecha,
                fecha_caducidad_licencia=fecha_fin_tarjeta,
                empresa=empresa
                ) 
            lista_chofer.append(chofer)

        Chofer.objects.bulk_create(lista_chofer, ignore_conflicts = True)
        

        print(Chofer.objects.all())
        return Response({"estado":"ok"})
   