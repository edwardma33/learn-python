import os
import sys
os.system('clear')
os.chdir('../')

day_num = input('What day is it? ')

if len(day_num) != 0:
    new_dir = f"Day-{day_num}"
else:
    new_dir = input("Directory name: ")
    day_num = f'-{new_dir}'

def proj_name_format(proj_name):
    proj_name = [*proj_name]
    for i in proj_name:
        if i == " ":
            proj_name[proj_name.index(i)] = "-"
    if proj_name[-3] == '.':
        for i in range(-3, 0):
            proj_name.pop(i)
    return "".join(proj_name).lower()

if input("Is this a project? [y/n]: ") == "y":
    new_file = f'{proj_name_format(input("What is the name of your project?: "))}.py'
    new_jup = f"proj-notes-{day_num}.ipynb"
else:
    new_file = 'main.py'
    new_jup = f"notes-{day_num}.ipynb"

os.system(f'mkdir {new_dir}')
os.chdir(f'./{new_dir}')
os.system(f'touch {new_jup} {new_file}')
os.system(f'echo "import os" > {new_file}')