"""
 功能简介：双色球随机选号程序
 Version: 1.0
 Author : 谭小品
 """

import random
n = int(input('生成及注号码'))

red_balls = [i for i in range(1,34)]
blue_balls = [i for i in range(1,17)]

for _ in range(n):
    selected_balls = random.sample(red_balls,6)
    selected_balls.sort()
    for ball in selected_balls:
        print(f'\033[031m{ball}\033[0m',end= ' ')
    blue_ball = random.choice(blue_balls)
    print(f'\033[031m{ball:0>2d}\033[0m')








