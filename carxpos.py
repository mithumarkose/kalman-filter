import random
import numpy as np
import random
from numpy import *
import matplotlib.pyplot as plt

np.seterr(divide='ignore', invalid='ignore')

previous_state=np.array([[4000],[280]])
i=1
time_intrvl=1
previous_pos_err=20
previous_vel_err=5
accel=np.array([[2]])
t_list=[i]
disp_list=[4000]
vel_list=[280]
kal_disp=[4000]
kal_vel=[280]
M_vel=[280]
M_disp=[4000]
A=np.array([[1,time_intrvl],[0,1]])

H=np.array([[1,0],[0,1]])
Q=np.array([[0.1,0.1],[0.1,0.1]])
C=np.array([[1,0],[0,1]])
R=np.array([[625,0],[0,36]])
B=np.array([[(time_intrvl*time_intrvl)/2],[time_intrvl]])
previous_conv=np.array([[previous_pos_err*previous_pos_err,0],[0,previous_vel_err]])
M=H.transpose()
At=A.transpose()
print(H)
while(i<50):

    pr_temp=np.matmul(A,previous_state)
    pr_temp2=np.matmul(B,accel)
    present_state=pr_temp+pr_temp2
    present_convtemp=(A*previous_conv)*At
    present_conv=present_convtemp+Q
    #print(present_conv)
    nume=(present_conv*M)
    deno=((H*present_conv)*M)+R
    kalman_gain=nume/deno
    m=isnan(kalman_gain)
    kalman_gain[m]=0
    #print(kalman_gain)

    m=random.random()
    Measured_pos=int(4000+(i*10)+(m*100))
    M_disp.append(Measured_pos)
    disp_list.append(4000+(i*10))
    Measured_vel=int(280+i+(m*20))
    M_vel.append(Measured_vel)
    vel_list.append(280+i)
    Y=np.array([[Measured_pos],[Measured_vel]])
    Measured_mat=np.matmul(H,Y)

    E=np.matmul(H,previous_state)
    J=Measured_mat-E
    present_temp=np.matmul(kalman_gain,J)
    present_state=previous_state+present_temp
    print(present_state)
    kal_vel.append(present_state[1][0])
    kal_disp.append(present_state[0][0])
    previous_conv=present_conv
    previous_state=present_state

    i=i+1
    t_list.append(i)

plt.subplot(2,1,1)
plt.plot(t_list,vel_list,color='blue',label='Actual Velocity')
plt.plot(t_list,kal_vel,'ro')
plt.plot(t_list,M_vel,color='green')
plt.subplot(2,1,2)
plt.plot(t_list,kal_disp,'go')
plt.plot(t_list,M_disp, color='violet')
plt.plot(t_list,disp_list,color='yellow')
plt.show()
