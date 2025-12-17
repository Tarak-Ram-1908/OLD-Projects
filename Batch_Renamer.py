import os

print("\n\nYou can enter 'exit' at any moment to exit\n\n")

while True:
    folder_path = input("Enter the folder path containing files\t-\t")
    if folder_path.strip().lower() == 'exit':
        print("\n\t***Exiting Program***\n\n")
        break

    if not os.path.exists(folder_path):
        print("\t***Invalid Path***\n\n")
        continue

    print("1\t-\tAdd Prefix")
    print("2\t-\tAdd Suffix")
    print("3\t-\tSequence Rename (e.g., file_1, file_2)")
    
    user_choice = input("Enter your choice {1/2/3}\t-\t")
    if user_choice.strip().lower() == 'exit':
        print("\n\t***Exiting Program***\n\n")
        break

    input_text = input("Enter the text or base name\t-\t")
    if input_text.strip().lower() == 'exit':
        print("\n\t***Exiting Program***\n\n")
        break

    try:
        files = os.listdir(folder_path)
        count = 1
        
        for original_name in files:
            file_path = os.path.join(folder_path, original_name)
            if os.path.isdir(file_path):
                continue

            name_part, extension_part = os.path.splitext(original_name)

            if user_choice == '1':
                new_name = input_text + original_name
            elif user_choice == '2':
                new_name = name_part + input_text + extension_part
            elif user_choice == '3':
                new_name = input_text + "_" + str(count) + extension_part
                count += 1
            else:
                print("\tInvalid Choice\n")
                break

            os.rename(file_path, os.path.join(folder_path, new_name))
            print("Renamed: " + original_name + " -> " + new_name)

        print("\n\t***Renaming Successful***\n\n")

    except Exception as e:
        print("\tError: " + str(e) + "\n\n")