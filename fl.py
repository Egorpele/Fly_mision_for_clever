# coding: utf8

import rospy
from clover import srv
from std_srvs.srv import Trigger
from clover.srv import SetLEDEffect
rospy.init_node('flight')
set_effect = rospy.ServiceProxy('led/set_effect', SetLEDEffect)
get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)
r_1 == input("Введите цвет 1: ")
g_1 == input("Введите цвет 2: ")
b_1 == input("Введите цвет 3: ")
set_effect ( r = r_1 , g = g_1 , b = b_1 )
navigate(x=0, y=0, z=1, frame_id='body', auto_arm=True)
x_1 = input("Введите координату:" )
y_1 = input("Введите координату: ")
z_1 = input("Задайте высоту: ")
p = input("Введите время ожидания: ")
navigate ( x = x_1 , y = y_1 , z = z_1 , frame_id = 'aruco_map' )
rospy.sleep(p)
x_2 = input("Введите координату:" )
y_2 = input("Введите координату: ")
z_2 = input("Задайте высоту: ")
p_1 = input("Введите время ожидания: ")
navigate ( x = x_2 , y = y_2 , z = z_2 , frame_id = 'aruco_map' )
rospy.sleep(p_1)
x_3 = input("Введите координату:" )
y_3 = input("Введите координату: ")
z_3 = input("Задайте высоту: ")
p_2 = input("Введите время ожидания: ")
navigate ( x = x_3 , y = y_3 , z = z_3 , frame_id = 'aruco_map' )
rospy.sleep(p_2)
land()





