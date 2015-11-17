# django-i-settings
django-i-settings handles multiple settings files for development, testing and production

# Alpha version

This is the first upload and it has not been tested. Can be used as starting point.

## Installation and Configuration

 - replace the settings.py with this package settings folder.
 - edit _base.py to match your basics settings requirements
 - edit server_* files to match your settings requirement for different servers types. For example: server_development.py, server_testing.py and server+production.py
 - edit or create feature_* files if you require features to switch on/off within each server type.

## Switching settings

 - edit/create local_config.py to select the server type and the features, see example.

For a development server type with redis active you might have the local_config.py like:

    settings_server='development'
    settings_features=[
      'feature_cache_redis_local',
    ]

# References

Main idea

 - [http://stackoverflow.com/questions/5159852/managing-multiple-settings-py-files](http://stackoverflow.com/questions/5159852/managing-multiple-settings-py-files)

Additional references for improvements and alternatives

 - Splitting up the settings file [https://code.djangoproject.com/wiki/SplitSettings](https://code.djangoproject.com/wiki/SplitSettings)
 - [http://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django](http://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django)
 - [http://stackoverflow.com/questions/88259/how-do-you-configure-django-for-simple-development-and-deployment](http://stackoverflow.com/questions/88259/how-do-you-configure-django-for-simple-development-and-deployment)
 - [http://django-configurations.readthedocs.org/en/latest/](http://django-configurations.readthedocs.org/en/latest/)

# Future / TODO

Include facility for virtualenv, ideas for example:

 - [http://www.marinamele.com/2014/02/django-best-practices-i-different.html](http://www.marinamele.com/2014/02/django-best-practices-i-different.html)

Include facility to print the selected settings as settings.py file for simple deploiment.

 - python manage.py  diffsettings --all
 - https://github.com/msabramo/django-print-settings