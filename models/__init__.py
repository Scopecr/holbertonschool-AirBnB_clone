#!/usr/bin/python3
"""__init__ magic method for models dictionary"""
from models.engine.file.storage import FileStorage


storage = FileStorage()
storage.reload()
