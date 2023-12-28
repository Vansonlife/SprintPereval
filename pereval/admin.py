from django.contrib import admin


from .models import Pereval, Coords, Images, Level


class PerevalAdmin(admin.ModelAdmin):
    list_display = ('id', 'beauty_title', 'title', 'other_titles', 'add_time', 'status')


class CoordsAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'height')


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_added')


class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'winter', 'summer', 'autumn', 'spring')

admin.site.register(Pereval, PerevalAdmin)
admin.site.register(Coords, CoordsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Level, LevelAdmin)
