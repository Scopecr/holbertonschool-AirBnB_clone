#!/usr/bin/python3
"""__init__ magic method for models dictionary"""

from models.engine.file_storage import FileStorage
# FileStorage instance
storage = FileStorage()
# & Reload objects
storage.reload()
