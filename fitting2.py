import numpy as np
def init_fx_data():
    #待拟合曲线f(x)=sin2x*[(x^2-1)^3+0.5]
    xs=np.arange(-1,1,0.01)#200个点
    ys=[((x**2-1)**3+0.5)*np.sin(2*x) for x in xs]
    ys1=[]
    for i in range(len(ys)):
        z=np.random.randint(low=-10,high=10)/100 #加入噪点
        ys1.append(ys[i]+z)
    return xs,ys1
#计算最小二乘法当前的误差
def last_square_current_loss(xs,ys,A):
    error=0.0
    for i in range(len(xs)):
        y1=0.0
        for k in range(len(A)):
            y1+=A[k]*xs[i]**k
        error+=(ys[i]-y1)**2
    return error
#迭代解法：最小二乘法+梯度下降法
def last_square_fit_curve_Gradient(xs,ys,order,iternum=10000,learn_rate=0.001):
    A=[0.0]*(order+1)
    for r in range(iternum+1):
        for k in range(len(A)):
            gradient=0.0
            for i in range(len(xs)):
                y1=0.0
                for j in range(len(A)):
                    y1+=A[j]*xs[i]**j
                gradient+=-2*(ys[i]-y1)*xs[i]**k
            A[k]=A[k]-(learn_rate*gradient)#更新A[K]的梯度
        #检查误差变化
        if r%100==0:
            error=last_square_current_loss(xs=xs,ys=ys,A=A)
            print('最小二乘法+梯度下降法：第{}次迭代，误差下降为：{}'.format(r,error))
    return A
if __name__ == '__main__':
    xs,ys=init_fx_data()
    last_square_fit_curve_Gradient(xs,ys,10)

