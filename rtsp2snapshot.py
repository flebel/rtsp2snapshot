#!/usr/bin/env python

import io
import shlex
import subprocess

from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/<path:url>')
def snapshot(url):
    if request.query_string:
        url += '?' + request.query_string
    # TODO: Sanitize interpolated string
    cmd = 'ffmpeg -i "rtsp://%s" -hide_banner -loglevel quiet -ss 00:00:01.500 -f image2 -vframes 1 -y -' % (url,)
    p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    p.wait()
    image = p.stdout.read()
    return send_file(io.BytesIO(image),
                     attachment_filename='snapshot.jpg',
                     mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

