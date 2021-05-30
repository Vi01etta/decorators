import datetime
import os


def logger(function):
    def new_func(*args, **kwargs):
        result = function(*args, **kwargs)
        with open('log.txt', 'a') as file:
            file.write(
                f'Дата и время вызова функции:{datetime.datetime.now()}, название функции: {function.__name__}, c аргументами:{args}, {kwargs}, результат: {result}\n')
        return result

    return new_func


def param_logger(filepath):
    logs_file_name = os.path.join(filepath, 'log.txt')

    def logger(function):
        def new_func(*args, **kwargs):
            result = function(*args, **kwargs)
            with open(logs_file_name, 'a', encoding='utf-8') as file:
                file.write(
                    f'Дата и время вызова функции:{datetime.datetime.now()}, название функции: {function.__name__}, c аргументами:{args}, {kwargs}, результат: {result}\n')
            return result

        return new_func

    return logger
