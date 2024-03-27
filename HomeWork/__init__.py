
import os

def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=[0, -1]):
    folder_path = os.path.dirname(os.path.abspath(__file__))

    file_list = os.listdir(folder_path)
    file_list.sort()

    counter = 1
    for file_name in file_list:
        if file_name.endswith("." + source_ext):
            new_name = desired_name + str(counter).zfill(num_digits) + "." + target_ext

            start_idx = name_range[0] if name_range[0] >= 0 else 0
            end_idx = name_range[1] if name_range[1] < 0 else len(file_name)
            original_name_part = file_name[start_idx:end_idx]

            if original_name_part:
                new_name = original_name_part + "_" + new_name

            os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))
            counter += 1
