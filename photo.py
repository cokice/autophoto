import os
import datetime
import shutil
import pathlib

# 脚本所在的目录
current_directory = pathlib.Path(__file__).parent

found_images = False

try:
    # 遍历当前目录及其所有子目录下的所有文件
    for item in current_directory.rglob('*'):

        # 打印所有遍历的文件
        print(f'Found item: {item.name}')

        # 如果是文件
        if item.is_file():

            # 仅处理图片文件（例如 .jpg, .png）
            if item.suffix in ['.JPG', '.ARW','.MP4','.DNG']:
                found_images = True

                try:
                    # 获取文件的创建时间
                    creation_time = item.stat().st_ctime
                except Exception as e:
                    print(f"Error getting creation time for {item}: {e}")
                    continue

                # 将创建时间转换为日期
                creation_date = datetime.date.fromtimestamp(creation_time)

                # 创建一个新的文件夹名称，该名称为创建日期
                new_folder = current_directory / creation_date.isoformat()

                # 打印出正在处理的文件以及目标文件夹
                print(f'Processing file: {item.name}, target folder: {new_folder}')

                try:
                    # 如果该文件夹不存在，则创建它
                    if not new_folder.exists():
                        print(f'Creating new directory: {new_folder}')
                        new_folder.mkdir()
                except Exception as e:
                    print(f"Error creating directory {new_folder}: {e}")
                    continue

                try:
                    # 将文件移动到新的文件夹中
                    shutil.move(str(item), new_folder / item.name)
                    print(f'Moved file: {item.name} to {new_folder}\n')
                except Exception as e:
                    print(f"Error moving file {item} to {new_folder}: {e}")
                    continue

    if not found_images:
        print("No .jpg or .png images found in directory.")
except Exception as e:
    print(f"Error processing directory: {e}")
