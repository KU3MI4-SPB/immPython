import glob
from immPython.HomeWorks.HomeWork8.Task2.merge_json_files import merge_json_files

if __name__ == "__main__":
    json_files = glob.glob('employees*.json')
    merge_json_files(json_files, 'all_employees.json')