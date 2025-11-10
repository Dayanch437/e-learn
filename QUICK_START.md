# Quick Reference Guide

## Starting the Application

### Option 1: Using the start script (Recommended)
```bash
./start.sh
```

### Option 2: Manual start
```bash
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000
```

## URLs

- **Home Page**: http://localhost:8000
- **All Lessons**: http://localhost:8000/lessons/
- **Admin Panel**: http://localhost:8000/admin

## First Time Setup

1. Create admin user (only needed once):
```bash
source venv/bin/activate
python manage.py createsuperuser
```

2. Start the server (see above)

3. Login to admin panel and add your first lesson

## Adding Lessons

### Via Admin Panel (Easy Way)
1. Go to http://localhost:8000/admin
2. Click "Lessons" → "Add Lesson"
3. Fill in:
   - Title (required)
   - Description (recommended)
   - Content (optional - can be text, notes, instructions)
   - Order number (0 = first)
   - Check "Is published" to make it visible
4. Add attachments in the inline form at the bottom
5. Click "Save"

### Lesson Fields Explained

- **Title**: The name students will see
- **Description**: Short summary shown in the list
- **Content**: Full lesson text (optional - good for instructions, notes, or text lessons)
- **Order**: Lower numbers appear first (use 0, 10, 20, 30 to easily reorder later)
- **Is published**: Uncheck to hide from students while editing

### Attachments

Each attachment can have:
- **Title**: Name of the file (e.g., "Week 1 - Banking Basics")
- **File**: Upload any file (PDF, DOCX, XLSX, etc.)
- **Description**: Optional notes about the file

## Common Workflows

### Preparing a Weekly Lesson
1. Create lesson with order=10 (for week 1)
2. Add title: "Week 1 - Introduction to Banking"
3. Add description summarizing the week's topics
4. Add content with week's outline and instructions
5. Upload all materials as attachments
6. Leave "Is published" unchecked until ready
7. When ready, check "Is published" and save

### Organizing Lessons
Use the order field strategically:
- 0 = Introduction
- 10, 20, 30... = Weekly lessons
- 100, 110, 120... = Advanced topics
- 1000+ = Reference materials

### Bulk Updates
In admin, you can:
- Use list view to quickly change order and publish status
- Use filters to find lessons by date
- Use search to find specific content

## File Management

### Uploaded Files Location
All attachments are stored in: `media/lesson_attachments/YYYY/MM/DD/`

### File Size Display
The system automatically shows human-readable file sizes (KB, MB, GB)

### File Types
Upload any file type - PDFs, Word docs, Excel sheets, PowerPoint, images, etc.

## Student Experience

Students will see:
1. **Home Page**: Welcome message + recent 5 lessons
2. **All Lessons Page**: Grid of all published lessons
3. **Lesson Detail**: Full content + all attachments with download buttons

Students can:
- Browse lessons by date
- See lesson descriptions before opening
- Read lesson content
- Download attachments
- See file sizes before downloading

## Tips & Best Practices

### Content Organization
- Use descriptions to help students decide if they need to review
- Put important notes in the content field
- Use meaningful file names for attachments

### Time-Saving Tips
- Prepare lessons ahead and keep unpublished
- Use copy/paste for similar lesson structures
- Number lessons to maintain order easily

### File Naming
Good: "Week1-BankingBasics-Slides.pdf"
Bad: "document1.pdf"

### Regular Tasks
- Weekly: Add new lessons
- Monthly: Review and update older content
- As needed: Upload new reference materials

## Troubleshooting

### Can't access admin panel?
Make sure you created a superuser with `python manage.py createsuperuser`

### Files not uploading?
Check that `media/` folder exists and has write permissions

### Port already in use?
Use a different port: `python manage.py runserver 0.0.0.0:8001`

### Students can't see a lesson?
Check that "Is published" is checked in the admin panel

## Advanced Features

### Filtering in Admin
- Filter lessons by publication status
- Filter by creation date
- Search by title, content, or description

### Inline Editing
In the lesson list view, you can edit order and publish status directly

### Bulk Actions
Select multiple lessons and use bulk actions in admin

## Keyboard Shortcuts (Admin Panel)

- `/` - Focus search box
- `Shift + A` - Add new item
- `Shift + S` - Save changes

## Need Help?

Check the README.md for detailed documentation
Django Admin Documentation: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

---

Keep this file handy for quick reference while managing your training lessons!
