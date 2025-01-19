import time
import smtplib
import logging
from watchdog.observers import Observer             # type: ignore
from watchdog.events import FileSystemEventHandler  # type: ignore

# Configure logging
logging.basicConfig(filename="monitor.log", level=logging.INFO, format="%(asctime)s - %(message)s") # Log to a file

# Email Alert Function
def send_email(subject, message):
    sender_email = "your_email@gmail.com"
    receiver_email = "admin@example.com"
    password = "your_email_password"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, receiver_email, email_message)

# Custom Log Event Handler
class LogFileHandler(FileSystemEventHandler):               # Inherit from the base class
    def on_modified(self, event):                           # Override the method
        if event.src_path == "./application.log":           # Check if the file is the target log file
            with open(event.src_path, "r") as file:         # Open the file in read mode
                lines = file.readlines()                    # Read all lines
                last_line = lines[-1] if lines else ""      # Get the last line or an empty string
                
                if "ERROR" in last_line:                    # Check for the keyword
                    logging.error(f"Critical Issue Found: {last_line.strip()}") #   Log the error
                    print("Error Detected! Sending Email Alert...")
                    #send_email("Log Alert: ERROR Detected", last_line.strip())

                elif "WARNING" in last_line:                            # Check for the keyword
                    logging.warning(f"Warning: {last_line.strip()}")    # Log the warning
                else:
                    print(f"Info: {last_line.strip()}")
                    logging.info(f"Info: {last_line.strip()}")
        else:
            print(f"File {event.src_path} has been modified.")

# Start Monitoring
if __name__ == "__main__":                                  # This is the entry point of the script
    path = "."                                              # Current directory
    event_handler = LogFileHandler()                        # Create an instance of the custom event handler
    observer = Observer()                                   # Create an observer object
    observer.schedule(event_handler, path, recursive=False) # Schedule the handler to watch the path
    observer.start()                                        # Start the observer

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:                               # Press Ctrl+C to stop the monitoring
        observer.stop()
    
    observer.join()
