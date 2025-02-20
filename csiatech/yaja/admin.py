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
admin.site.register(DefaultMonday, SimpleHistoryAdmin)
admin.site.register(DefaultTuesday, SimpleHistoryAdmin)
admin.site.register(DefaultWednesday, SimpleHistoryAdmin)
admin.site.register(DefaultThursday, SimpleHistoryAdmin)