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

    assert home_page.recommended_product_container_is_displayed()

    product_title = home_page.recommended_product_item_name()
    product_price = home_page.recommended_product_item_price()
    #product_endpoint = home_page.recommended_product_item_endpoint()

    home_page.recommended_product_item_click()

    assert product_details_page.product_name_head() == product_title

    assert product_details_page.product_price() == product_price

    product_details_page.add_to_cart()

    assert product_details_page.add_to_cart_alert_header_text(test_data)
    assert product_details_page.add_to_cart_alert_product_name_text() == product_title
    assert product_details_page.add_to_cart_alert_product_price_value() == product_price

    assert product_details_page.add_to_cart_alert_back_to_shopping_btn_visible()

    product_details_page.add_to_cart_alert_go_to_cart()

    expect(page).to_have_url(test_data["cartUrl"])

    assert cart.product_name_text() == product_title
    assert cart.product_price_value() == product_price

    assert cart.part_summary_value() == product_price

    assert cart.shipping_cost(test_data)

    cart.final_summary_value() == product_price

    cart.increase_number_of_product_pieces()

    assert cart.final_summary_value() == product_price*cart.number_of_product_pieces()

    assert cart.delete_product(test_data)

    cart.back_to_shopping_btn_click()

    assert product_details_page.product_name_head()

    #expect(page).to_have_url(test_data["Url"])



    



    