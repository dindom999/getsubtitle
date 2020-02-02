#!/home/dom/anaconda3/bin/python
# coding: utf-8
import time
import os
from getsubtitle.main import GetSubtitles
import getsubtitle.constants as cons
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

path = "/data/mv/bt"

def get_this(name):
    file_ext = os.path.splitext(name)[1]
    print(name)
    if file_ext.lower() in cons.video_format_list:
        fn = os.path.basename(name)
        dirname = os.path.dirname(name)
        print(fn, dirname)
    
        GetSubtitles(
            name=fn,
            both=True,
            debug=True,
            downloader="subhd",
            sub_path=dirname,
            query=False,
            single=False,
            save_original=False,
            over=False,
            plex=False,
            sub_num=2
        ).start()


class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        get_this(event.src_path)

if __name__ == "__main__":
    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

