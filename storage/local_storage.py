from . import storage

import os
import shutil

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
        
        # Create dest_dir and dest_path from dest
        dest_dir = ''
        dest_path = ''

        if os.path.exists(dest_dir) and os.path.isdir(dest_dir):
            if os.path.exists(dest_path):
                # Destination path/file already exists
                return False

            # Move backup to destination
            shutil.move(source_path,dest_path)

            if os.path.exists(dest_path):
                # Copied succesfully
                return True
            
        # Still did not copy backup with success
        return False