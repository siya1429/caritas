from django.db import models
from users.models import User
# Create your models here.
class Event(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  name = models.CharField(max_length=100)
  description = models.TextField(blank=True, null=True)
  purpose = models.TextField()
  event_date = models.DateField()
  is_approved = models.BooleanField(default=False)
  
  created_at =  models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'events'

  def __str__(self):
    return self.name
