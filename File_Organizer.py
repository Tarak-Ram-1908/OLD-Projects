import os
import shutil

print("\n\nYou can enter 'exit' at any moment to exit\n\n")

while True:
    directory_path = input("Enter the full path of the folder to organize\t-\t")
    
    if directory_path.strip().lower() == 'exit':
        print("\n\t***Exiting Program***\n\n")
        break

    if not os.path.exists(directory_path):
        print("\t***Invalid Path. Please try again.***\n\n")
        continue

    # Extension mapping
    extension_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Audio': ['.mp3', '.wav', '.aac'],
        'Archives': ['.zip', '.rar', '.7z']
    }

    try:
        files_list = os.listdir(directory_path)
        for file_name in files_list:
            source_file_path = os.path.join(directory_path, file_name)
            
            # Skip directories
            if os.path.isdir(source_file_path):
                continue

            # Get extension
            file_extension = os.path.splitext(file_name)[1].lower()
            
            moved = False
            for folder_name, extensions in extension_map.items():
                if file_extension in extensions:
                    target_folder = os.path.join(directory_path, folder_name)
                    
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    
                    shutil.move(source_file_path, os.path.join(target_folder, file_name))
                    print("Moved " + file_name + " to " + folder_name)
                    moved = True
                    break
            
            if not moved:
                others_folder = os.path.join(directory_path, "Others")
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(source_file_path, os.path.join(others_folder, file_name))
                print("Moved " + file_name + " to Others")

        print("\n\t***Organization Complete***\n\n")

    except Exception as error:
        print("\tAn error occurred: " + str(error) + "\n\n")