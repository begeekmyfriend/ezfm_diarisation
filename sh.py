# coding=utf-8

__author__ = 'hou'

import subprocess

def run(cmd, capture = False):
    out_stream = subprocess.PIPE if capture else None
    err_stream = subprocess.PIPE if capture else None

    print cmd
    p = subprocess.Popen(cmd, shell=True, stdout=out_stream, stderr=err_stream)
    (stdout, stderr) = p.communicate()

    stdout = stdout.strip() if stdout else ""
    stderr = stderr.strip() if stderr else ""

    return_code = p.returncode
    success = (return_code == 0)

    return Result(cmd, stdout, stderr, success, return_code)

class Result(object):
    def __init__(self, cmd, stdout, stderr, success, return_code):
        self.value = {}
        self.value.setdefault('cmd', cmd)
        self.value.setdefault('stdout', stdout)
        self.value.setdefault('stderr', stderr)
        self.value.setdefault('success', success)
        self.value.setdefault('return_code', return_code)

    def cmd(self):
        return self.value.get('cmd', '')

    def stdout(self):
        return self.value.get('stdout', '')

    def stderr(self):
        return self.value.get('stderr', '')

    def success(self):
        return self.value.get('success', False)

    def return_code(self):
        return self.value.get('return_code', -1)

    def __repr__(self):
        return self.value.__repr__()
