# Generated by Django 3.2.4 on 2022-06-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_classnotes_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classnotes',
            name='note',
            field=models.FileField(upload_to='notes'),
        ),
    ]
