from service.process import Processing
from service.service import DataService as ds


class LogStorage:
    """
    Управляет данными статистики ( записывает в базу или получает из нее )
    """
    def __init__(self):
        self.__data_log = Processing.get_log()

    def add_statistic(self, key, data) -> None:
        """
        Добавляет в базу статистики данные об успешных авторизациях пользователей
        :param data: Принимает данные в виде строки
        :return: None
        """
        if key not in self.__data_log:
            self.__data_log[key] = [data]

        else:
            self.__data_log[key].append(data)




    @property
    def granted(self) -> list[str]:
        return self.__data_log['granted']


    @property
    def denied(self) -> list[str]:
        return self.__data_log['denied']


    def save(self) -> None:
        """
        Перезаписывает в базу полученные данные, если файла нет - создает его
        :return: None
        """
        ds.write_data_log(self.__data_log)