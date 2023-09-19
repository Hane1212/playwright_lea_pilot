# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import os
import pytest

from pages.home import HomePage
from playwright.sync_api import Playwright, APIRequestContext, Page, expect
from typing import Generator


# ------------------------------------------------------------
# automationexercise fixtures
# ------------------------------------------------------------

@pytest.fixture
def home_page(page: Page) -> HomePage:
    return HomePage(page)


