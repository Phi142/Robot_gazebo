#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float64

def callback_function1(message):
    # In giá trị nhận được từ bánh xe thứ nhất
    rospy.loginfo("Received wheel velocity 1: %s" % message.data)

    # Gửi giá trị vận tốc bánh xe thứ nhất tới chủ đề "/joint1_velocity_command"
    pub = rospy.Publisher('/my_diffbot/joint1_velocity_controller/command', Float64, queue_size=10)
    pub.publish(message.data)

def callback_function2(message):
    # In giá trị nhận được từ bánh xe thứ hai
    rospy.loginfo("Received wheel velocity 2: %s" % message.data)

    # Gửi giá trị vận tốc bánh xe thứ hai tới chủ đề "/joint2_velocity_command"
    pub = rospy.Publisher('/my_diffbot/joint2_velocity_controller/command', Float64, queue_size=10)
    pub.publish(message.data)

def subscriber():
    # Khởi tạo ROS node, đặt tên là "computer_subscriber"
    rospy.init_node("computer_subscriber")

    # Đăng ký subscriber với chủ đề "/wheel_velocity1" và callback function cho bánh xe thứ nhất
    rospy.Subscriber('/wheel_velocity1', Float64, callback_function1)

    # Đăng ký subscriber với chủ đề "/wheel_velocity2" và callback function cho bánh xe thứ hai
    rospy.Subscriber('/wheel_velocity2', Float64, callback_function2)

    rospy.spin()

if __name__ == "__main__":
    subscriber()

""" import rospy
from std_msgs.msg import Float64
def publisher():
    # Khởi tạo publisher tới chủ đề 
    joint1 = rospy.Publisher('/my_diffbot/joint1_velocity_controller/command', Float64, queue_size=10)
    joint2 = rospy.Publisher('/my_diffbot/joint2_velocity_controller/command', Float64, queue_size=10)
    # Tạo một thông điệp Float64
    message1 = Float64()
    message2 = Float64()

    rate = rospy.Rate(10)  # Tần suất gửi: 10Hz (mỗi 0.1 giây)

    while not rospy.is_shutdown():
        # Thiết lập giá trị vận tốc bánh xe
        message1.data = 1.5
        message2.data = -1.5

        # In giá trị mà publisher gửi
        rospy.loginfo("Publishing value: %s" % message1.data)
        rospy.loginfo("Publishing value: %s" % message2.data)
        # Gửi thông điệp tới chủ đề
        joint1.publish(message1)
        joint2.publish(message2)
        rate.sleep()

if __name__ == "__main__":
    # Khởi tạo nút, đặt tên là "continuous_publisher"
    rospy.init_node("continuous_publisher")
    publisher() """





    

