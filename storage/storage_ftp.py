from . import storage
from ftplib import FTP

import os

class StorageFtp(storage.Storage):
    def upload_backup(self,source_path,dest_info) -> bool:
        # Check file source
        if not os.path.exists(source_path):
            # Source file does not exist, something went wrong on pg_dump
            return False

        ftp_host = 'host.com'
        ftp_port = 21
        ftp_ssl = 4
        ftp_user = 5
        ftp_passwd = 6

        ftp_pasv_mode = 3
        ftp_pasv_ports = []

        ftp = FTP(source_address=(ftp_host,ftp_port),user=ftp_user,passwd=ftp_passwd,encoding='utf-8')
        ftp.connect()
        ftp.login()
        ftp.set_pasv(ftp_pasv_mode)


    def remove_backup(self):
        None

    def get_max_space(self):
        None

    def get_current_space(self):
        None

    def get_free_space(self):
        None

    def check_connection(self,dest_info):
        ftp_host = 'host.com'
        ftp_port = 21
        ftp_ssl = 4
        ftp_user = 5
        ftp_passwd = 6


        ftp = FTP(source_address=(ftp_host,ftp_port),user=ftp_user,passwd=ftp_passwd,encoding='utf-8')
        resp = ftp.connect()
        if resp == '':
            return False
        resp = ftp.login()
        if resp == '':
            return False
        ftp.close()
        return True


