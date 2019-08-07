from django.db import models

# Create your models here.
class Moive(models.Model):
    name = models.CharField(max_length=10,verbose_name="电影名称",primary_key=True)
    real_time_gross = models.DecimalField(max_digits=12,decimal_places=2,default=-1,verbose_name="实时票房")
    total_box_office = models.DecimalField(max_digits=12,decimal_places=2,default=-1,verbose_name="累计票房")
    precent = models.CharField(max_length=6,verbose_name="实时排片")
    row_screenings = models.IntegerField(verbose_name="实时场次")
    Release_time = models.IntegerField(verbose_name="上映天数")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "电影票房"
