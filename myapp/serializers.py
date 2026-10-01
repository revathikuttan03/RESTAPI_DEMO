from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        return value


    def validate(self,data):
        if data.get('completed') and len(data.get('title')) < 5:
            raise serializers.ValidationError(
                "A completed task must have a title with at least 5 characters."
            )
        return data

    class Meta:
        model = Task
        fields = '__all__'