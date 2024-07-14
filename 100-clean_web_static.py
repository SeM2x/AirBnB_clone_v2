#!/usr/bin/python3
"""
deletes out-of-date archives, using the function do_clean
"""
from fabric.api import env, hide, local, run


env.hosts = ['100.25.163.188', '34.203.77.186']


def get_date(filename):
    """returns the date which the file is created at"""
    return int(filename.split('.')[0].split('_')[-1])


def clean_local(number):
    """cleans the versions folder"""
    with hide('commands'):
        res = local('ls versions', capture=True)
    files = res.split('\n')
    dates = [get_date(filename) for filename in files]
    dates = sorted(dates, reverse=True)[number:]

    for filename in files:
        if get_date(filename) in dates:
            local(f'rm -f versions/{filename}')


def clean_remote(number):
    """cleans /data/web_static/releases folder of both of your web servers"""
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
    """cleans local and both remote servers"""
    number = int(number)
    if number == 0:
        number = 1
    clean_local(number)
    clean_remote(number)
