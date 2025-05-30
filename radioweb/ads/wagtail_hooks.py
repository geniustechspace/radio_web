from wagtail_modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Advertisement

# class AdvertisementPageAdmin(ModelAdmin):
#     model = Advertisement
#     menu_label = "Advertisements"
#     menu_icon = "pick"  # You can choose an icon from Wagtail's icon set
#     menu_order = 200
#     add_to_settings_menu = False
#     exclude_from_explorer = False
#     list_display = ("title", "ad_type", "live", "last_published_at")

# modeladmin_register(AdvertisementPageAdmin)
