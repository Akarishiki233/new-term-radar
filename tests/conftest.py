import copy

import pytest

from radar import config, i18n


@pytest.fixture(autouse=True)
def english(monkeypatch):
    i18n.set_lang("en")
    monkeypatch.delenv("GOANYAPI_API_KEY", raising=False)   # the optional source is off unless a test turns it on


@pytest.fixture
def cfg(tmp_path):
    c = copy.deepcopy(config.DEFAULTS)
    c["_dir"] = tmp_path
    return c
