
from tkinter.messagebox import *

def validation_enter(name, zone, common_areas, access_zone, data_employees):

    def requires_access(method):

        def wrapper(self, *args, **kwargs):

            assert name in data_employees, showerror('Error input', 'This name not in the list of employees')

            if zone in common_areas:
                res = method(self, *args, **kwargs)
                return res

            if zone in access_zone:
                res = method(self, *args, **kwargs)
                return res

            return False

        return wrapper


def validation_log(name, granted, denied):

    def log_access(method):

        def wrapper(self, *args, **kwargs):

            res = method(self, *args, **kwargs)

            if res:
                granted(self).append(f'user access {name} granted')

            denied(self).append(f'user access {name} denied')

        return wrapper




