import pytest
from playwright.sync_api import Page, expect
from pages.home import HomePage
from pages.result import ResultPage
from settings.params import settings
from settings.fixtures import test_data

def test_main_menu_bar(page: Page, test_data: dict, home_page: HomePage, result_page: ResultPage):

    home_page.load()

    assert home_page.check_main_menu_bar_category_names(test_data)

    assert home_page.main_menu_bar_wrapper_is_visible()

    assert home_page.main_menu_bar_categories_btns_respond(test_data)