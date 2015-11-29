import os

if __name__ == '__main__':
  home = os.path.expanduser('~')
  keyword = raw_input('input keyword want to grep: \n')
  os.system("grep -r '{1}' {0}/*".format(home, keyword))
