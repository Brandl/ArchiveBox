# Generated by Django 3.1.14 on 2024-01-24 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archiveboxdependency',
            options={'verbose_name': 'Internal Dependency: archivebox'},
        ),
        migrations.AlterModelOptions(
            name='djangodependency',
            options={'verbose_name': 'Internal Dependency: django'},
        ),
        migrations.AlterModelOptions(
            name='nodejsenvironmentdependency',
            options={'verbose_name': 'Shell Environment: node'},
        ),
        migrations.AlterModelOptions(
            name='pythonenvironmentdependency',
            options={'verbose_name': 'Shell Environment: python3'},
        ),
        migrations.AlterModelOptions(
            name='sqlitedependency',
            options={'verbose_name': 'Internal Dependency: sqlite3'},
        ),
    ]
