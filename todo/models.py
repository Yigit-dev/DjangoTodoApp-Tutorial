from django.db import models

# Create your models here.

class Todo(models.Model):
  #id vermedik zaten bunu django oluşturuyor primary key özelliğide veriyor
  title = models.CharField(max_length=50, verbose_name = "Başlık") # charfield: varchar
  completed = models.BooleanField(verbose_name="Durum")

  def __str__(self):
    return self.title