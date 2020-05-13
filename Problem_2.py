
import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    subdirectories=os.listdir(path)                             # Contains all the files and directories within the path
    path_list=list()                                            # Empty list to which all the paths will be added

    if len(subdirectories)==0:                                  # Base case if there are no files or sub directories within the path
        return path_list

    for item in subdirectories:
        item=os.path.join(path,item)
        if os.path.isfile(item) and item.endswith(suffix):      # if file containing '.c' is present, then add the path to the list
            path_list.append(item)
        if os.path.isdir(item):
            sub_pathList=find_files(suffix,item)                # Recurse to sub directories to find the file
            for file in sub_pathList:
                path_list.append(file)                          # Add result of recursion to the list
    return path_list
