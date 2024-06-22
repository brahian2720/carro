from rest_framework import serializers
from .models import Marca, Dueño, Car, DueñoCar
from django.conf import settings

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class DueñoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueño
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(write_only=True, required =False)
    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        car = super().create(validated_data)
        if image:
            car.image_url = self.save_image(car, image)
            car.save()
        return car

    def save_image(self, car, image):
        from django.core.files.storage import default_storage 
        from django.core.files.base import ContentFile
        import os

        path = default_storage.save(os.path.join('images', str(car.id) + '_' + image.
        name), ContentFile(image.read())) 
        return settings.MEDIA_URL + path

class DueñoCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DueñoCar
        fields = '__all__'