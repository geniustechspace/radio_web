from wagtail_modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import ProgramSchedule

class ProgramScheduleAdmin(ModelAdmin):
    model = ProgramSchedule
    menu_label = "Program Schedules"
    menu_icon = "radio-full"
    menu_order = 200
    add_to_settings_menu = False
    list_display = ("title", "presenter", "day_of_week", "start_time", "end_time")
    search_fields = ("title", "presenter", "day_of_week")

# Register the model admin so it appears in the Wagtail admin
modeladmin_register(ProgramScheduleAdmin)
