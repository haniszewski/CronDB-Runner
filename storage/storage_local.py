from . import storage

import os
import shutil

class StorageLocal(storage.Storage):
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
                shutil.copy2(source_path,dest_path)
                # Copied succesfully
                return True
            
        # Still did not copy backup with success
        return False
    
    def remove_backup(self,dest_info):
        dest_path = ''

        if os.path.exists(dest_path):
            os.remove(dest_path)
        else:
            # File doesnt exists already
            None

    def check_connection(self):
        # Could be simplfied but set for later
        if os.path.isdir(self.root_path):
            # Root path is OK, so True
            return True
        return False