from django.contrib import admin
from .models import Lesson, Attachment


class AttachmentInline(admin.TabularInline):
    """Inline admin for attachments"""
    model = Attachment
    extra = 1
    fields = ['title', 'file', 'description']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """Admin configuration for Lesson model"""
    list_display = ['title', 'order', 'date_created', 'is_published', 'attachment_count']
    list_filter = ['is_published', 'date_created']
    search_fields = ['title', 'content', 'description']
    list_editable = ['order', 'is_published']
    date_hierarchy = 'date_created'
    inlines = [AttachmentInline]
    
    fieldsets = (
        ('Sapagyň maglumatlary', {
            'fields': ('title', 'description', 'content', 'order')
        }),
        ('Sazlamalar', {
            'fields': ('is_published',)
        }),
    )
    
    def attachment_count(self, obj):
        return obj.attachments.count()
    attachment_count.short_description = 'Goşmaça faýllar'


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    """Admin configuration for Attachment model"""
    list_display = ['title', 'lesson', 'get_file_size_display', 'uploaded_at']
    list_filter = ['uploaded_at', 'lesson']
    search_fields = ['title', 'description', 'lesson__title']
    readonly_fields = ['file_size', 'uploaded_at']
