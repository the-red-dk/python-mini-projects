import os
import subprocess
import time

def git_init():
    subprocess.run(['git', 'init'])
    # time.sleep(1)
    subprocess.run(['git', 'add', '.'])
    
if __name__ == '__main__':
    git_init()
