import numpy as np
#未实现牛顿-柯特斯和复化牛顿-柯特斯公式
def f(x):
    return np.exp(x**2)
def Trapezoid(a,b):
    """
    梯形求积公式
    :param a: 积分下限
    :param b: 积分上限
    :return:
    """
    return (b-a)*(f(a)+f(b))/2
def Simpson(a,b):
    """
    辛普森求积公式
    :param a: 积分下限
    :param b: 积分上限
    :return:
    """
    c=(a+b)/2
    result=(b - a) / 6 * (f(a) + f(b))
    result+=(b-a)/6*f(c)
    return  result

def Cotes(a,b):
    """
    柯特斯求积公式 4阶
    :param a: 积分下限
    :param b: 积分上限
    :return:
    """
    h=(b-a)/4
    x0,x1,x2,x3,x4=a,a+h,a+2*h,a+3*h,a+4*h
    return (b-a)*(7*f(x0)+32*f(x1)+12*f(x2)+32*f(x3)+7*f(x4))/190
def complex_trapzoid(a,b,n):
    """
    复化梯形积分公式
    :param a: 积分下限
    :param b: 积分上限
    :param n: 分割点个数
    :return: 积分值
    """
    h=(b-a)/n
    x=a
    s=f(a)+f(b)
    for k in range(1,n+1):
        x=x+h
        s=s+2*f(x)
    result=(h/2)*s
    return result
def complex_simpon(a,b,n):
    """
    复化辛普森积分公式
    :param a: 积分下限
    :param b: 积分上限
    :param n: 分割点个数
    :return: 积分值
    """
    h=(b-a)/n
    x=a
    s=f(x)+f(b)
    for k in range(1,n+1):
        x=x+h/2
        s=s+4*f(x)
        x=x+h/2
        s=s+2*f(x)
    result=(h/6)*s
    return result
if __name__ == '__main__':
    result=complex_simpon(0,1,10)
    print(result)


