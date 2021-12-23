echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('superadmin', 'postmancourse@course.com', 'ThisIs@SecurePassw0rd')" | python manage.py shell


python manage.py drf_create_token superadmin