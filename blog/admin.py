from django.contrib import admin
from .models import Blog              #for adding the project in the admin sot hat whenever a change is done
                                          #  it reflects immediately
admin.site.register(Blog)
