from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    numero_telefonico = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=100)
    c_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class CooperativaTransporte(models.Model):
    id_cooperativa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    informacion_contacto = models.CharField(max_length=100)
    id_empleado = models.ForeignKey('PersonalAdministrativo', on_delete=models.CASCADE)
    n_vehiculos = models.IntegerField()
    color_vehiculo = models.CharField(max_length=100)
    monto_a_cobrar = models.DecimalField(max_digits=10, decimal_places=2)
    

class Informes(models.Model):
    id_informe = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey('PersonalAdministrativo', on_delete=models.CASCADE)
    fecha_y_hora = models.DateTimeField()
    descripcion = models.CharField(max_length=500)

class Rutas(models.Model):
    id_rutas = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    hora = models.TimeField()
    id_unidad = models.ForeignKey('UnidadTransporte', on_delete=models.CASCADE)
    id_cooperativa = models.ForeignKey('CooperativaTransporte', on_delete=models.CASCADE)

class PersonalAdministrativo(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=10)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    correo_electronico = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    id_unidad = models.ForeignKey('UnidadTransporte', on_delete=models.CASCADE)

class UnidadTransporte(models.Model):
    id_unidad = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=10)
    detalles_de_ruta = models.CharField(max_length=150)
    id_cooperativa = models.ForeignKey('CooperativaTransporte', on_delete=models.CASCADE)

class Conductores(models.Model):
    id_conductor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    numero_licencia = models.CharField(max_length=10)
    id_cooperativa = models.ForeignKey('CooperativaTransporte', on_delete=models.CASCADE)
    informacion_contacto = models.CharField(max_length=100)
    id_unidad = models.ForeignKey('UnidadTransporte', on_delete=models.CASCADE)


class HistorialTransacciones(models.Model):
    id_historial = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    id_tarjeta = models.ForeignKey('Tarjeta', on_delete=models.CASCADE)
    fecha_y_hora = models.DateTimeField()
    tipo = models.CharField(max_length=10)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    id_empleado = models.ForeignKey('PersonalAdministrativo', on_delete=models.CASCADE)

class RegistroAcceso(models.Model):
    id_registro = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    tipo_de_acceso = models.CharField(max_length=10)
    fecha_y_hora = models.DateTimeField()
    direccion_ip = models.CharField(max_length=10)

class Tarjeta(models.Model):
    id_tarjeta = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    numero_tarjeta = models.BigIntegerField()
    fecha_expiracion = models.DateField()
    estado = models.CharField(max_length=10)
    saldo_asociado = models.DecimalField(max_digits=10, decimal_places=2)
    contraseña = models.CharField(max_length=20)



