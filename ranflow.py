import os
import time
import random
from datetime import datetime

FAKE_KEY = "FAKE-KEY-123"
TARGET_DIRECTORY = "C:\\Users\\Public"
LOG_FILE = "operation_log.txt"

def simulate_operation(file_path):
    fake_key = generate_fake_key()
    print(f"[{get_timestamp()}] Simulating operation on {file_path} with key {fake_key}...")
    time.sleep(random.uniform(0.2, 1.0))

def generate_fake_key():
    return FAKE_KEY

def log_operation(file_path):
    with open(LOG_FILE, "a") as log:
        log.write(f"{get_timestamp()} - Processed: {file_path}\n")

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def display_fake_message():
    print("\n" + "="*60)
    print("!!! Your files have been processed !!!")
    print("All your important files are now handled.")
    print("To proceed further, contact support at FAKE-SUPPORT-ADDRESS-123")
    print(f"Processing Key: {generate_fake_key()}")
    print("="*60)

def scan_and_simulate(directory):
    print(f"Scanning directory: {directory}...")
    time.sleep(1)
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            simulate_operation(file_path)
            log_operation(file_path)

def simulate_network_communication():
    print("Connecting to remote system...")
    time.sleep(1.5)
    print("Sending operation logs to server: FAKE-SERVER-123...")
    time.sleep(1.5)
    print("Connection lost. Retrying...")
    time.sleep(1.5)
    print("Connection failed. Continuing offline.")

def main():
    print("Initializing operation...")
    time.sleep(2)
    simulate_network_communication()
    scan_and_simulate(TARGET_DIRECTORY)
    display_fake_message()
    print("\nOperation complete. Have a nice day.")

if __name__ == "__main__":
    main()