from ..database import Database

class Postgres12(Database):
    def __init__(self):
        None

    def test_connection(self,conn_info):
        # Test connection to pg12 database, test login
        return super().test_connection()
    
    def create_backup(self,backup_info):
        # pg_dump -O -h host ...  > path to temp
        return super().create_backup()