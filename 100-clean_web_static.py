#!/usr/bin/python3
"""
"""
from fabric.api import env, hide, local, run


#env.hosts = ['35.174.207.53', '54.237.227.188']
env.hosts = ['35.174.207.53']

def get_date(filename):
    return int(filename.split('.')[0].split('_')[-1])


def clean_local(number):
    with hide('commands'):
        res = local('ls versions', capture=True)
    files = res.split('\n');
    dates = [get_date(filename) for filename in files]
    dates = sorted(dates, reverse=True)[number:]

    for filename in files:
        if get_date(filename) in dates:
            local(f'rm -f versions/{filename}')

def clean_remote(number):
    path = '/data/web_static/releases/'
    with hide('running', 'stdout', 'stderr'):
        res = run(f'ls {path}')
    dirs = res.stdout.split(' ')
    dates = [get_date(dirname) for dirname in dirs if 'web_static' in dirname]
    dates = sorted(dates, reverse=True)[number:]

    for dirname in dirs:
        if 'web_static' in dirname and get_date(dirname) in dates:
            print(f'rm -rf {dirname}')


def do_clean(number=0):
    """"""
    number = int(number)
    if number == 0:
        number = 1
    #clean_local(number)
    clean_remote(number)
