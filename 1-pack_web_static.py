#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local, hide
from datetime import datetime


def do_pack():
    """generates a tgz archiv"""
    try:
        now = datetime.now()
        filename = f'versions/web_static_{now.strftime("%Y%m%d%H%M%S")}.tgz'

        local('mkdir -p versions')
        local(f'tar -cvzf {filename} web_static')
        result = local(f'test -e {file_path} && echo "Found"', capture=True)
        return filename
    except:
        return None
