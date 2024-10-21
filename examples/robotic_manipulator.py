import robocore as rc
import time
import threading

def joint_publisher():
    pub = rc.Publisher(topic="joint_states")
    for i in range(10):
        data = {'joint1': i, 'joint2': i*2}
        pub.publish(data)
        print(f"Published Joint States: {data}")
        time.sleep(0.5)
    pub.close()

def gripper_publisher():
    pub = rc.Publisher(topic="gripper_state")
    for i in range(10):
        data = {'gripper': 'open' if i % 2 == 0 else 'closed'}
        pub.publish(data)
        print(f"Published Gripper State: {data}")
        time.sleep(1)
    pub.close()

def control_subscriber():
    sub_joint = rc.Subscriber(topic="joint_states")
    sub_gripper = rc.Subscriber(topic="gripper_state")
    for _ in range(10):
        joint_data = sub_joint.receive()
        gripper_data = sub_gripper.receive()
        print(f"Control Received Joint: {joint_data}, Gripper: {gripper_data}")
    sub_joint.close()
    sub_gripper.close()

if __name__ == "__main__":
    rc.start_servers()
    threading.Thread(target=control_subscriber).start()
    threading.Thread(target=joint_publisher).start()
    threading.Thread(target=gripper_publisher).start()
