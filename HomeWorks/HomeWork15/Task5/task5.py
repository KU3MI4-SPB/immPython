import os
import logging
from collections import namedtuple
import sys

logging.basicConfig(
    filename='dir_logging.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def collect_directory_info(directory):
    if not os.path.isdir(directory):
        logging.error(f"The path {directory} is not a valid directory.")
        return
    parent_directory = os.path.basename(directory)
    for entry in os.listdir(directory):
        entry_path = os.path.join(directory, entry)
        if os.path.isdir(entry_path):
            info = FileInfo(name=entry, extension='', is_directory=True, parent_directory=parent_directory)
            logging.info(f"Directory: {info}")
        else:
            name, extension = os.path.splitext(entry)
            info = FileInfo(name=name, extension=extension.lstrip('.'), is_directory=False,
                            parent_directory=parent_directory)
            logging.info(f"File: {info}")


def main():
    if len(sys.argv) != 2:
        print("Используйте команду: python task5.py <путь_к_каталогу>")
        return
    directory_path = sys.argv[1]
    collect_directory_info(directory_path)


if __name__ == '__main__':
    main()


# python task5.py C:\Users\KU3MI4\PycharmProjects\pythonProject\immPython

# Directory: FileInfo(name='.git', extension='', is_directory=True, parent_directory='immPython')
# 2024-12-23 17:10:02,264 - INFO - File: FileInfo(name='.gitignore', extension='', is_directory=False, parent_directory='immPython')
# 2024-12-23 17:10:02,264 - INFO - Directory: FileInfo(name='HomeWorks', extension='', is_directory=True, parent_directory='immPython')
# 2024-12-23 17:10:02,264 - INFO - Directory: FileInfo(name='OldLesson', extension='', is_directory=True, parent_directory='immPython')