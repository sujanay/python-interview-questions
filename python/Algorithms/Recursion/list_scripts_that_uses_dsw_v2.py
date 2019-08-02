import os

all_files_list = []


def get_all_paths(start_path):
    files = os.listdir(start_path)
    for file_name in files:
        full_link = start_path + '/' + file_name

        if os.path.isdir(full_link) :
            get_all_paths(full_link)
        else:
            if file_name.endswith('.py'):
                with open(full_link, 'r') as f:
                    lines = f.read()

                # check if the script (.py file) has any substring '_v2_1' (which is to check the dsw v2 schemas)
                # or 'spark.sql' (because if .py file is using querying table then it will do so with 'spark.sql')
                if ('_v2_1' in lines) or ('spark.sql(' in lines):
                    all_files_list.append(full_link)

    return all_files_list


def save_files_list_to_txt(files_list):
    with open('dsw_v2_files_list.txt', 'w') as my_file:
        for each_line in files_list:
            my_file.write(each_line + '\n')


if __name__=='__main__':
    # Put your start path here
    start_path = "/Users/sujan.tamang/Documents/dsw_v2_to_v3"

    # get all file paths for scripts(.py) that uses dsw v2 table
    filesList = get_all_paths(start_path)

    # save the files paths list to csv
    save_files_list_to_txt(filesList)

    for path in filesList:
        print(path)
