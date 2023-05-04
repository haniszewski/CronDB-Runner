# Generic storage file
# Acts like interface

class Storage:
    def upload_backup(self) -> bool:
        return False

    def remove_backup(self):
        None

    def get_max_space(self):
        None

    def get_current_space(self):
        None

    def get_free_space(self):
        None

    def check_connection(self):
        None

    