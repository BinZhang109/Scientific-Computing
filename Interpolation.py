import numpy as np
import matplotlib.pyplot as plt
def lagrange(x,y,u):
    '''
    拉格朗日插值函数
    :param x: 所有输入点的x坐标 类型nparray
    :param y: 所有输入点的y的坐标 类型nparray
    :param u: 测试点x坐标
    :return:  测试点y坐标
    '''
    result=0.0
    for i in range(len(y)):
        t=y[i]
        for j in range(len(x)):
            if i!=j:
                t*=(u-x[j])/(x[i]-x[j]) #拉杆格朗日核心代码
        result+=t
    return result
def get_diff_table(x,y):
    '''
        求差函数
        :param x: 所有输入点的x坐标 类型nparray
        :param y: 所有输入点的y的坐标 类型nparray
        :return:  差商矩阵
    '''
    n=len(x)
    A=np.zeros([n,n])
    for i in range(n):
        A[i,0]=y[i]
    for j in range(1,n):
        for i in range(j,n):
            A[i,j]=(A[i,j-1]-A[i-1,j-1])/(x[i]-x[i-j])
    return A
def netwon(x,y,u):
    '''
        牛顿插值函数
        :param x: 所有输入点的x坐标 类型nparray
        :param y: 所有输入点的y的坐标 类型nparray
        :param u: 测试点x坐标
        :return:  测试点y坐标
    '''
    sum=y[0]
    n=len(x)
    temp=np.zeros([n,n])
    for i in range(0,n):
        temp[i,0]=y[i]
    temp_sum=1.0
    for i in range(1,n):
        temp_sum=temp_sum*(u-x[i-1])
        for j in range(i,n):
            temp[j,i]=(temp[j,i-1]-temp[j-1,i-1])/(x[j]-x[j-i])
        sum+=temp_sum*temp[i,i]
    return sum
def piecewise_linear(x,y,u):
    '''
        分段线性插值函数
        :param x: 所有输入点的x坐标 类型nparray
        :param y: 所有输入点的y的坐标 类型nparray
        :param u: 测试点x坐标
        :return:  测试点y坐标
    '''
    if u in x:
        return y[u]
    else:
        index=0
        for i in range(len(x)):
            if u>=x[i] & u<=x[i+1]:
                index=i
                break
        result =y[index]*(u-x[index+1])/float((x[index]-x[index+1]))+y[index+1]*(u-x[index])/float(x[index+1]-x[index])
    return result
def segmentation_twice(x,y,u):
    '''
        分段二次插值函数
        :param x: 所有输入点的x坐标 类型nparray
        :param y: 所有输入点的y的坐标 类型nparray
        :param u: 测试点x坐标
        :return:  测试点y坐标
    '''
    if u in x:
        return y[u]
    else:
        index=0
        for i in range(len(x)):
            if u>=x[i] & u<=x[i+2]:
                index=i
                break
        result=y[index]*(u-x[index+1])*(u-x[index+2])/float((x[index]-x[index+1])*(x[index]-x[index+2]))+\
               y[index+1]*(u-x[index])*(u-x[index+2])/float((x[index+1]-x[index])*(x[index+1]-x[index+2]))+\
               y[index+2]*(u-x[index])*(u-x[index+1])/float((x[index+2]-x[index])*(x[index+2]-x[index+1]))
    return result
def plot(x,y,func,nums):
    '''
    绘图函数
    :param x: 输入点所有x的坐标
    :param y: 输入点所有y的坐标
    :param func: 插值函数
    :param nums: 分割点个数
    :return: 绘制的函数图像
    '''
    area=[min(x),max(x)]
    X=[area[0]+1.0*i*(area[1]-area[0])/nums  for i in range(nums)]
    X[len(X)-1]=area[1]
    Y=[func(x,y,u) for u in X]
    plt.plot(X,Y,label='result')
    for i in range(len(x)):
        plt.plot(x[i],y[i],'ro',label='point')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    x=np.array([2,4,6,8,10])
    y=np.array([0,3,5,4,1])
    result=lagrange(x,y,5)
    print("拉格朗日插值函数计算结果：\n",result)
    diff_table=get_diff_table(x,y)
    print("差商矩阵如下：\n",diff_table)
    result_newton=netwon(x,y,5)
    print("牛顿插值函数计算结果：\n",result_newton)
    result_piecewise=piecewise_linear(x,y,5)
    print("分段线性插值函数计算结果：\n",result_piecewise)
    result_segmenttation=segmentation_twice(x,y,5)
    print("分段二次插值函数计算结果：\n",result_segmenttation)
    plot(x,y,netwon,10)
    #plot(x,y,lagrange,10)
    # plot(x,y,piecewise_linear,10)
    # plot(x,y,segmentation_twice,10)

