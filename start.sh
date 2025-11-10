#!/bin/bash
# Quick start script for Lesson Manager

echo "======================================"
echo "  Bank Training Lesson Manager"
echo "======================================"
echo ""

# Activate virtual environment
source venv/bin/activate

# Check if superuser exists by trying to get user count
USER_COUNT=$(python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.count())" 2>/dev/null)

if [ "$USER_COUNT" = "0" ] || [ -z "$USER_COUNT" ]; then
    echo "⚠️  No admin user found. Let's create one!"
    echo ""
    python manage.py createsuperuser
    echo ""
fi

echo "✅ Starting development server..."
echo ""
echo "📱 Access the application at: http://localhost:8000"
echo "🔐 Admin panel at: http://localhost:8000/admin"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python manage.py runserver 0.0.0.0:8000
