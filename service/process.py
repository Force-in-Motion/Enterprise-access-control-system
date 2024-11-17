import sys
from service.service import DataService as ds

class Processing:
    @staticmethod
    def on_close():
        sys.exit()


    @staticmethod
    def get_data_users():
        ds.create_folder()
        return ds.read_data_user() if ds.check_file_data_user() else {}


    @staticmethod
    def get_log():
        ds.create_folder()
        return ds.read_data_log() if ds.check_file_data_log() else {}

