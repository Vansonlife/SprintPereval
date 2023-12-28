from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Pereval(models.Model):
    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
    ("new", "новый"),
    ("pending",  "модератор взял в работу"),
    ("accepted", "модерация прошла успешно"),
    ("rejected",  "модерация прошла, информация не принята"),
    ]

    beauty_title = models.CharField(max_length=255, verbose_name='Название препятствия')
    title = models.CharField(max_length=255, verbose_name='Название вершины')
    other_titles = models.CharField(max_length=255, verbose_name='Другое название')
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    #coords = models.ForeignKey('Coords', on_delete=models.CASCADE)
    #level = models.ForeignKey('Level', on_delete=models.CASCADE)
    #photo = models.ManyToManyField('Images', blank=True, related_name='img')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    connect = models.TextField(null=True)

    def __str__(self):
        return f'{self.beauty_title} {self.title} {self.other_titles} id: {self.pk} {self.title}'

    class Meta:
        verbose_name = "Перевал"
        verbose_name_plural = "Перевал"


class Coords(models.Model):
    coords = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    latitude = models.FloatField(max_length=50, verbose_name='Широта')
    longitude = models.FloatField(max_length=50, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"


class Level(models.Model):
    level = models.ForeignKey(Pereval, on_delete=models.CASCADE)
    winter = models.CharField(max_length=10, verbose_name='Зима', null=True)
    summer = models.CharField(max_length=10, verbose_name='Лето', null=True)
    autumn = models.CharField(max_length=10, verbose_name='Осень', null=True)
    spring = models.CharField(max_length=10, verbose_name='Весна', null=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

    class Meta:
        verbose_name = "Уровень сложности"
        verbose_name_plural = "Уровень сложности"


class Images(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    #data = models.CharField(max_length=255)
    data = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', null=True, blank=True)
    title = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    #image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"id: {self.pk} title:{self.title} {self.data}"

    class Meta:
        verbose_name = "Изображения"
        verbose_name_plural = "Изображения"

phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,12}$',
        message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 12 digits allowed.")

class Users(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    otc = models.CharField(max_length=150)
    phone = models.CharField(validators=[phone_regex], max_length=14, blank=True)

    def __str__(self):
        return f'{self.name}'
