"""
Написати програму, яка просканує кореневу папку вашого проєкту,
збереже у файл files_size.txt назви та розмір файлів,
і надрукує назву найбільшого файлу та його розмір.
"""

import os

largest_file_name = None
largest_file_size = 0

root_directory = input(r"Enter your directory")

with open("files_size.txt", "w") as file_sizes_file:
    for foldername, subfolders, filenames in os.walk(root_directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_size = os.path.getsize(file_path)

            file_sizes_file.write(f"{file_path}: {file_size} bytes\n")

            if file_size > largest_file_size:
                largest_file_size = file_size
                largest_file_name = file_path

if largest_file_name:
    print(f"Largest file: {largest_file_name}, Size: {largest_file_size} bytes")
else:
    print("There are no files in the project.")
