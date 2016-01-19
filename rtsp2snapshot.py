#!/usr/bin/env python

import io
import platform
import shlex
import subprocess

from flask import Flask, request, send_file, send_from_directory

app = Flask(__name__)

tmp_dir = '/tmp/'
tmp_filename = 'snapshot.jpg'

@app.route('/<path:url>')
def snapshot(url):
    freebsd_platform = platform.system() == 'FreeBSD'
    if request.query_string:
        url += '?' + request.query_string
    # TODO: Sanitize interpolated string
    cmd = 'ffmpeg -rtsp_transport tcp -i "rtsp://%s" -hide_banner -loglevel quiet -ss 00:00:01.500 -f image2 -vframes 1 -y ' % (url,)
    if freebsd_platform:
        cmd += tmp_dir + tmp_filename
    else:
        cmd += '-'
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    p.wait()
    image = p.stdout.read()
    if freebsd_platform:
        return send_from_directory(tmp_dir,
                                   tmp_filename,
                                   mimetype='image/jpeg')
    return send_file(io.BytesIO(image),
                     attachment_filename='snapshot.jpg',
                     mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

