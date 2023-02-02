# Generated by Django 2.2.16 on 2022-11-17 01:34

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'Пользователь с таким именем уже существует'}, help_text='Обязательное поле. Не более 30 символов. Допускаются только буквы латинского алфавита, цифры и символы @ . + - _', max_length=150, unique=True, validators=[users.models.username_validation], verbose_name='Имя пользователя')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='Фамилия')),
                ('email', models.EmailField(help_text='Указание email обязательно так как на него отправляется ключ авторизации', max_length=254, unique=True, verbose_name='Email адрес')),
                ('role', models.CharField(choices=[('user', 'Аутентифицированный пользователь'), ('moderator', 'Модератор'), ('admin', 'Администратор')], default='user', max_length=9, verbose_name='Права пользователя')),
                ('bio', models.TextField(blank=True, verbose_name='Биография')),
                ('is_superuser', models.BooleanField(default=False, help_text='Обозначает, что у этого пользователя есть все разрешениябез их явного назначая.', verbose_name='Суперпользователь')),
                ('is_active', models.BooleanField(default=True, help_text='Поле не доступно для редактирование администратором. Активация осуществляется пользователем через API', verbose_name='Активный пользователь')),
                ('confirmation_code_hash', models.CharField(blank=True, max_length=64, verbose_name='Хеш сумма кода подтверждения')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['id'],
            },
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_relationships'),
        ),
    ]
