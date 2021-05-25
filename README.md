### Создать/обновить суперюзера

python manage.py createsuperuser

   - `python manage.py shell`
   - `from django.contrib.auth.models import User`
   - `user=User.objects.create_user('<твой логин>', password='<твой пароль>')`
   - *здесь, если юзер существует* `user=User.objects.get(username='<твой логин>')`
   - `user.is_superuser=True`
   - `user.is_staff=True`
   - `user.save()`
   - `exit`