from django.contrib import admin
from market.models import *

# Register your models here.
admin.site.register(Currency)
admin.site.register(Key)
admin.site.register(Market)
admin.site.register(Position)
admin.site.register(Transaction)
