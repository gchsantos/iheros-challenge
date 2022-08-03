import uuid
from django.db import models


class Identity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    classification = models.ForeignKey(
        "Classes", on_delete=models.CASCADE, related_name="heroclassification"
    )
    lat = models.FloatField("Latitude", blank=True)
    lng = models.FloatField("Longitude", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Classes(models.Model):
    classification = models.TextField(unique=True)
