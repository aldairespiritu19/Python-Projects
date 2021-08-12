
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('courseNumber', models.IntegerField(default=0)),
                ('instructorName', models.CharField(max_length=90)),
                ('duration', models.FloatField(default=0.0)),
            ],
        ),
    ]