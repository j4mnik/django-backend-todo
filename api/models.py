import uuid
from django.db import models

# Create your models here.

REGULAR = "regular"
CAN_WAIT = "can_wait"
HAVE_TO = "have_to"

PRIORITIES = (
    (REGULAR, "Regular"),
    (CAN_WAIT, "Can wait"),
    (HAVE_TO, "Have to!")
)


class Task(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255, null=False)
    importance = models.CharField(max_length=25, null=False, default=REGULAR, choices=PRIORITIES)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    is_done = models.BooleanField(default=False, null=False)

    class Meta:
        db_table = "task"
