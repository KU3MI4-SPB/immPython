import os
import shutil

# Создать тестовую папку
folder_name = "test_folder"
folder_path = os.path.join(os.getcwd(), folder_name)
if os.path.exists(folder_path):
    shutil.rmtree(folder_path)
os.makedirs(folder_path)

# Заполнить тестовую папку
file_name = "test1.txt"
file_path = os.path.join(folder_path, file_name)
with open(file_path, "w") as file:
    file.write("This is a test file.\n")


def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=[0, -1]):
    file_list = os.listdir(folder_path)
    file_list.sort()

    counter = 1
    for file_name in file_list:
        if file_name.endswith("." + source_ext):
            new_name = desired_name + str(counter).zfill(num_digits) + "." + target_ext

            start_idx = name_range[0] if name_range[0] >= 0 else 0
            end_idx = name_range[1] if name_range[1] < 0 else len(file_name)
            original_name_part = file_name[start_idx:end_idx]

            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))
            counter += 1

rename_files(desired_name="file_", num_digits=4, source_ext="txt", target_ext="txt")

folder_content = ""
files = os.listdir(folder_path)
files.sort()
separator = ", "
files_as_string = separator.join(files)
print(files_as_string)

shutil.rmtree(folder_path)
