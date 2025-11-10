from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Lesson(models.Model):
    """Model for storing lesson information"""
    title = models.CharField(max_length=200, verbose_name="Sapagyň ady")
    content = RichTextField(blank=True, null=True, config_name='lesson_content', help_text="Baý tekst formatlaşdyrma bilen sapagyň mazmuny (hökmany däl)", verbose_name="Mazmun")
    description = models.TextField(max_length=500, blank=True, null=True, help_text="Gysga düşündiriş", verbose_name="Düşündiriş")
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Döredilen senesi")
    date_updated = models.DateTimeField(auto_now=True, verbose_name="Täzelenen senesi")
    is_published = models.BooleanField(default=True, help_text="Talyplara görkezilsin", verbose_name="Çap edildi")
    order = models.IntegerField(default=0, help_text="Görkeziş tertibi (pes sanlar öň görkeziler)", verbose_name="Tertip belgisi")
    
    class Meta:
        ordering = ['order', '-date_created']
        verbose_name = "Sapak"
        verbose_name_plural = "Sapaklar"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'pk': self.pk})


class Attachment(models.Model):
    """Model for storing lesson attachments"""
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='attachments', verbose_name="Sapak")
    title = models.CharField(max_length=200, help_text="Goşmaça faýlyň ady", verbose_name="Ady")
    file = models.FileField(upload_to='lesson_attachments/%Y/%m/%d/', verbose_name="Faýl")
    description = models.TextField(blank=True, null=True, help_text="Goşmaça düşündiriş (hökmany däl)", verbose_name="Düşündiriş")
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Ýüklenen senesi")
    file_size = models.IntegerField(blank=True, null=True, help_text="Faýlyň ululygy baýtda", verbose_name="Faýl ululygy")
    
    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = "Goşmaça faýl"
        verbose_name_plural = "Goşmaça faýllar"
    
    def __str__(self):
        return f"{self.title} - {self.lesson.title}"
    
    def save(self, *args, **kwargs):
        if self.file:
            self.file_size = self.file.size
        super().save(*args, **kwargs)
    
    def get_file_size_display(self):
        """Return human-readable file size"""
        if not self.file_size:
            return "Unknown"
        
        size = self.file_size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f} {unit}"
            size /= 1024.0
        return f"{size:.1f} TB"
