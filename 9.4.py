ignore = ["duplex", "alias", "configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.
    command - строка. Команда, которую надо проверить
    ignore - список. Список слов
    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    ignore_status = False
    for word in ignore:
        if word in command:
            ignore_status = True
    return ignore_status


def convert_config_to_dict(config_filename):
    config_dict = {}
    with open(config_filename) as f:
        for line in f:
            line = line.rstrip()
            if line and not (line.startswith("!") or ignore_command(line, ignore)):
                if line[0].isalnum():
                    section = line
                    config_dict[section] = []
                else:
                    config_dict[section].append(line.strip())
    return config_dict
config = convert_config_to_dict("config_sw1.txt")
print(*config, sep="\n")
