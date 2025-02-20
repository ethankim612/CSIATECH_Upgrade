from django.contrib import admin
from .models import (
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    DefaultMonday,
    DefaultTuesday,
    DefaultWednesday,
    DefaultThursday,
)
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
admin.site.register(Monday, SimpleHistoryAdmin)
admin.site.register(Tuesday, SimpleHistoryAdmin)
admin.site.register(Wednesday, SimpleHistoryAdmin)
admin.site.register(Thursday, SimpleHistoryAdmin)
admin.site.unregister(DefaultMonday)
admin.site.unregister(DefaultTuesday)
admin.site.unregister(DefaultWednesday)
admin.site.unregister(DefaultThursday)