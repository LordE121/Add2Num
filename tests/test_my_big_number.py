import logging

from main import main
from my_big_number import MyBigNumber


def test_sample_from_requirement():
    assert MyBigNumber().sum("1234", "897") == "2131"


def test_different_lengths():
    assert MyBigNumber().sum("1000", "23") == "1023"


def test_final_carry():
    assert MyBigNumber().sum("999", "1") == "1000"


def test_very_large_numbers():
    assert (
        MyBigNumber().sum("123456789123456789", "987654321987654321")
        == "1111111111111111110"
    )


def test_zero_values():
    assert MyBigNumber().sum("0", "0") == "0"


def test_main_prints_sum(capsys):
    result = main("1234", "897")

    assert result == "2131"
    assert capsys.readouterr().out.strip() == "2131"


def test_main_reads_interactive_input(monkeypatch, capsys):
    answers = iter(["1234", "897"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(answers))

    result = main()

    assert result == "2131"
    assert capsys.readouterr().out.strip() == "2131"


def test_show_steps_writes_operation_logs(caplog):
    caplog.set_level(logging.INFO, logger="my_big_number")

    result = MyBigNumber(show_steps=True).sum("99", "1")

    assert result == "100"
    assert "Step 1: 9 + 1 + carry 0 = 10; write 0, next carry 1" in caplog.text
    assert "Result: 99 + 1 = 100" in caplog.text
