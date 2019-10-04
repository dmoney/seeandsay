#!/usr/bin/env python3

import subprocess, sys, datetime
import lookandsay

if __name__ == '__main__':
    for runtype in lookandsay.RUNTYPES:
        print(f"running: {runtype}")
        before = datetime.datetime.now()
        subprocess.run(f"python3 lookandsay.py {runtype} 1223334444 45".split(),
            stdout=subprocess.DEVNULL
            )
        after = datetime.datetime.now()
        print(f"Realtime: {after - before}\n")
