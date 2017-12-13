
# -*- coding : utf-8 -*-
# /usr/bin/python
# file Least_squares

import matplotlib.pyplot as plt  

def Least_squares():
    average_x = float(sum(X))//len(X)  
    average_y = float(sum(Y))/len(Y)  
    print (average_x,average_y)
    x_sub = [x-average_x for x in X]
    y_sub = [y-average_y for y in Y] 
    print (x_sub,y_sub)
    x_sub_pow2 = [x**2 for x in x_sub] 
    y_sub_pow2 = [y**2 for y in y_sub] 
    x_y = map((lambda x,y:x*y) , x_sub,y_sub)  
    a = float(sum(x_y)) / float(sum(x_sub_pow2))  
    b = average_y-a*average_x 
    
    result_plot(a,b)
    
def result_plot(a,b):
    
    plt.xlabel('X')  
    plt.ylabel('Y')  
    plt.plot(X, Y, '*')  
    plt.plot([0,15],[0*a+b,15*a+b])  
    plt.grid()  
    plt.show()      



if __name__ == '__main__':
    X =[1,2,3,5,6,12,11,13]  
    Y =[4,5,8,13,12,23,20,22] 
    
    Least_squares()
    
