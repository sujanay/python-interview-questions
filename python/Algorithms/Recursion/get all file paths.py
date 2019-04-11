import os


# change the directory when a path is supplied
# similar to ~cd command
def changeDir(path):
    new_dir = os.chdir(path)
    return new_dir


# should return True / False
def isDir(path):
    """ returns 'True' if the given path is a Directory """

    return os.path.isdir(path)


# list all files in the given folder path
# similar to ~ls command
def listFiles(path):
    """ Return a list containing the names of the entries in the directory given by path """

    return os.listdir(path)


# func getallpath(fileName):
# return list containg all the path of the files
all_files_list = []
def getAllPaths(start_path, filename):
    """ returns all the file paths that matches the file 'filename' """
    files = listFiles(start_path)
    for file_name in files:
        full_link = start_path + '/' + file_name

        if isDir(full_link):
            getAllPaths(full_link, filename)
        else:
            if file_name == filename:
                all_files_list.append(full_link)
    return all_files_list

start_path = "S:/recursive practice/newfolder"
filename = "sample.txt.txt"

print(getAllPaths(start_path, filename))