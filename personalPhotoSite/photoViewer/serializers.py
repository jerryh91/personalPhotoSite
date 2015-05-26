from django.forms import widgets
from rest_framework import serializers
from photoViewer.models import Photo


class PhotoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    photo_title = serializers.CharField(max_length=200)
    date_taken = serializers.DateField('date taken', allow_blank=True)
    photo_img = serializers.ImageField(upload_to = "images/", default= "")

    def create(self, validated_data):
        """
        Create and return a new `Photo` instance, given the validated data.
        """
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Photo` instance, given the validated data.
        """
        instance.photo_title = validated_data.get('photo_title', instance.photo_title )
        instance.date_taken = validated_data.get('date_taken', instance.date_taken)
        instance.photo_img = validated_data.get('photo_img', instance.photo_img)
        instance.save()
        return instance