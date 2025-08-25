
import builtins
import io
import os
import tempfile
from pathlib import Path
import pytest

from file import modify_content, read_file, write_file, main


def test_modify_content():
    """Test that modify_content converts text to uppercase."""
    assert modify_content("Allan mboti") == "ALLAN MBOTI"
    assert modify_content("123 ALLAN") == "123 ALLAN"


def test_read_file(tmp_path):
    """Test that read_file correctly reads content from a file."""
    file_path = tmp_path / "test.txt"
    file_path.write_text("Sample content", encoding="utf-8")
    content = read_file(str(file_path))
    assert content == "Sample content"


def test_write_file(tmp_path):
    """Test that write_file correctly writes content to a file."""
    file_path = tmp_path / "output.txt"
    write_file(str(file_path), "allan mboti")
    assert file_path.read_text(encoding="utf-8") == "allan mboti"


def test_read_file_not_found():
    """Test that read_file raises FileNotFoundError for missing files."""
    with pytest.raises(FileNotFoundError):
        read_file("non_existent.txt")


def test_main_file_not_found(monkeypatch, capsys):
    """Test main function with missing file."""
    monkeypatch.setattr(builtins, "input", lambda _: "missing.txt")
    main()
    captured = capsys.readouterr()
    assert "error" in captured.out.lower()
