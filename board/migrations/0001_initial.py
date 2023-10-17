# Generated by Django 4.2.3 on 2023-10-16 16:02

import board.managers
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='phone number')),
                ('student_id', models.IntegerField(verbose_name='Студенческий ID')),
                ('grade', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0, 'Оценка не может быть меньше 0'), django.core.validators.MaxValueValidator(100, 'Оценка не может быть больше 100')], verbose_name='Оценка')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('is_verified', models.BooleanField(default=False, verbose_name='verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this student belongs to.', related_name='students', related_query_name='student', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this student.', related_name='students', related_query_name='student', to='auth.permission', verbose_name='User permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'unique_together': {('username', 'email', 'phone')},
            },
            managers=[
                ('objects', board.managers.UserManager()),
            ],
        ),
    ]
