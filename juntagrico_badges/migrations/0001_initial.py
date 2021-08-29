# Generated by Django 3.1.7 on 2021-04-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('juntagrico', '0030_auto_20201112_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Eindeutiger Name des Abzeichens', max_length=100, unique=True, verbose_name='Name')),
                ('description', models.TextField(default='', max_length=1000, verbose_name='Beschreibung')),
                ('self_assignable', models.BooleanField(default=False, help_text='Erlaubt Mitglied sich das Abzeichen selbst zu geben', verbose_name='Selbstauszeichnung')),
                ('members', models.ManyToManyField(blank=True, related_name='badges', to='juntagrico.Member', verbose_name='Abzeichen')),
            ],
        ),
    ]
