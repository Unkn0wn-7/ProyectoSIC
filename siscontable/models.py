from datetime import date
from django.db import models


# modelo cuentas
class Cuenta(models.Model):
    codigo=models.CharField(max_length=4, null=False, primary_key=True)
    tipo=models.CharField(max_length=20)
    nombre=models.CharField(max_length=50)
    totalDebe=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    totalHaber=models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.codigo,self.nombre)
    
    class Meta:
        db_table = 'cuentas'

# modelo transacciones
class Transaccion(models.Model):
    fecha=models.DateField(default=date.today)
    concepto=models.CharField(max_length=20)
    nomCuenta=models.CharField(max_length=50)
    monto=models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return self.concepto
    
    class Meta:
        db_table = 'transaccion'
