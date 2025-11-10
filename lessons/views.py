from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Lesson, Attachment


class LessonListView(ListView):
    """View for listing all published lessons"""
    model = Lesson
    template_name = 'lessons/lesson_list.html'
    context_object_name = 'lessons'
    paginate_by = 10
    
    def get_queryset(self):
        return Lesson.objects.filter(is_published=True).prefetch_related('attachments')


class LessonDetailView(DetailView):
    """View for displaying a single lesson with attachments"""
    model = Lesson
    template_name = 'lessons/lesson_detail.html'
    context_object_name = 'lesson'
    
    def get_queryset(self):
        return Lesson.objects.filter(is_published=True).prefetch_related('attachments')


def home(request):
    """Home page view"""
    recent_lessons = Lesson.objects.filter(is_published=True).prefetch_related('attachments')[:5]
    total_lessons = Lesson.objects.filter(is_published=True).count()
    
    context = {
        'recent_lessons': recent_lessons,
        'total_lessons': total_lessons,
    }
    return render(request, 'lessons/home.html', context)
