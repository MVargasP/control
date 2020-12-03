from django.contrib import admin
from .models import Distrito,Empresa,Chofer
from import_export.admin import ImportExportModelAdmin

from import_export import resources,fields,widgets
from import_export.widgets import ForeignKeyWidget


class ChoferResource(resources.ModelResource):
    distrito=fields.Field(column_name='distrito',attribute='distrito',widget=ForeignKeyWidget(Distrito,'distrito'))
    empresa=fields.Field(column_name='empresa',attribute='empresa',widget=ForeignKeyWidget(Empresa,'empresa'))
  
    def before_import_row(self, row, **kwargs):
         distrito  = row.get('distrito')
         empresa  = row.get('empresa')

         (doc,_created)=Distrito.objects.get_or_create(distrito=distrito)
         (tra,_created)=Empresa.objects.get_or_create(empresa=empresa)

         
         row['distrito'] = doc.distrito
         row['empresa'] = tra.empresa

         
    class Meta:
        model = Chofer
        fields=('distrito','nombre','apellido','placa','empresa',
        'dni','civ','identificador') # campos que se import-export
        export_order = ['distrito','nombre','apellido','placa','empresa',
        'dni','civ','identificador']
        import_id_fields = ['placa'] # import busca un id por default especificar que campo utilizare como id si cambio el pk

class ChoferAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('distrito','nombre','apellido','placa','empresa',
        'dni','civ','identificador') # campos que se mostraran
	search_fields = ['nombre','apellido','placa','dni'] # busqueda de campos
	resource_class = ChoferResource 


admin.site.register(Distrito)
admin.site.register(Empresa)
admin.site.register(Chofer,ChoferAdmin)