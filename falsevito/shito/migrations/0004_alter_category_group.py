# Generated by Django 3.2 on 2021-05-01 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shito', '0003_auto_20210429_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='group',
            field=models.CharField(choices=[('Личные вещи', 'Личные вещи'), ('Животные', 'Животные'), ('Услуги', 'Услуги'), ('Бытовая электроника', 'Бытовая электроника'), ('Транспорт', 'Транспорт'), ('Для дома и дачи', 'Для дома и дачи'), ('Готовый бизнес и оборудование', 'Готовый бизнес и оборудование'), ('Недвижимость', 'Недвижимость'), ('Работа', 'Работа')], default='Транспорт', max_length=50),
        ),
    ]
