import app


class FakeResponse:
    status_code = 200


def test_fetch_returns_status_code(monkeypatch):
    monkeypatch.setattr(app.requests, "get", lambda url, timeout: FakeResponse())
    assert app.fetch("https://example.com") == 200
