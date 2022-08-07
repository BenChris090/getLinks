# Generated by Django 4.1 on 2022-08-04 19:51

from django.db import migrations

def create_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User(f_name="Joe", m_name="Andre", l_name="Silver", email="joe@email.com", username="22342342", password="00000000").save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]

