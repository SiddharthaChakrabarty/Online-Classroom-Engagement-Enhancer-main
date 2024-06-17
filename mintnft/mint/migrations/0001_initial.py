# Generated by Django 4.0.4 on 2024-04-20 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=200)),
                ('student_cgpa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('student_wallet', models.CharField(max_length=200)),
                ('certificate_url', models.URLField(max_length=1000)),
            ],
        ),
    ]
