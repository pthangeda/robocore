import robocore as rc
import time

def publisher():
    pub = rc.Publisher(topic="camera_feed")
    for i in range(10):
        data = f"Frame {i}"
        pub.publish(data)
        print(f"Published: {data}")
        time.sleep(1)
    pub.close()

def subscriber():
    sub = rc.Subscriber(topic="camera_feed")
    for _ in range(10):
        data = sub.receive()
        print(f"Received: {data}")
    sub.close()

if __name__ == "__main__":
    rc.start_servers()
    import threading
    threading.Thread(target=subscriber).start()
    threading.Thread(target=publisher).start()
