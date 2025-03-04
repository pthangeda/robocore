# RoboCore

> [!Warning]
> This project is in early development stages and under active development. Breaking changes may occur frequently without notice. Use with caution.

**RoboCore** is a pure Python middleware for robotic communication, emphasizing simplicity, customizability, and ease of use. It enables high-bandwidth, low-latency communication suitable for streaming data like RGB-D arrays.

## Philosophy

`RoboCore` aims to lower the barrier to entry for robotic communication by providing an easy-to-use and highly customizable framework. The goal is to make sure that you can focus on your methods without worrying about the underlying communication complexities.

## Features

- **Publish/Subscribe Paradigm**: Simple string-based topics with support for multiple publishers and subscribers.
- **Centralized Key-Value Store**: A database-like system for storing and retrieving key-value pairs.
- **Automatic Server Initiation**: Servers for topic registry and key-value store start automatically in the background.
- **Visualization Tools**: Real-time data inspection and visualization using `rerun-sdk`.
- **Configuration Files**: Use `.yaml` files to specify topic types and additional info.

## Installation

```bash
pip install robocore
```

## Getting Started

### Simple Publish/Subscribe

```python
import robocore as rc

def publisher():
    pub = rc.Publisher(topic="camera_feed")
    pub.publish(data)  # Replace 'data' with your data
    pub.close()

def subscriber():
    sub = rc.Subscriber(topic="camera_feed")
    data = sub.receive()
    sub.close()
```

### Multiple Subscribers

Check out the example in the `examples` folder:

```bash
python examples/multiple_subscribers.py
```

### Robotic Manipulator Example

Simulate a robotic manipulator with multiple publishers and subscribers:

```bash
python examples/robotic_manipulator.py
```

### Cross-Device Communication

Use Tailscale for networking across devices:

- Install Tailscale on both devices.
- Run the publisher on one device and the subscriber on the other.
- Modify the `connect` method to use the Tailscale IP address.

## Configuration

Use a `.yaml` file to specify topic types and visualization settings:

```yaml
topics:
  - name: camera_feed
    type: image
    visualize: true
```

## Visualization

Integrate with `rerun-sdk` for real-time visualization:

```python
visualizer = rc.Visualizer(topics=["camera_feed"])
visualizer.start()
```

## Contributing

We will welcome contributions once the code development is stable. Please feel free to open an issue if you have any suggestions or feedback.

## Contact

For any feedback or queries, please contact the author at `contact@prny.me`

---

For more examples and detailed usage, please refer to the `examples` folder.