from django.db import models


class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=256)
    is_finish = models.BooleanField(default=False)
    isEditing = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isChecked = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
