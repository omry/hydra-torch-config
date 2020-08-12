import pytest


@pytest.mark.parametrize("name,expected", ["tests.test_module.TestClass"])
def test_generate(name: str, expected: str):
    ...
