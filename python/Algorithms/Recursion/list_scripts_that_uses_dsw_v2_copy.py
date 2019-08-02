import os


def changeDir(path):
    #     new_dir = os.chdir(path)
    #     return new_dir
    pass


def isDir(path):
    return os.path.isdir(path)


def listFiles(path):
    return os.listdir(path)


all_files_list = []


def getAllPaths(start_path):
    files = listFiles(start_path)
    for file_name in files:
        full_link = start_path + '/' + file_name

        if isDir(full_link):
            getAllPaths(full_link)
        else:
            if file_name.endswith('.py'):
                all_files_list.append(full_link)

    return all_files_list


if __name__=='__main__':
    # Put your path here
    start_path = "/Users/sujan.tamang/Documents/dsw_v2_to_v3"

    # Put your file here you want to search (use "*.txt" / "*.png" / "*.exe" for WILDCARD search)
    print()
    filesList = getAllPaths(start_path)

    for path in filesList:
        print(path)