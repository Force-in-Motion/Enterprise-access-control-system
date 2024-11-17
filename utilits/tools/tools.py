

def validation_enter(zone, common_areas, access_zone):

    def requires_access(method):

        def wrapper(self, *args, **kwargs):

            if zone in common_areas:
                method(self, *args, **kwargs)
                return True

            if zone in access_zone:
                method(self, *args, **kwargs)
                return True

            return False

        return wrapper

    return requires_access



def validation_log(name, zone):

    def log_access(method):

        def wrapper(self, *args, **kwargs):
            from src.model.model import DataStorage as ds

            res = method(self, *args, **kwargs)

            if res:
                ds.add_granted(self, f'Пользователь с именем {name} вошел в зону {zone}')

            ds.add_denied(self, f'Пользователю с именем {name} отказано в доступе в зону {zone}')

        return wrapper

    return log_access




