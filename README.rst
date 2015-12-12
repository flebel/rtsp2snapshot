Flask app to display a snapshot from a RTSP feed.

WARNING
=======

This should not be exposed to unsafe or uncontrolled networks. Parts of the URL
is interpolated as is into a call to execute the `ffmpeg` binary. This can be
exploited by malicious individuals to perform unauthorized actions that could
compromise the integrity of the system.

The overhead from executing `ffmpeg` is costly, and therefore it is not
recommended to perform more than one request every two seconds.

Getting started
===============

Requirements:

* flask
* ffmpeg

The `flask` Python requirement is expressed in the `requirements.txt` file and
may be installed by running the following command (preferably from a virtual
environment)::

    pip install -r requirements.txt

The `ffmpeg` binary should be installed through your system's package
manager, or compiled from source.

Usage
=====

Execute the script to start a debugging server listening on `localhost:5000`,
or serve through WSGI. Pass the URI to the RTSP feed as the resource, without
the protocol prefix. For example,

    http://localhost:5000/192.168.0.10:554/user=admin&password=&channel=1&stream=0.sdp?real_stream

Everything past the port and slash will be used to connect to the RTSP feed,
and prefixed with `rtsp://`.

