from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def user_directory_path(instance, filename):
    return f'user_{instance.author.id}/ads/{filename}'


def user_avatar_path(instance, filename):
    return f'user_{instance.user.id}/avatar/{filename}'


class Profile(models.Model):
    """
    Мщдель профиля пользователя
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField('Date of Birth', blank=True, null=True)
    avatar = models.ImageField(upload_to=user_avatar_path)
    city = models.TextField(max_length=50, blank=True)

    def __str__(self):
        return f'Profile for user - {self.user.username}'


class Ad(models.Model):
    """
    Обьявление пользователя
    """
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.TextField(max_length=300, verbose_name='Название')
    description = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to=user_directory_path)
    date_pub = models.DateTimeField(default=timezone.now)
    date_edit = models.DateTimeField(default=timezone.now)
    favorites = models.ManyToManyField(User, blank=True, related_name='users_favorites', verbose_name='Избранное')


class Category(models.Model):
    """
    Категории обьявления
    """
    Transport = 'Транспорт'
    Realty = 'Недвижимость'
    Work = 'Работа'
    Services = 'Услуги'
    Personal_items = 'Личные вещи'
    For_homes_and_cottages = 'Для дома и дачи'
    Consumer_electronics = 'Бытовая электроника'
    Hobbies_and_recreation = 'Хобби и отдых'
    Animals = 'Животные'
    Ready_made_business_and_equipment = 'Готовый бизнес и оборудование'

    CHOICE_GROUP = {
        (Transport, 'Транспорт'),
        (Realty, 'Недвижимость'),
        (Work, 'Работа'),
        (Services, 'Услуги'),
        (Personal_items, 'Личные вещи'),
        (For_homes_and_cottages, 'Для дома и дачи'),
        (Consumer_electronics, 'Бытовая электроника'),
        (Animals, 'Животные'),
        (Ready_made_business_and_equipment, 'Готовый бизнес и оборудование')
    }

    group = models.CharField(max_length=50, choices=CHOICE_GROUP, default=Transport)



