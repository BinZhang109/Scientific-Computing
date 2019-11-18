def classic_least_square(x_list,y_list):
    '''
    经典最小二乘法
    :param x_list: 输入点所有x的坐标
    :param y_list:
    :return:
    '''
    N=len(x_list)
    x_avg=sum(x_list)/N
    y_avg=sum(y_list)/N
    var_x,cov_xy=0.0
    for x,y in zip(x_list,y_list):
        temp=x-x_avg
        var_x+=temp**2
        cov_xy+=temp*(y-y_avg)
    a=cov_xy/var_x
    b=y_avg-a*x_avg
    return (a,b)
