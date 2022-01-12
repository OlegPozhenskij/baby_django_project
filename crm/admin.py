from django.contrib import admin
from .models import Order, StatusName, CommentCrm

# Register your models here.
admin.site.register(Order)
admin.site.register(StatusName)
admin.site.register(CommentCrm)