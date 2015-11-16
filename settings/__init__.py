#
import os
#
SETTINGS_DIR = os.path.abspath(__file__)
SETTINGS_BASE_DIR = os.path.abspath(os.path.abspath(__file__))
FILE_BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = FILE_BASE_DIR
VERBOSE_LEVEL = 1

# infrastrucureSettings 
from _infrastructure import get_server_type
from _infrastructure import get_features

# Local - Not under revision
exec("from _local_settings import *")
# Base
exec("from _base import *")
#from _base import *

# Load Server
exec("from %s import *" % get_server_type())

# Load Features
for feature in get_features():
    exec("from %s import *" % feature)

# Local Post Changes - Not under revision
exec("from _local_settings_changes import *")
