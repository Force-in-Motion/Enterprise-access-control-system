import sys
from service.service import DataService as ds

class Processing:

    @staticmethod
    def on_close():
        """
        Закрывает приложение
        :return:
        """
        sys.exit()


    @staticmethod
    def converts_data_to_str(data) -> str:
        """
        Сортирует данные и преобразует в строки для вывода статистики
        :param data: dict
        :return: str
        """
        sorted_keys = sorted(data.keys())

        result_string = ""

        for key in sorted_keys:
            values = ', '.join(data[key])

            values = values.replace(', ', '\n')

            result_string += f"{values}\n"

        return result_string

