# coding=UTF-8
import os


# 合并path和name
def abspath(path, name):
    aaa = os.path.join(path, name)
    return aaa


# 检测list列表里是否有这个值，有的话删除
def rm_no_used_value_from_list(lists):
    value_willbe_rm = ['System Volume Information', '$RECYCLE.BIN', 'desktop.ini']
    for g in value_willbe_rm:
        while lists.count(g) != 0:
            lists.remove(g)
    return lists


# 检查路径的内容，返回两个列表files和列表folders
# 接收一个string，返回两个list(files，folders)
def check_folder(path):
    # folders存放文件夹名称，files存放文件名称
    files = []
    folders = []
    # 返回当前路径的全部文件
    all_file = os.listdir(path)
    # 在列表删除不需要的文件/夹 (windows系统文件夹或文件)
    rm_no_used_value_from_list(all_file)
    # 开始已all_file列表进行循环
    for i in all_file:
        # listdir返回的是"文件名"而不是路径，需要将传进来的路径和文件名拼起来
        i_path = abspath(path, i)
        # 开始判断
        # 列表files存文件，列表folders存文件夹
        # 这个地方存储的都是真实路径
        if os.path.isfile(i_path):
            files.append(i_path)
        elif os.path.isdir(i_path):
            folders.append(i_path)
    return files, folders


# 统计list里全部路径里的文件数量，返回字典
# 接收一个list，返回directory
def count_folders_files(folders):
    # 定义一个字典存储文件夹里文件夹里文件的数量
    file_directory_count = {}
    for i in folders:
        i_files, i_folders = check_folder(i)
        i_files_count = len(i_files)
        file_directory_count[i] = i_files_count
    return file_directory_count


# 判断文件名的扩展名
# 接受一个list，按扩展名统计总数，返回directory
def count_folders_files_by_ext(folders, ext):
    # 定义一个字典存储文件夹里文件夹里文件的数量
    file_directory_count = {}
    j_file = []
    # 判断ext的值第一位是不是.，是的话将.去掉
    if ext[0] == '.':
        ext = ext[1:]
    # 开始将传过来的folder里面的每一行的路径带入循环，删除非扩展名的值，最后统计
    for i in folders:
        i_files, i_folders = check_folder(i)
        for j in i_files:
            # j_extname存放扩展名，例如.exe，j_name没用
            j_name, j_extname = os.path.splitext(j)
            # lower将强制小写
            if j_extname[1:].lower() == ext:
                j_file.append(j)
        i_files_count = len(j_file)
        file_directory_count[i] = i_files_count
        j_file = []
    return file_directory_count


# 将用户输入的路径存入变量
inputfilepath = input('请输入路径：\n')
inputext = input('输入扩展名，按enter确认；如果无需指定扩展名，请直接按enter确认:\n')

# files存放当前目录的文件，folders存放当前目录的文件夹
files, folders = check_folder(inputfilepath)
# print('folders=%s' % folders)
# 如果inputext有值，执行count_folders_files_by_ext检查扩展名，否则执行count_folders_files
if inputext:
    directory = count_folders_files_by_ext(folders, inputext)
else:
    directory = count_folders_files(folders)
# 开始遍历字典输出
for i in directory:
    print(i, directory[i])
input('按任意键退出~~~')
