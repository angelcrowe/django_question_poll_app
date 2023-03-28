from django.contrib import admin
#mke poll app modifiable in admin panel
from .models import Question

admin.site.register(Question)
