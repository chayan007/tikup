import uuid as uuid
from django.db import models


class BaseModel(models.Model):
    """Base model for Tikup infrastructure."""

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At', db_index=True)
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Last Modified At')

    class Meta:
        """Define meta params for model."""

        abstract = True
        ordering = ('-created_at',)
