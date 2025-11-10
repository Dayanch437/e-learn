# Bank Training Lesson Manager

A Django-based lesson management system designed for bank training programs. Share lessons and materials with students efficiently.

## Features

- 📚 **Lesson Management**: Create and organize training lessons
- 📎 **File Attachments**: Upload and share training materials (PDFs, documents, etc.)
- 🎨 **Modern UI**: Responsive design using Ant Design principles
- 📱 **Mobile Friendly**: Works perfectly on all devices
- 🔒 **Admin Panel**: Easy-to-use admin interface for managing content
- 🎯 **Simple & Efficient**: No complicated setup, just add lessons and go!

## Quick Start

### 1. Create Admin User

First, create an admin account to manage lessons:

```bash
source venv/bin/activate
python manage.py createsuperuser
```

Follow the prompts to set up your username, email, and password.

### 2. Run the Server

Start the development server:

```bash
python manage.py runserver 0.0.0.0:8000
```

The application will be available at: `http://localhost:8000`

### 3. Access Admin Panel

1. Go to: `http://localhost:8000/admin`
2. Login with your superuser credentials
3. Start adding lessons!

## How to Use

### Adding a New Lesson

1. Login to the admin panel
2. Click on "Lessons" → "Add Lesson"
3. Fill in the lesson details:
   - **Title**: Name of the lesson
   - **Description**: Short summary (optional but recommended)
   - **Content**: Full lesson text (optional)
   - **Order**: Display order (lower numbers appear first)
   - **Is published**: Check to make visible to students
4. Add attachments if needed (files, PDFs, documents)
5. Click "Save"

### Managing Attachments

You can add attachments in two ways:

1. **When creating a lesson**: Scroll down to the "Attachments" section
2. **Separately**: Go to "Attachments" → "Add Attachment" in admin

Each attachment can have:
- Title (required)
- File upload (required)
- Description (optional)

### Student View

Students can:
- View all published lessons on the homepage
- Browse all lessons at `/lessons/`
- Click any lesson to see full details
- Download attached files with one click

## Project Structure

```
lesson/
├── lesson_manager/          # Django project settings
├── lessons/                 # Main app
│   ├── models.py           # Lesson and Attachment models
│   ├── views.py            # Views for displaying lessons
│   ├── admin.py            # Admin configuration
│   └── urls.py             # URL routing
├── templates/              # HTML templates
│   ├── base.html          # Base template with Ant Design
│   └── lessons/           # Lesson-specific templates
├── static/                # CSS, JS files (if needed)
├── media/                 # Uploaded files storage
└── manage.py             # Django management script
```

## Tips for Bank Training

1. **Organization**: Use the "order" field to arrange lessons by topic or date
2. **Descriptions**: Add clear descriptions so students know what to expect
3. **File Naming**: Use descriptive names for attachments (e.g., "Week1-BankingBasics.pdf")
4. **Publishing**: Use the "is_published" toggle to prepare lessons before making them visible
5. **Updates**: The system tracks when lessons are created and updated

## Common Tasks

### Change Server Port

```bash
python manage.py runserver 0.0.0.0:8080
```

### Create Database Backup

```bash
cp db.sqlite3 db.sqlite3.backup
```

### View All Lessons (Command Line)

```bash
python manage.py shell
>>> from lessons.models import Lesson
>>> Lesson.objects.all()
```

## Troubleshooting

### Port Already in Use

If port 8000 is busy, use a different port:
```bash
python manage.py runserver 0.0.0.0:8001
```

### Admin CSS Not Loading

Make sure DEBUG=True in `lesson_manager/settings.py` for development.

### File Upload Issues

Check that the `media/` folder exists and has write permissions.

## Security Notes

⚠️ **For Production Use**:
- Change `SECRET_KEY` in settings.py
- Set `DEBUG = False`
- Configure proper `ALLOWED_HOSTS`
- Use a production database (PostgreSQL, MySQL)
- Setup proper static file serving
- Enable HTTPS

## Support

For issues or questions about Django:
- Django Documentation: https://docs.djangoproject.com/
- Django Admin Guide: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

---

**Built with Django 5.2** | **Designed for Bank Training Programs**
# e-learn
