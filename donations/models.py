from django.db import models
from users.models import User
# Create your models here.
class Donation(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  category = models.CharField(max_length=50)
  amount = models.DecimalField(max_digits=7, decimal_places=2)
  status = models.CharField(max_length=20, default='INITIATED')
  payment_id = models.CharField(max_length=50, blank=True, null=True)
  transaction_id = models.CharField(max_length=50, blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  class Meta:
    db_table = 'donation'

  def __str__(self):
    return str(self.id)


