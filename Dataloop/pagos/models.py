from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator 

from django.utils.translation import gettext_lazy as _

# Create your models here.

class recibo(models.Model):
    id               = models.AutoField(primary_key=True, null=False, blank=False)
    casa             = models.PositiveSmallIntegerField( null=False, blank=False)
    MESES =[
    (1,"Enero"),
    (2,"Febrero"),
    (3,"Marzo"),
    (4,"Abril"),
    (5,"Mayo"),
    (6,"Junio"),
    (7,"Julio"),
    (8,"Agosto"),
    (9,"Septiembre"),
    (10,"Octubre"),
    (11,"Noviembre"),
    (12,"Diciembre"),            
    ]
    mes              = models.SmallIntegerField(null=False, blank=False,choices=MESES)
    monto            = models.PositiveSmallIntegerField(null=False, blank=False,validators=[MinValueValidator(1)])
    fecha_pago       = models.DateField(auto_now_add=True)
class gasto(models.Model):
    id               = models.AutoField(primary_key=True, null=False, blank=False)
    concepto         = models.CharField(max_length=50, null=False, blank=False)
    fecha_aplicacion = models.DateField(null=False, blank=False)
    monto            = models.PositiveSmallIntegerField(null=False, blank=False,validators=[MinValueValidator(1)])
class Meta:    
    recibo.objects.order_by('casa', 'mes')
    gasto.objects.order_by('id','fecha_aplicacion')
