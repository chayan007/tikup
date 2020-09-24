
# settings.py
from dotenv import load_dotenv

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # Python 3.6+ only

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


import os

from tikup.base import *

if os.getenv("ENVIRONMENT") == "local":  # local development
    from tikup.local import *
else:  # production
    from tikup.production import *
    