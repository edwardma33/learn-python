import os
def clear():
    os.system("clear")
clear()

grid = []

for i in range(0, 10 + 1):
    grid.append([])

print(len(grid))

for i in range(0, len(grid)):
    for i in range(0, 11):
        grid[i].append("_")

def plot_point(x, y):
    grid[-y + len(grid)][x] = "o"
    

while input("Would you like to plot a point? [y/n]: ") == "y":
    plot_point(int(input("x: ")), int(input("y: ")))
    for i in grid:
        print(f"{i}")

