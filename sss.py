#!/bin/env python
# coding: utf-8
import sys
import time
import os
from getsubtitle.main import GetSubtitles
import getsubtitle.constants as cons
import subprocess

path = "/data/mv/bt"

def main(minutes= 120):
    cmd = "find %s -type f -amin -%s"%(path,minutes)
    rs = subprocess.check_output(cmd,shell=True)
    rs = rs.decode().split("\n")

    for name in rs:
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


if __name__ == "__main__":
    if len(sys.argv)>1:
        minutes = int(sys.argv[1])
    else:
        minutes = 60*24
    main(minutes)

