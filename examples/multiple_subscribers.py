import robocore as rc
import time
import threading

def publisher():
    pub = rc.Publisher(topic="sensor_data")
    for i in range(10):
        data = {'sensor': 'temperature', 'value': i}
        pub.publish(data)
        print(f"Published: {data}")
        time.sleep(1)
    pub.close()

def subscriber(name):
    sub = rc.Subscriber(topic="sensor_data")
    for _ in range(10):
        data = sub.receive()
        print(f"{name} Received: {data}")
    sub.close()

if __name__ == "__main__":
    rc.start_servers()
    threading.Thread(target=subscriber, args=("Subscriber 1",)).start()
    threading.Thread(target=subscriber, args=("Subscriber 2",)).start()
    threading.Thread(target=publisher).start()
