import turtle
import random
from zipfile import sizeEndCentDir

# 设置画布和初始参数
screen = turtle.Screen()
screen.title("圣诞树")
screen.bgcolor("black")  # 黑色背景，突出圣诞树
screen.setup(width=800, height=600)

# 配置颜色模式支持RGB
turtle.colormode(255)

# 创建绘图对象
tree = turtle.Turtle()
tree.speed(0)  # 最快速度绘制
tree.hideturtle()
tree.penup()
tree.goto(0, -250)  # 从底部开始绘制
tree.setheading(90)  # 向上绘制
tree.pendown()

# 装饰颜色列表
ornament_colors = [
    (255, 0, 0),  # 红色
    (0, 255, 0),  # 绿色
    (0, 0, 255),  # 蓝色
    (255, 255, 0),  # 黄色
    (255, 165, 0),  # 橙色
    (128, 0, 128),  # 紫色
    (255, 192, 203)  # 粉色
]

def draw_moon(x, y):
    """绘制月亮"""
    tree.penup()
    tree.goto(x, y)
    tree.color(255, 215, 0)  # 金色月


    # 绘制⚪
    tree.pendown()
    tree.begin_fill()
    tree.circle(100)
    tree.end_fill()

    tree.penup()
    tree.goto(x+40, y+40)
    tree.color(0, 0, 0)  # 黑色月
    tree.pendown()
    tree.begin_fill()
    tree.circle(80)
    tree.end_fill()

def draw_star(x, y):
    """绘制星星"""
    tree.penup()
    tree.goto(x, y)
    tree.setheading(0)
    tree.color(255, 215, 0)  # 金色星星
    tree.pendown()
    tree.begin_fill()

    # 绘制五角星
    for _ in range(5):
        tree.forward(9)
        tree.right(144)

    tree.end_fill()


def draw_stars():
    """绘制星星们"""
    for _ in range(30):
        x = random.randint(-980, 980)
        y = random.randint(300, 680)
        draw_star(x, y)

def draw_snowflake(x, y):
    """绘制雪花"""
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    tree.color(255, 255, 255)  # 白色雪花
    tree.pensize(1)

    # 简单的雪花形状
    for _ in range(6):
        tree.forward(5)
        tree.backward(5)
        tree.right(60)

    tree.pensize(2)  # 恢复画笔大小

def draw_snow():
    """绘制背景雪花"""
    for _ in range(300):
        x = random.randint(-980, 980)
        y = random.randint(-850, 880)
        draw_snowflake(x, y)


def draw_ornament(x, y):
    """在指定位置绘制圣诞装饰"""
    tree.penup()
    tree.goto(x, y)
    tree.pendown()

    # 随机选择装饰颜色
    color = random.choice(ornament_colors)
    tree.color(color)

    # 绘制圆形装饰
    tree.begin_fill()
    tree.circle(random.randint(3, 6))
    tree.end_fill()


def draw_branch(length,depth):
    """递归绘制树枝"""
    # 设置树枝颜色和粗细
    if depth > 6.9:
        # 较粗的树枝用深绿色
        tree.color(139, 69, 19)
        tree.pensize(depth // 2)
        tree.forward(length)
    else:
        # 细枝用浅绿色
        tree.color(0, 180, 0)
        tree.pensize(depth // 2)
        # tree.pensize(max(1, depth // 2))
        tree.forward(length)

    # 绘制当前树枝
    # tree.color(0, 100, 0)
    # tree.right(40)
    # # tree.left(40)
    # tree.forward(length)
    # tree.left(40)


    # 递归终止条件
    if length > 10:
        #随机决定是否添加装饰
        if random.random() < 0.3 and depth < 6:
            draw_ornament(tree.xcor(), tree.ycor())

        angle = random.randint(40, 55)
        lengthh = random.uniform(0.6, 0.7) * length




        # 右分支
        tree.right(angle)
        draw_branch(lengthh, depth - 1)
        #draw_branch(lengthh)

        # 左分支
        tree.left( 2 * angle)
        draw_branch(lengthh, depth - 1)
        #draw_branch(lengthh)


        tree.right(angle)
        #tree.backward(length)

    # 绘制叶簇（在最细的枝条末端）
    if depth == 0:
        tree.color(0, 200, 0)
        tree.begin_fill()
        tree.circle(2)
        tree.end_fill()


    tree.penup()
    tree.backward(length)
    tree.pendown()


def draw_trunk(high,siz,poin):
    """绘制树干"""
    if high > 10:
        for _ in range(40, 10, -3):
            tree.penup()
            tree.setheading(90)
            tree.color(139, 69, 19)  # 棕色树干
            high1 = random.uniform(0.8, 0.88) * high
            siz1 =  random.uniform(0.8, 0.88) * siz
            poin1 = poin+1.2 * high1
            tree.goto(0, poin1)
            tree.pendown()
            tree.pensize(siz1)
            tree.forward(high1)

            tree.penup()
            tree.goto(0, poin1)
            tree.pendown()
            draw_branch(high1, 7)
            draw_trunk(high1, siz1,poin1)



# 绘制圣诞树

draw_stars()
draw_snow()
draw_moon( 300, 200)
draw_trunk(150,30,-600 )
# draw_branch(100, 7)   # 初始长度和递归深度


# 保持窗口打开
turtle.done()
