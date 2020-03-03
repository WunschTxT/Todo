from rest_framework import serializers

from . import models


class TodoListSerializer(serializers.ListSerializer):
    def update(self, instance, validated_data):
        for index, obj in enumerate(instance):
            self.child.update(obj, validated_data[index])
        return instance


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = (
            'id',
            'value',
            'is_finish',
            'isEditing',
            'isActive',
            'isChecked'
        )
        list_serializer_class = TodoListSerializer


