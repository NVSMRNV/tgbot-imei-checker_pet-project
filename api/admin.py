from django.contrib import admin

from api.models.users import User
from api.models.whitelist import WhiteList


admin.site.register(User)
admin.site.register(WhiteList)

