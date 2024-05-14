# Generated by Django 5.0.4 on 2024-05-12 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalAdministrativo',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numero_de_telefono', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
                ('correo_electronico', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=50)),
                ('fecha_contratacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('numero_telefonico', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
                ('correo_electronico', models.CharField(max_length=100)),
                ('c_usuario', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Informes',
            fields=[
                ('id_informe', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_y_hora', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=500)),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.personaladministrativo')),
            ],
        ),
        migrations.CreateModel(
            name='CooperativaTransporte',
            fields=[
                ('id_cooperativa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('informacion_contacto', models.CharField(max_length=100)),
                ('n_vehiculos', models.IntegerField()),
                ('color_vehiculo', models.CharField(max_length=100)),
                ('monto_a_cobrar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.personaladministrativo')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadTransporte',
            fields=[
                ('id_unidad', models.AutoField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=10)),
                ('detalles_de_ruta', models.CharField(max_length=150)),
                ('id_cooperativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.cooperativatransporte')),
            ],
        ),
        migrations.CreateModel(
            name='Rutas',
            fields=[
                ('id_rutas', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=150)),
                ('hora', models.TimeField()),
                ('id_cooperativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.cooperativatransporte')),
                ('id_unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.unidadtransporte')),
            ],
        ),
        migrations.AddField(
            model_name='personaladministrativo',
            name='id_unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.unidadtransporte'),
        ),
        migrations.CreateModel(
            name='Conductores',
            fields=[
                ('id_conductor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('numero_licencia', models.CharField(max_length=10)),
                ('informacion_contacto', models.CharField(max_length=100)),
                ('id_cooperativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.cooperativatransporte')),
                ('id_unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.unidadtransporte')),
            ],
        ),
        migrations.CreateModel(
            name='Tarjeta',
            fields=[
                ('id_tarjeta', models.AutoField(primary_key=True, serialize=False)),
                ('numero_tarjeta', models.BigIntegerField()),
                ('fecha_expiracion', models.DateField()),
                ('estado', models.CharField(max_length=10)),
                ('saldo_asociado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contraseña', models.CharField(max_length=20)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroAcceso',
            fields=[
                ('id_registro', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_de_acceso', models.CharField(max_length=10)),
                ('fecha_y_hora', models.DateTimeField()),
                ('direccion_ip', models.CharField(max_length=10)),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialTransacciones',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_y_hora', models.DateTimeField()),
                ('tipo', models.CharField(max_length=10)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.personaladministrativo')),
                ('id_tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.tarjeta')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioUnidadTransporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TransPorto.unidadtransporte')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_unidad_transporte', to='TransPorto.usuarios')),
            ],
        ),
    ]
