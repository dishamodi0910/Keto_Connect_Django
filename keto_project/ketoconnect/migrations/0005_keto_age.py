# Generated by Django 4.1.5 on 2023-02-25 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ketoconnect', '0004_meal_planner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keto_Age',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ketoconnect.user_detail')),
                ('current_age', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('experience_ketodiet', models.IntegerField()),
                ('number_of_meals', models.IntegerField()),
                ('number_of_snacks', models.IntegerField()),
                ('intermittent_fasting', models.BooleanField()),
                ('number_of_steps', models.IntegerField()),
                ('exercise_days', models.IntegerField()),
                ('isSmoker', models.BooleanField()),
                ('number_of_sleep_hours', models.FloatField()),
                ('waist_to_height_ratio', models.FloatField()),
                ('systolic_bp', models.IntegerField()),
                ('diastolic_bp', models.IntegerField()),
                ('oxygen_level', models.IntegerField()),
                ('hemoglobin', models.FloatField()),
            ],
        ),
    ]
