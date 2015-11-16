'''
@author: F.Mariotti
'''

import os
#import imp
from . import VERBOSE_LEVEL

def get_server_type(servername=None):

    if servername != None:
        return 'server_'+servername

    try:
        #imp.find_module('local_config')
        from . import local_config
    except ImportError:
        server = 'default'
        config_features = list()
        if VERBOSE_LEVEL > 0:
            print "no local_config module found"
    else:
        if VERBOSE_LEVEL > 0:
            print "reading from local_config module: "+local_config.settings_server
        #from . import local_config
        server = local_config.settings_server
        config_features = local_config.settings_features
        
    return 'server_'+server
#
def get_features( features=list(), only_selected=False):

    try:
        #imp.find_module('local_config')
        from . import local_config
    except ImportError:
        server = 'default'
        config_features = list()
        if VERBOSE_LEVEL > 0:
            print "no local_config module found"
    else:
        if VERBOSE_LEVEL > 0:
            print "reading from local_config module: "+str(local_config.settings_features)
        #from . import local_config
        server = local_config.settings_server
        config_features = local_config.settings_features

    if not only_selected:
        features = config_features + features

        
    return features
#    
def print_current_settings():

    from django.conf import settings as current_settings
    from pprint import pprint
    
    for name in dir(current_settings):
        #print name, getattr(current_settings, name)
        pprint(getattr(current_settings, name))
