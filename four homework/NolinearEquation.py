import numpy as np
def f(x):
    """待求解的非线性方程"""
    return 2*np.sin(np.pi*x)-np.cos(np.pi*x)
def bisect(f,a,b,epson):
    """
    二分法求非线性方程的根
    :param f: 非线性方程
    :param a: 区间上限
    :param b: 区间下限
    :param epson: 精度
    :return: 迭代情况
    """
    c=(a+b)/2
    i = 1
    while abs(f(c))>=epson:
        if f(a)*f(c)>=0:
            a=c
        else:
            b=c
        print("第{}次迭代：误差为：{}".format(i,f(c)))
        c = (a + b) / 2
        i=i+1
    print("第{}次迭代：误差为：{}".format(i, f(c)))
    print("在第{}次迭代后，误差小于{}。".format(i,epson))
def f1(x):
    """
    待求根的非线性方程
    """
    return x**3-x-1
def g(x):
    """
    迭代函数 该迭代函数收敛阶数为二阶 收敛速度快
    """
    return (2*x**3+1)/(3*x**2-1)
def Fix_point(g,x,epson):
    """
    简单不动点函数求非线性方程组的根
    :param g: 迭代函数
    :param x: 起始点
    :param epson: 精度
    :return: 迭代的过程
    """
    i=1
    while abs(x-g(x))>=epson:
        print("第{}次迭代：x的值为{}，g(x)的值为{}，误差为{}".format(i,x,g(x),abs(x-g(x))))
        x=g(x)
        i=i+1
    print("第{}次迭代：x的值为{}，g(x)的值为{}，误差为{}".format(i, x, g(x), abs(x - g(x))))
    print("第{}次迭代后：误差为{}小于{}，满足迭代终止条件".format(i,  abs(x - g(x)),epson))
def secant(f,x0,x1,epson):
    """
    弦截法计算非线性方程组的根
    :param f: 待求非线性方程
    :param x0: 区间上限
    :param x1: 区间下限
    :param epson: 精度
    :return: 迭代情况
    """
    i=1
    x=x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
    while abs(f(x))>=epson:
        print("第{}次迭代：x的值为{}，f(x)的值为{}大于误差{}".format(i,x,f(x),epson))
        x0=x1
        x1=x
        x=x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
        i=i+1
    print("第{}次迭代：x的值为{}，f(x)的值为{}大于误差{}".format(i,x,f(x),epson))
    print("在第{}次迭代：x的值为{}，f(x)的值为{}小于误差{}，迭代结束。".format(i, x, f(x), epson))
def f2(x):
    """待求的非线性方程"""
    return x-np.cos(x)
def df(x):
    """对应的导数函数"""
    return 1+np.sin(x)
def Newton(f,df,x0,epson):
    """
    牛顿法求非线性方程组的根
    :param f: 非线性方程函数名
    :param df: 对应的导函数名
    :param x0: 初始值
    :param epson: 精度
    :return: 迭代情况
    """
    x=x0-f(x0)/df(x0)
    i=1
    while abs(x-x0)>=epson:
        print("第{}次迭代，此时x0的值为{}，与前次相比变化多少{}".format(i,x0,abs(x0-x)))
        x0 = x
        x=x0-f(x0)/df(x0)
        i=i+1
    print("第{}次迭代，此时x0的值为{}，与前次相比变化为{}".format(i, x0, abs(x0 - x)))
    print("在第{}次迭代，此时x0的值为{}，与前次相比变化为{}，满足迭代终止条件误差{}".format(i, x0, abs(x0 - x),epson))
if __name__ == '__main__':
    print("############这是简单不动点迭代情况#################")
    Fix_point(g, 1, 0.0000000001)
    print("############这是弦截法迭代情况#################")
    secant(f1, 1, 2, 0.000000000001)
    print("############这是二分迭代情况#################")
    bisect(f,0,1,0.01)
    print("############这是牛顿法迭代情况#################")
    Newton(f2,df,0.5,0.000000001)