# Generated by Django 3.1.7 on 2021-04-10 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECEapp', '0022_auto_20210411_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='doamin',
            field=models.CharField(choices=[('MANAGERIAL', 'ANALYST'), ('IT', 'IT'), ('ECE-CORE', 'ECE-CORE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='people',
            name='year',
            field=models.IntegerField(choices=[(3, 'Third Year'), (5, 'M.TECH'), (1, 'First Year'), (6, 'PHD'), (2, 'Second Year'), (4, 'Final Year')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='projecttype',
            field=models.IntegerField(choices=[(8, 'Pre Print'), (5, 'Chapter'), (2, 'Article'), (7, 'Poster'), (9, 'Research Internship  Report'), (1, 'Thsesis'), (3, 'Publication'), (6, 'Patent'), (4, 'Conference Paper')], default=1),
        ),
    ]
