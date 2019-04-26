import os


class ConfigFile:
    """
        Класс для работы с конфигурациооными файлами
    """

    def __init__(self):
        print('---new object cf was created', id(self))
        self.config = self.get_config()
        self.hosts = self.get_hosts()

    # def is_config(self, filename):
    #     result = True if str(filename).endswith('cfg.txt') else False
    #     return result

    def get_list(self):

        """
            Получение списка с конфигурационными файлами во вложенной папке проекта /cfg
            простая проверка - файл должен быть текстовым заканчиваться на cfg.txt
            в перпективе можно написать проверку формата конфигурационного файла
            :return: список файлов конфигурации с указание папки
        """

        path = os.path.join(os.getcwd(), 'cfg')
        configs_list = []

        for filename in os.listdir(path):
            filename = os.path.join('cfg', filename)
            if str(filename).endswith('cfg.txt'):
                configs_list.append(filename)
        return configs_list

    # def menu(self):
    #
    #     print('Доступные конфигурации:')
    #     for i, path in enumerate(self.get_list(), 0):
    #         print(f'{i}\t{os.path.split(path)[1]}')
    #     return input("Введите номер выбранного конфига: ")

    def get_config(self):

        """
            Получение конфига для проведения теста
            :return: Список словарей {ip: "ip", description: "description"}
        """

        configs_list = self.get_list()
        config = []

        # рисуем меню

        print('Доступные конфигурации:')

        for i, path in enumerate(configs_list, 0):
            print(f'{i}\t{os.path.split(path)[1]}')

        while True:
            num_config = input("Введите номер выбранного конфига: ")
            if num_config.isdigit():
                num_config = int(num_config)
                if 0 <= num_config < len(configs_list):
                    break
                else:
                    print('Нет такого конгифига, Попробуйте снова.')
            else:
                print('Это не число. Попробуйте снова')

        # забираем конфиг из выбранного файла

        with open(configs_list[num_config], 'r', encoding='utf-8') as f:
            text_config = f.read().split()

        for line in text_config:
            if line.startswith('#') or line.startswith(';'):
                print(line, ' - it line was passed')
                pass
            else:
                print(line, ' - it line was added to config')
                config.append({'host': line.split(':')[0], 'description': line.split(':')[1]})

        return config

    def get_host_description(self, ip):

        """
            :param ip: ip  из конфига
            :return: описание задаенного ip
        """

        for host_line in self.config:
            if host_line['host'] == ip:
                return host_line['description']
        return 'no matches'

    def get_hosts(self):

        """
            формирует массив ip адресов для мониторинга из конфига
        """

        result = []
        for line in self.config:
            result.append(line['host'])
        return result

