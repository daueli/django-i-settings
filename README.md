# django-i-settings
django-i-settings handle multiple settings files for development, testing and production

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

