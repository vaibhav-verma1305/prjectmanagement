from django.contrib import admin
from .models import First_year
from .models import Second_year
from .models import Third_year
from .models import Fourth_year

# Register your models here.
admin.site.register(First_year)
admin.site.register(Second_year) 
admin.site.register(Third_year) 
admin.site.register(Fourth_year)  