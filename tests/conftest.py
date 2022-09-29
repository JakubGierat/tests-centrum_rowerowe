import pytest
from playwright.sync_api import Page

from pages.home import HomePage
from pages.result import ResultPage

@pytest.fixture
def home_page(page:Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def result_page(page:Page) -> ResultPage:
    return ResultPage(page)
