import pytest
from playwright.sync_api import Page
from pages.cart import Cart
from pages.pdp import ProductDetailsPage
from pages.home import HomePage
from pages.result import ResultPage

@pytest.fixture
def home_page(page:Page) -> HomePage:
    return HomePage(page)

@pytest.fixture
def result_page(page:Page) -> ResultPage:
    return ResultPage(page)

@pytest.fixture
def product_details_page(page:Page) -> ProductDetailsPage:
    return ProductDetailsPage(page)

@pytest.fixture
def cart(page:Page) -> Cart:
    return Cart(page)
