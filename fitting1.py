import numpy as np
from scipy.linalg import solve
# 首先根据最小二乘法原理构造系数矩阵X,Y ，再根据系数矩阵求解线性方程组得出
# 线性方程租的解即为：拟合多项式的系数列表
# 解线性方程组用的是高斯消元法 通过Gauss消元原理一步步构造函数用来解线性方程组
# 自己构造的高斯消元不能满足计算 就调用scipy的solve方法来解线性方程组
def last_square_fit_curve_Gauss(xs,ys,order):
    X,Y=[],[]
    #求解偏导数矩阵，含有矩阵xi的系数矩阵X
    for i in range(0,order+1):
        X_line=[]
        for j in range(0,order+1):
            sum_xi=0.0
            for xi in xs:
                sum_xi+=xi**(i+j)
            X_line.append(sum_xi)
        X.append(X_line)
    #求解偏导数矩阵，含有矩阵yi的系数矩阵
    for i in range(0,order+1):
        Y_line=0.0
        for j in range(0,order+1):
            sum_xi_yi=0.0
            for k in range(len(xs)):
                sum_xi_yi+=xs[k]**i*ys[k]
            Y_line=sum_xi_yi
        Y.append(Y_line)
    x = solve(X, Y)
    return  x
    # return X,Y


#下面是根据高斯消元原理构造的函数

#构造增广矩阵
def arguemented_mat(a,b):
    return np.c_[a,b]
#行交换
def swap_row(a,i,j):
    m,n=a.shape
    if i>=m or j>=m:
        print('error:out of index...')
    else:
        a[i]=a[i]^a[j]
        a[j]=a[i]^a[j]
        a[i]=a[i]^a[j]
    return a

def trape_mat(sigma):
    m,n=sigma.shape
    #保存主元的所在的列数，一般来说，每行都有一个主元，除非某行全零
    main_factor=[]
    main_col=0
    while main_col<n & len(main_factor)<m:
        #当行数多于列数的时候，出现所有的列数已经处理完结束
        if main_col==n:
            break
        #阻列找主元，若该列全零(第i行往下)，则没有主元
        #当前查找小矩阵首行为所在原矩阵的行号
        first_row=len(main_factor)
        while main_col<n:
            new_col=sigma[first_row:,main_col]
            not_zeros=np.where(new_col>0)[0]
            #若该列没有非零值，则该列是非主元列
            if len(not_zeros)==0:
                main_col+=1
                break
            #否则通过行变换找到主元
            else:
                main_factor.append(main_col)
                index=not_zeros[0]
                #若首个元素(不是主元，需要航变换
                if index!=0:
                    sigma=swap_row(sigma,first_row,first_row+index)
                #把该主元下面的元素全部与、变为0
                if first_row<m-1:
                    for k in range(first_row+1,m):
                        times=float(sigma[k,main_col])/sigma[first_row,main_col]
                        sigma[k]=sigma[k]-sigma[k]*times
            main_col+=1
            break

    return sigma,main_factor

def back_solve(sigma,main_factor):
    #判断是否有解
    if len(main_factor)==0:
        print("wrong main_factor...")
        return None
    m,n=sigma.shape
    if  main_factor[-1]==n-1:
        print('no answer...')
        return None
    #把所有主元元素上方的元素变成0
    for  i  in range(len(main_factor)-1,-1,-1):
        factor=sigma[i,main_factor[i]]
        sigma[i]=sigma[i]/float(factor)
        for j in range(i):
            times=sigma[j,main_factor[i]]
            sigma[j]=sigma[j]-float(times)*sigma[i]
    return sigma
def print_result(sigma,main_factor):
    if sigma is  None:
        print("no answer...")
        return
    m,n=sigma.shape
    result=['']*(n-1)
    main_factor=list(main_factor)
    for i in range(n-1):
        #如果不是主元列，则为自由变量
        if i not in main_factor:
            result[i]='X_'+str(i+1)+'(free var)'
        #否则是主元变量从对应的行将主元变量表示成非主元变量的线性组合
        else:
            #row_of_main 表示该主元所在的行
            row_of_main=main_factor.index(i)
            result[i]=str(sigma[row_of_main,-1])
            for j  in  range (i+1,n-1):
                ratio=sigma[row_of_main,j]
                if ratio>0:
                    result[i]=result[i]+'-'+str(ratio)+'X_'+str(j+1)
                if ratio<0:
                    result[i]=result[i]+'+'+str(-ratio)+'X_'+str(j+1)
    return result

# 得到简化的阶梯矩阵和主元列
def solve1(a,b):
    sigma = arguemented_mat(a,b)
    print ('增广矩阵为：')
    print (sigma)
    sigma, main_factor = trape_mat(sigma)
    sigma = back_solve(sigma, main_factor)
    print ('方程的简化阶梯矩阵:')
    print (sigma)
    print ('方程的主元列为：')
    print (main_factor)
    print_result(sigma, main_factor)

if __name__ == '__main__':
    xs=[19,25,31,38,44]
    ys=[19.0,32.3,49.0,73.3,97.8]
    print(last_square_fit_curve_Gauss(xs,ys,5))
    # print(type(X))
    # print(arguemented_mat(np.array(X),np.array(Y)))
    # print('\n')
    # print(Y)
