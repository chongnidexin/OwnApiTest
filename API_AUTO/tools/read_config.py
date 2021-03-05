import configparser


class ReadConfig:

    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]


if __name__ == '__main__':
    from tools import project_path

    print(type(ReadConfig.get_config(project_path.case_config_path, 'MODE', 'mode')))
