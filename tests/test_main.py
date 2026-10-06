# tests/test_main.py
from main import main


def test_main_runs(capsys):
    main()
    assert "Hello from life-os!" in capsys.readouterr().out
