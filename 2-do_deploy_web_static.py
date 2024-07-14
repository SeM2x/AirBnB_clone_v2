#!/usr/bin/python3
"""pack and deploy content to server
"""
from fabric.api import env, run, put, local
import os

env.hosts = ['100.25.163.188', '34.203.77.186']


def do_deploy(archive_path):
    """deploy package to remote server
    Arguments:
        archive_path: path to archive to deploy
    """
    if not archive_path or not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp')

    file_name = archive_path.split('/')[-1]
    dir_name = file_name.split('.')[0]

    try:
        run('mkdir -p /data/web_static/releases/{}/'.format(dir_name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
                file_name, dir_name
        ))
        run('rm /tmp/{}'.format(file_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
                dir_name, dir_name
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            dir_name
        ))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(
            dir_name
        ))
        print("New version deployed!")
        return True
    except:
        return False
