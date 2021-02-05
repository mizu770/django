from django.contrib import admin
from .models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','created','updated']
    raw_id_fields = ['author']
    list_filter = ['created', 'updated', 'author']
    # 외래키는 __ 사용해야된다 (그래야 하위 키 값을 읽을 수 있다.)
    search_fields = ['text','created','author__uername']
    ordering = ['-updated', '-created']

admin.site.register(Photo, PhotoAdmin)