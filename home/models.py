from django.db import models

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()
  email = models.EmailField(max_length=100)
  phone = models.CharField(max_length=15, blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'contacts'

  def __str__(self):
    return self.name