import os 

from toolbox.load_shifting.run import run_load_shifting

if __name__ == '__main__':
    task = os.environ['TASK']
    if task == "load_shifting":
        run_load_shifting()