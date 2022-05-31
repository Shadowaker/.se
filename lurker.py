#!/usr/bin/env python3

import pyudev
import os
import sys


def main():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    monitor.start()

    for _ in iter(monitor.poll, None):
        # testing purposes
        os.system("open https://www.google.com")


if __name__ == '__main__':
    try:
        if sys.argv[1] == 'test':
            main()
    except IndexError:
        pass
    print("Online...")
