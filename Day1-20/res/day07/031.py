"""
 功能简介：双色球选号升级版
 Version: 1.0
 Author : 谭小品
 """
import random
red_balls = [i for i in range(1,34)]
bule_balls = [i for i in range(1,17)]
selected_balls = random.sample(red_balls,6)
selected_balls.sort()
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
blue_ball = random.choice(bule_balls)

print(f'\033[034m{blue_ball:0>2d}\033[0m', end=' ')












