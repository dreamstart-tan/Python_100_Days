"""
 功能简介：双色球随机
 Version: 1.0
 Author : 谭小品
 """
import random
red_balls = list(range(1,101))
selected_balls = []
for _ in range(6):
    index = random.randrange(len(red_balls))
    selected_balls.append(red_balls.pop(index))
selected_balls.sort()
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m',end = ' ')
blue_ball = random.randrange(1,17)
print(f'\033[034m{blue_ball:0>d}\033[0m')












