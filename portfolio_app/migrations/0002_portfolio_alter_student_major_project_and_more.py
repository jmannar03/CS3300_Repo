# Generated by Django 4.2 on 2024-02-29 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('is_Active', models.BooleanField(default=False)),
                ('about', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('CSCI-BS', 'BS in Computer Science'), ('CPEN-BS', 'BS in Computer Engineering'), ('BIGD-BI', 'BI in Game Design and Development'), ('BICS-BI', 'BI in Computer Science'), ('BISC-BI', 'BI in Computer Security'), ('CSCI-BA', 'BA in Computer Science'), ('DASE-BS', 'BS in Data Analytics and Systems Engineering')], max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('portfolio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='portfolio', to='portfolio_app.portfolio'),
        ),
    ]
