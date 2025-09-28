# test_app.py
import urllib.request

def test_home_returns_200():
    with urllib.request.urlopen("http://127.0.0.1:5000/") as resp:
        assert resp.status == 200
