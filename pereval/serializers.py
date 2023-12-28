from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Coords, Level, Pereval, Images, Users


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring')


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    fam = serializers.CharField(source='last_name')
    otc = serializers.CharField(source='patronymic')
    email = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = User
        fields = ('email', 'fam', 'name', 'otc', 'phone',)
        verbose_name = 'Пользователь'


class ImagesSerializer(serializers.ModelSerializer):
    #image = serializers.ImageField(max_length=None, use_url=True)
    data = serializers.ImageField(max_length=None, use_url=True)
    #data = serializers.CharField()
    #data = serializers.URLField()

    class Meta:
        model = Images
        fields = ('data', 'title')
        verbose_name = 'Фото'

class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ('beauty_title', 'title', 'other_titles', 'connect')
        verbose_name = 'Фото'

class PerevalAddSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    perevals = PerevalSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    image = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'id', 'user', 'perevals', 'coords', 'level', 'image','status')


    def create(self, validated_data):
        image_data = validated_data.pop('data')
        pereval = Pereval.objects.create(**validated_data)
        for images_data in image_data:
            Images.objects.create(pereval=pereval, **images_data)
        return pereval


class PerevalSubmitDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = '__all__'


class PerevalSubmitDataUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ('fam', 'email', 'phone')


class PerevalSubmitDataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

