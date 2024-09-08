# Generated by Django 5.1.1 on 2024-09-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_remove_team_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='rank',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='team',
            unique_together={('player1', 'player2', 'group')},
        ),
    ]
