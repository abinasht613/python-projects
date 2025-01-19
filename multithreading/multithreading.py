import threading
import time

def download_file(file_name, duration):
    """Simulates downloading a file."""
    print(f"Starting download: {file_name}")
    time.sleep(duration)  # Simulate the time taken to download
    print(f"Finished download: {file_name}")

def main():
    # Files to download with simulated durations (in seconds)
    files = [
        ("File_1.txt", 3),
        ("File_2.txt", 5),
        ("File_3.txt", 2),
        ("File_4.txt", 4),
    ]

    threads = []  # List to store threads

    # Create and start a thread for each file
    for file_name, duration in files:
        thread = threading.Thread(target=download_file, args=(file_name, duration))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("All downloads completed!")

if __name__ == "__main__":
    main()
