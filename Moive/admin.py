from django.contrib import admin

from .models import Moive
# Register your models here.
@admin.register(Moive)
class MoiveAdmin(admin.ModelAdmin):
    fields = ('name','real_time_gross','total_box_office','precent','row_screenings','Release_time')
    list_display = ('name','real_time_gross','total_box_office','precent','row_screenings','Release_time')
    save_on_top = True