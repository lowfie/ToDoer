from rest_framework import serializers

from src.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class CreateTaskSerializer(serializers.ModelSerializer):
    due_date_timestamp = serializers.CharField(required=True)

    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "due_date_timestamp",
            "is_complete",
            "user_id",
        )

    def create(self, validated_data):
        validated_data["user_id"] = self.context.get("user_id")
        return Task.objects.create(**validated_data)


class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "title",
            "description",
            "is_complete",
        )


class ExploreTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
