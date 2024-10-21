import robocore as rc
import time

def publisher():
    pub = rc.Publisher(topic="remote_sensor")
    for i in range(10):
        data = {'sensor': 'distance', 'value': i*10}
        pub.publish(data)
        print(f"Published: {data}")
        time.sleep(1)
    pub.close()

def subscriber():
    sub = rc.Subscriber(topic="remote_sensor")
    for _ in range(10):
        data = sub.receive()
        print(f"Received: {data}")
    sub.close()

if __name__ == "__main__":
    rc.start_servers()
    # On Device 1
    # threading.Thread(target=publisher).start()
    # On Device 2
    # threading.Thread(target=subscriber).start()
    # Use Tailscale for networking across devices
