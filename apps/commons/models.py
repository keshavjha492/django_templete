from django.db import models
import uuid




class DateTimeModel(models.Model):
    uuid= models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class meta:
        abstract = True
  
