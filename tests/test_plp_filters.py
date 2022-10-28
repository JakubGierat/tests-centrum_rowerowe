# Test Product listing page (PLP) filters
import pytest
from playwright.sync_api import Page, expect
from pages.cart import Cart
from pages.home import HomePage
from pages.result import ResultPage
from pages.pdp import ProductDetailsPage
from settings.params import settings
from settings.fixtures import test_data

def test_add_to_cart(page: Page, test_data: dict, home_page: HomePage, result_page: ResultPage, product_details_page: ProductDetailsPage, cart: Cart):
    
    home_page.load()

    assert home_page.popular_categories_container_is_displayed()

    #homepage_category_name = home_page.popular_categories_tile_name()

    #for nth_index in range(home_page.popular_categories_tiles_counter()):
    for nth_index in range(1,2):  

        homepage_category_name = home_page.popular_categories_tile_name(nth_index)

        home_page.popular_categories_tile_click(nth_index)
        
        for i in range(len(homepage_category_name)):
            assert homepage_category_name[i] in result_page.category_name_header_content()

        assert result_page.main_filters_container_visible()

        errors = result_page.sorting(test_data)
        assert len(errors) == 0, errors

        result_page.back_to_main_page_breadcrumb()

