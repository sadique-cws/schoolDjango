from django.contrib import admin
from .models import * 



class NotesAdmin(admin.ModelAdmin):
    list_display = ["id","user","content","date"]
    list_filter = ["user","date"]
    search_fields = ("user__username__icontains","content__icontains")

admin.site.register(Notes, NotesAdmin)



class NotesharingAdmin(admin.ModelAdmin):
    list_display = ("id","notes","share_by","share_to")
    list_filter = ("share_by","share_to","notes")

admin.site.register(NoteSharing, NotesharingAdmin)

  