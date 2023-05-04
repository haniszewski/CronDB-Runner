from . import storage

import os

class LocalStorage(storage.Storage):
    def __init__(self,storage_root_path):
        super().__init__()
        if storage_root_path == None:
            return
        self.root_path = storage_root_path

    def upload_backup(self,source_path,dest_info) -> bool:

        # Check file source
        if not os.path.exists(source_path):
            # Source file does not exist, something went wrong on pg_dump
            return False
        
        dest_dir = ''
        


        return False