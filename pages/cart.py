import logging
from unicodedata import category
from playwright.sync_api import Page
from settings.fixtures import test_data
from settings.params import settings
import time

logging.basicConfig(level=logging.DEBUG)
Logger = logging.getLogger(__name__)

class Cart:

    def __init__(self, page: Page):
        self.page = page
        self.product_name = page.locator("p.name > a")
        self.product_price = page.locator("div.final-price")
        self.product_price_per_piece = page.locator("div.final-price > span.unit-price")
        self.part_summary = page.locator("div.prices > p > span.right")
        self.final_summary = page.locator("div.total-price-container > p > span")
        self.delivery_label = page.locator("span.delivery-label")
        self.select_bar = page.locator("select[name='QuantityList']")
        self.select_bar_options = page.locator("select[name='QuantityList'] > option")
        self.delete_btn = page.locator("a.gray")
        self.empty_cart_alert = page.locator("div.emptyCart > div > div > p")
        self.back_to_shopping_btn = page.locator("div.emptyCart > div > div > a")
    
    def product_name_text(self):
        return self.product_name.text_content().lower().strip(' ')

    def product_price_value(self):
        Logger.info("Cart price: {}".format(float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') for i in self.product_price.first.text_content().split('\n')]))))

        return float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') for i in self.product_price.first.text_content().split('\n')]))

    def part_summary_value(self):
        Logger.info("Cart summary price: {}".format(float(''.join([i.replace(' zł', '').replace(',', '.').replace(' ', '').strip(' ') for i in self.part_summary.first.text_content().split('\n')]))))

        return float(''.join([i.replace(' zł', '').replace(',', '.').replace(' ', '').strip(' ') 
        for i in self.part_summary.first.text_content().split('\n')]))

    def shipping_cost(self, test_data):
        return self.part_summary.nth(1).text_content().strip(' ').lower() == test_data['shippingCost']

    def final_summary_value(self):
        Logger.info("Summary total: {}".format(float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') for i in self.final_summary.text_content().split('\n')]))))

        return float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') for i in self.final_summary.text_content().split('\n')]))

    def increase_number_of_product_pieces(self):
        self.select_bar.wait_for()
        if self.select_bar.is_visible():
            self.select_bar.hover()
            self.select_bar.click()
            #self.select_bar_options.last.click()
            #self.select_bar.fill(self.select_bar_options.last.text_content().strip(' '))
            #Logger.info(self.select_bar_options.last.text_content())
            self.select_bar.select_option(self.select_bar_options.last.text_content().strip(' '))
            #self.select_bar.press(key='Enter')
            self.select_bar.click()
            self.product_price_per_piece.wait_for()
            #Logger.info(self.product_price_per_piece.text_content())
        else:
            pass

    def number_of_product_pieces(self):
        if self.select_bar.is_visible():
            return float(self.select_bar.input_value())
        else:
            return 1

    #def incresed_summary_value(self, test_data):
        self.final_summary.wait_for()
        Logger.info('Summary after increase: {}'.format(self.final_summary_value()))
        #Logger.info('3x product price: {}'.format((self.product_price_value() * self.increase_number_of_product_pieces(test_data))))
        return self.final_summary

    def delete_product(self, test_data):
        self.delete_btn.wait_for()
        self.delete_btn.hover()
        self.delete_btn.click()
        return self.empty_cart_alert.first.text_content().strip(' ') == test_data["emptyCartAlert"]

    def back_to_shopping_btn_click(self):
        self.back_to_shopping_btn.click()




    

