import os
import re

def get_proc_file():
    cwd = os.getcwd()
    items  = os.listdir(cwd)
    proc_files = [item for item in items if os.path.isfile(cwd + '/' + item) and re.match('^proc[1-9]\d*.py$', item)]
    proc_files.sort(key = lambda obj : int(obj.split('.')[0].split('proc')[1]))
    return proc_files[-1]

if __name__ == '__main__':
    proc_module_name = get_proc_file().split('.')[0]
    m = __import__(proc_module_name)
    src = open(m.src_file_path, 'r')
    dst = open(m.dst_file_path, 'w')
    for line in src.readlines():
      for sub_line in m.proc(line):
        dst.write(sub_line)
    src.close()
    dst.close()
