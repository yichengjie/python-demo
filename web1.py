from django.apps import apps
name = apps.get_app_config('admin').verbose_name
print('name : ', name)
