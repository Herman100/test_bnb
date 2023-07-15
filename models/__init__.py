#!/usr/bin/python3
"""init file module containing storage call"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
