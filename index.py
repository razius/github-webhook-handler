#!/usr/bin/env python
import io
import os
import sys
import json
import subprocess
import requests
import ipaddress
from flask import Flask, request, abort

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    # Store the IP address blocks that github uses for hook requests.
    hook_blocks = requests.get('https://api.github.com/meta').json()['hooks']

    if request.method == 'GET':
        return ' Nothing to see here, move along ...'

    elif request.method == 'POST':
        # Check if the POST request if from github.com
        is_github = False
        for block in hook_blocks:
            ip = ipaddress.ip_address(u'%s' % request.remote_addr)
            if ipaddress.ip_address(ip) in ipaddress.ip_network(block):
                is_github = True
        if not is_github:
            abort(403)

        if request.headers.get('X-GitHub-Event') == "ping":
            return json.dumps({'msg': 'Hi!'})
        repo_name = json.loads(request.data)['repository']['name']
        repo_owner = json.loads(request.data)['repository']['owner']['name']
        repos = json.loads(io.open('repos.json', 'r').read())
        repo = repos.get('%s/%s' % (repo_owner, repo_name), None)
        if repo and repo.get('path', None):
	    if repo.get('action', None):
	        for action in repo['action']:
		    subprocess.Popen(action,
                             cwd=repo['path'])
	    else:
		subprocess.Popen(["git", "pull", "origin", "master"],
                             cwd=repo['path'])
        return 'OK'

if __name__ == "__main__":
    try:
        port_number = int(sys.argv[1])
    except:
        port_number = 80
    is_dev = os.environ.get('ENV', None) == 'dev'
    app.run(host='0.0.0.0', port=port_number, debug=is_dev)
