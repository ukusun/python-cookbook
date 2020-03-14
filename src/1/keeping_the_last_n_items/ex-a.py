from collections import deque

def search(lines, pattern, history = 5):
    previous_lines = deque(maxlen = history)
    for line in lines:
        previous_lines.append(line)
        if pattern in line:
            yield line, previous_lines


#example use on a somefile
if __name__ == '__main__':
    with open(r'D:\git_repo\python-cookbook\src\1\keeping_the_last_n_items\somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end = '')
            print(line, end = '')
            print('-'*20)
