import random
import time

def stop_and_wait(data):
    ack_received = True
    frame_number = 0
    i = 0
    while i < len(data):
        if ack_received:
            print(f"Sender: Sending frame {frame_number} -> {data[i]}")
            ack_received = False

        # Simulate transmission
        time.sleep(0.5)
        if random.random() < 0.8:  # 80% chance frame arrives
            print(f"Receiver: Frame {frame_number} received: {data[i]}")
            print(f"Receiver: Sending ACK {frame_number}")
            ack_received = True
            i += 1
            frame_number = 1 - frame_number
        else:
            print(f"Frame {frame_number} lost, retransmitting...")

# Example
data = "HELLO"
stop_and_wait(data)
