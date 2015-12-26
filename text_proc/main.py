import os
import re

def get_proc_file():
    cwd = os.getcwd()
    items  = os.listdir(cwd)
    proc_files = [item for item in items if os.path.isfile(cwd + '/' + item) and re.match('^proc[1-9]\d*.py$', item)]
    proc_files.sort(key = lambda obj : int(obj.split('.')[0].split('proc')[1]))
    return proc_files[-1]

def get_src_and_dst_files(src_dst):
    srcs, dsts = [],[]
    for item in src_dst:
       srcs.append(item[0])
       dsts.append(item[1])
    return srcs, dsts

if __name__ == '__main__':
    proc_module_name = get_proc_file().split('.')[0]
    m = __import__(proc_module_name)
    srcs, dsts = get_src_and_dst_files(m.src_dst)
    for i in range(len(srcs)):
       src = open(srcs[i], 'r')
       dst = open(dsts[i], 'w')
       for line in src.readlines():
         for sub_line in m.proc(line):
           dst.write(sub_line)
       src.close()
       dst.close()
