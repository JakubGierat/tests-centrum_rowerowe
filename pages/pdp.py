# Product Details Page
import logging
from playwright.sync_api import Page
from settings.params import settings
import time

logging.basicConfig(level=logging.DEBUG)
Logger = logging.getLogger(__name__)

class ProductDetailsPage:

    def __init__(self, page: Page):
        self.page = page
        self.product_name_header = page.locator(".product-name > h1")
        self.product_price_value = page.locator(".price-box > .price-left > .main-price")
        self.add_to_cart_btn = page.locator("div.buy > a.gtm-add-to-cart-detail >> visible=true")
        self.add_to_cart_alert_header = page.locator("div.padding > div.header")
        self.add_to_cart_alert_product_name = page.locator("div.col > span.productName")
        self.add_to_cart_alert_product_price = page.locator("div.col > span.price")
        self.add_to_cart_alert_back_to_shopping_btn = page.locator("div.col > a.button")
        self.add_to_cart_alert_go_to_cart_btn = page.locator("div.col > form > a.button")

    def product_name_head(self):
        self.product_name_header.wait_for()
        #Logger.info(str(self.product_name_header.text_content()))
        return self.product_name_header.text_content().lower().strip(' ')

    def product_price(self):
        self.product_price_value.wait_for()

        Logger.info("PDP price: {}"
        .format(float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') 
        for i in self.product_price_value.first.text_content().split('\n')]))))

        return float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ')
        for i in self.product_price_value.first.text_content().split('\n')]))

    def add_to_cart(self):
        time.sleep(1.5)
        self.add_to_cart_btn.first.click()

    def add_to_cart_alert_header_text(self, test_data):
        return self.add_to_cart_alert_header.text_content().lower().strip(' ') == test_data["addToCartAlertHeader"]

    def add_to_cart_alert_product_name_text(self):
        return self.add_to_cart_alert_product_name.text_content().lower().strip(' ')

    def add_to_cart_alert_product_price_value(self):
        b = float(''.join([i.replace(' / szt.', '').replace('\xa0zł', '').replace(',', '.').replace(' ', '').strip('\t').strip(' ') for i in self.add_to_cart_alert_product_price.first.text_content().split('\n')]))

        Logger.info("Alert price: {}".format(b))
        return float(''.join([i.replace(' / szt.', '').replace('\xa0zł', '').replace(',', '.').replace(' ','').strip('\t').strip(' ') 
        for i in self.add_to_cart_alert_product_price.first.text_content().split('\n')]))

    def add_to_cart_alert_back_to_shopping_btn_visible(self):
        return self.add_to_cart_alert_back_to_shopping_btn.is_enabled()

    def add_to_cart_alert_go_to_cart(self):
        self.add_to_cart_alert_go_to_cart_btn.wait_for(state="visible")
        self.add_to_cart_alert_go_to_cart_btn.click()

    