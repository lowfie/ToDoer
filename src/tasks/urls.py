from django.urls import path

from src.tasks.views import get_task_details, create_task, update_task, ExploreTask

urlpatterns = [
    path('create/', create_task),
    path('<int:id>/', get_task_details),
    path('<int:id>/update/', update_task),
    path('explore/', ExploreTask.as_view())
]
