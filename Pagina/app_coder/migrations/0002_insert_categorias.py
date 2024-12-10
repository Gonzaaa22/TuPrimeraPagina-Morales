from django.db import migrations

def create_categorias(apps, schema_editor):
    Categoria = apps.get_model('app_coder', 'Categoria')
    Categoria.objects.create(nombre='Bebidas')
    Categoria.objects.create(nombre='Comida')
    Categoria.objects.create(nombre='Objetos')

class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_categorias),
    ]
