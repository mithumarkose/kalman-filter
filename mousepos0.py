from pynput.mouse import Controller
import time
import matplotlib.pyplot as plt
import random

mouse= Controller()

x_list=[]
y_list=[]
actual_list=[]
newX_list=[]
i=0


previous_prediction_error=1
previous_state=0



while(i<35):

    mouse_current=mouse.position
    m=random.random()
    measuredValue_errorX=(mouse_current[0]+(m*200))
    print(mouse_current[0])
    actual_list.append(mouse_current[0])
    x_list.append(measuredValue_errorX)
    actual_valueY=mouse_current[1]
    y_list.append(actual_valueY)
    time.sleep(0.2)

    present_state=1*previous_state
    current_prediction_error=previous_prediction_error

    kalman_gain=current_prediction_error/(current_prediction_error+0.1)
    print(kalman_gain)
    present_state=(previous_state+(kalman_gain*(measuredValue_errorX-previous_state)))
    newX_list.append(present_state)
    current_prediction_error=(1-kalman_gain)*previous_prediction_error

    previous_state=present_state
    previous_prediction_error=current_prediction_error
    i=i+1

print("x values")
print(x_list)
print("y values")
print(y_list)
print(newX_list)
plt.plot(x_list, y_list, color='blue')
plt.plot(newX_list,y_list,'ro')
plt.plot(actual_list,y_list, color='green')
plt.show()
