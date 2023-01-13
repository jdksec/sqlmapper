import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    DIRECTORY_TO_WATCH = "./watcher/"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print ("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print("New file found")
            os.system("fname=%s; datenow=$(cat $fname |md5sum | cut -d ' ' -f 1); echo \"Scanned $datenow\"; cat $fname | sed 's/\r//' > scans/$datenow; tmux new-session -d -s $datenow \"~/Tools/sqlmap/sqlmap.py -r scans/$datenow --batch --random-agent --tamper=space2comment --banner| tee -a scans/$datenow;cat scans/$datenow > log.txt\"; /bin/mv $fname completed/$datenow" % event.src_path)

if __name__ == '__main__':
    if not os.path.exists('scans'):
        os.makedirs('scans')
    if not os.path.exists('completed'):
        os.makedirs('completed')
    if not os.path.exists('watcher'):
        os.makedirs('watcher')
    w = Watcher()
    w.run()

