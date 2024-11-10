import sys
from service.data_service import DataService as ds

class Processing:
    @staticmethod
    def on_close():
        sys.exit()


    @staticmethod
    def get_load_data():
        ds.create_folder()
        return ds.read_data_user() if ds.check_file_data_user() else {}

