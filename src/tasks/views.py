from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema
from rest_framework import response, status, permissions, generics
from rest_framework.decorators import api_view, permission_classes

from src.tasks.models import Task
from src.tasks.types import TaskMethods
from src.tasks.serializer import (
    TaskSerializer,
    UpdateTaskSerializer,
    CreateTaskSerializer,
    ExploreTaskSerializer
)


@swagger_auto_schema(
    method=TaskMethods.get,
    operation_description="Get task details",
    responses={200: TaskSerializer}
)
@api_view(http_method_names=[TaskMethods.get, TaskMethods.delete])
@permission_classes([permissions.IsAuthenticated])
def get_task_details(request: Request, id: int):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return response.Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    # TODO: add IsTaskOwner permission
    if request.user != task.user:
        return response.Response({"detail": "You don't have permission"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == TaskMethods.delete:
        task.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    task_serialize = TaskSerializer(task).data
    return response.Response(task_serialize)


@swagger_auto_schema(
    method="post",
    operation_description="Create task",
    request_body=CreateTaskSerializer,
    responses={200: TaskSerializer},
)
@api_view(http_method_names=["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_task(request: Request):
    serializer = CreateTaskSerializer(data=request.data, context={"user_id": request.user.id})
    serializer.is_valid(raise_exception=True)

    serializer.save()
    return response.Response(serializer.data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(
    method=TaskMethods.patch,
    operation_description="Update task details",
    request_body=UpdateTaskSerializer,
    responses={200: TaskSerializer},
)
@permission_classes([permissions.IsAuthenticated])
@api_view(http_method_names=[TaskMethods.patch])
def update_task(request: Request, id: int):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return response.Response(status=status.HTTP_404_NOT_FOUND)

    # TODO: add IsTaskOwner permission
    if request.user != task.user:
        return response.Response({"detail": "You don't have permission"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UpdateTaskSerializer(instance=task, data=request.data)
    serializer.is_valid()
    if serializer.errors:
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return response.Response(TaskSerializer(task).data, status=status.HTTP_200_OK)


class ExploreTask(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExploreTaskSerializer

    def get_queryset(self):
        """
        Not the best filter solution, because if there
        are a lot of parameters, you will have to write
        a lot of conditions, it is better to use some
        pattern or django-filter
        """
        queryset = Task.objects.filter(user=self.request.user)

        due_date = self.request.query_params.get('due_date')
        is_complete = self.request.query_params.get('is_complete')

        if due_date:
            is_due_date = due_date.lower() == str(True).lower()
            queryset = queryset.order_by('-due_date') if is_due_date else queryset.order_by()

        if is_complete:
            is_complete = is_complete.lower() == str(True).lower()
            queryset = queryset.filter(is_complete=is_complete)

        return queryset
