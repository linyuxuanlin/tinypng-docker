import tinify
import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("Received created event - %s." % event.src_path)
            source_path = event.src_path
            output_path = os.path.join(os.environ['OUTPUT_DIR'], os.path.basename(source_path))
            compress_image(source_path, output_path)

def compress_image(source_path, output_path):
    tinify.key = os.environ['TINYPNG_API_KEY']
    source = tinify.from_file(source_path)
    source.to_file(output_path)
    print(f"{source_path} compressed and saved to {output_path}")

if __name__ == "__main__":
    print("Watching for new images...")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.environ['INPUT_DIR'], recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
