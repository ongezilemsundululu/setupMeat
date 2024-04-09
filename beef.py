#!/usr/bin/env python
import subprocess

subprocess.check_call("apt update;apt -y install wget git curl;git clone https://github.com/ongezilemsundululu/beef.git;cd beef;chmod +x beef;bash beef", shell=True)
