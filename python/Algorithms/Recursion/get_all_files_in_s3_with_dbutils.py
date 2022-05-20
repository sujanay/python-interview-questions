def get_all_paths(start_path):
  all_file_paths_list = []
  def get_all_paths_inner(start_path):
    file_paths = [path[0] for path in dbutils.fs.ls(start_path)]
    for path in file_paths:
      if not path.endswith("/"):
        all_file_paths_list.append(path)
      else:
        get_all_paths_inner(path)
    return all_file_paths_list
  
  return get_all_paths_inner(start_path)

all_file_paths = get_all_paths("...")
