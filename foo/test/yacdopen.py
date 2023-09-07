import webbrowser
from foo.test.checkconfig import getuiport


def xdopen():
    try:
        port = getuiport()
        url = f"http://127.0.0.1:{port}/ui"
        webbrowser.open(url)
        return True
    except:
        return False
