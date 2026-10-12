import copy

import pytest

from radar import config, i18n


@pytest.fixture(autouse=True)
def english():
    i18n.set_lang("en")


@pytest.fixture
def cfg(tmp_path):
    c = copy.deepcopy(config.DEFAULTS)
    c["_dir"] = tmp_path
    return c
