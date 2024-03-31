import os

def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


import json
import csv
import pickle

def save_results_to_json(results, filename):
    with open(filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)

def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as csv_file:
        fieldnames = results[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

def save_results_to_pickle(results, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(results, pickle_file)


directory = 'D:\GB\immPython\HomeWork'
results = traverse_directory(directory)

save_results_to_json(results, 'results.json')
save_results_to_csv(results, 'results.csv')
save_results_to_pickle(results, 'results.pkl')
