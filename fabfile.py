#!/usr/bin/python3
from fabric.api import env, run

env.hosts= ['35.174.207.53', '54.237.227.188']

def do_test():
    run('pwd')
