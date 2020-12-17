from django.db import models

class Empresa(models.Model):
	empresa=models.CharField('Empresa',max_length=250)
	logo=models.ImageField('Logo',null=True,blank=True,upload_to='logo/')

	def __str__(self):
		return self.empresa	


class Distrito(models.Model):
	distrito=models.CharField('Distrito',max_length=100)
	logo=models.ImageField('Logo',null=True,blank=True,upload_to='logo/')

	def __str__(self):
		return self.distrito


class Chofer(models.Model):
	nombre = models.CharField('Nombre', max_length=50)
	apellido = models.CharField('apellido', max_length=60)
	placa= models.CharField('Placa',max_length=10,primary_key=True)
	dni= models.CharField('Dni', max_length=10)
	civ = models.IntegerField('CIV')
	identificador=models.IntegerField('ID')
	foto=models.ImageField('Foto',null=True,blank=True,upload_to='fotos/')
	distrito=models.ForeignKey(Distrito,related_name='chofer_distrito',on_delete=models.CASCADE,null=True,blank=True)
	empresa=models.ForeignKey(Empresa,related_name='chofer_empresa',on_delete=models.CASCADE,null=True,blank=True)
	fecha_caducidad_licencia= models.DateField('Fecha de Caducidad',null=True,blank=True)


	def __str__(self):
		return self.apellido


