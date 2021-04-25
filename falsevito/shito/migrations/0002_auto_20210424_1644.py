# Generated by Django 3.2 on 2021-04-24 12:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shito', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tel_number',
        ),
        migrations.AlterField(
            model_name='ad',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='users_favorites', to=settings.AUTH_USER_MODEL, verbose_name='Избранное'),
        ),
        migrations.AlterField(
            model_name='category',
            name='group',
            field=models.CharField(choices=[('Недвижимость', 'Недвижимость'), ('Готовый бизнес и оборудование', 'Готовый бизнес и оборудование'), ('Работа', 'Работа'), ('Животные', 'Животные'), ('Личные вещи', 'Личные вещи'), ('Услуги', 'Услуги'), ('Для дома и дачи', 'Для дома и дачи'), ('Бытовая электроника', 'Бытовая электроника'), ('Транспорт', 'Транспорт')], default='Транспорт', max_length=50),
        ),
    ]
