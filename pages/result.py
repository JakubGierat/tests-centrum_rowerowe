from distutils.log import Log, error
from operator import itemgetter, attrgetter
from typing import Any
import pytest
from playwright.sync_api import Page
from pages.home import Logger
from settings.fixtures import test_data
from settings.params import settings

class ResultPage:

    def __init__(self, page:Page):
        self.page = page
        self.search_input = page.locator(".search-bar > input")
        self.search_button = page.locator("span[class='button orange jqSearch']")
        self.search_phrase_header = page.locator("div[class='searched-phrase hidden-xs']")
        self.item_container = page.locator(".item-container > .first-leyer")
        self.item_container_product_price = page.locator("div.price-delivery > span.final-price")
        self.item_container_product_name = page.locator("div.name > a.gtm-detail-link")
        self.item_container_product_rate = page.locator("div.rate > span.note")
        self.item_container_product_opinion = page.locator("div.opinions  p.counted")
        self.empty_input_text = page.locator(".empty-list-text > h2")
        self.remove_search_phrase_btn = page.locator("div[class='searched-phrase hidden-xs'] > form[action='ProductList/ProductList']:nth-child(2) > a")
        self.category_name_header = page.locator("div.description > h1")
        self.main_filters_container = page.locator("div.main-filters-container")
        self.breadcrumb_btn = page.locator("a[itemprop='item']")
        self.sortby_options_container_btn = page.locator("div.list-sort > div.jsFunc > div.option-list > div.dropdown")
        self.sortby_options_container_main_options = page.locator("span.sort")
        self.sortby_options_container_exact_options = page.locator("div.options-container > div.mobile-content > div.options > ul > li > div > form > a")
        self.page_number = page.locator("a.page-number")
        self.next_page_btn = page.locator("a.page-button")
        self.selected_page_number = page.locator("a[class='selected page-number']")
        self.dropdown_text = page.locator("div.list-sort > div > div.option-list > div.dropdown")
        
    # Type phrase in search input
    def type_phrase(self, phrase: str):
        self.search_input.type(phrase)

    # Click search button
    def search(self):
        self.search_button.click()

    # Check the search phrase header is visible
    def search_phrase_header_is_visible(self, phrase):
        return f'Szukasz: "{phrase}"' in self.search_phrase_header.text_content()

    # Check the number of tiles on the result page
    def number_of_tiles(self, test_data):
        return len(self.item_container.all_inner_texts()) <= test_data["numberOfResultTiles"]

    # Delete the value from search input
    def clear_search_input(self):
        self.search_input.fill('')

    # Check the empty input alert text
    def empty_input_alert_text(self, test_data):
        return self.empty_input_text.text_content() == test_data["emptyInputText"]

    # Check the search input contains fail phrase
    def search_input_contains_fail_phrase(self):
        return self.search_input.text_content() == ''

    # Click remove search phrase button (cross sign button next to search phrase header)
    def click_remove_search_phrase_button(self):
        self.remove_search_phrase_btn.wait_for()
        self.remove_search_phrase_btn.hover()
        self.remove_search_phrase_btn.click()
        
    # Check the all offers page is displayed
    def all_offers_page_is_displayed(self, test_data):
        Logger.info("Actual URL: {}, Expected: {}".format(self.page.url, test_data["offersUrl"]))
        self.page.wait_for_url(test_data["offersUrl"])
        Logger.info("Actual URL: {}, Expected: {}".format(self.page.url, test_data["offersUrl"]))
        return self.page.url == test_data["offersUrl"]
    
    def category_name_header_content(self):
        Logger.info(self.category_name_header.text_content().replace('\n', '').strip(' ').split(' '))
        return self.category_name_header.text_content().replace('\n', '').strip(' ').lower().split(' ')

    def main_filters_container_visible(self):
        Logger.info("Main filters cointainer is visible: {}".format(self.main_filters_container.is_visible()))
        return self.main_filters_container.is_visible()

    def back_to_main_page_breadcrumb(self):
        self.breadcrumb_btn.first.click()

    def expand_sortby_container_button_click(self):
        self.page.wait_for_load_state()
        self.sortby_options_container_btn.click()

    def item_price(self, nth) -> float:
        return float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') for i in self.item_container_product_price.nth(nth).text_content().split('\n')][0:3]))

    def item_prices(self) -> list:
        return [(float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') for i in self.item_container_product_price.nth(x).text_content().split('\n')][0:3]))) for x in range(len(self.item_container_product_price.all_text_contents()))]

    def item_name(self, nth) -> str:
        return self.item_container_product_name.nth(nth).text_content().lower()

    def item_names(self) -> list:
        #return self.item_container_product_name.nth(nth_index).text_content().lower().split(' ')
        return [x.lower() for x in self.item_container_product_name.all_text_contents()]

    def item_rate(self, nth) -> float:
        if self.item_container_product_rate.nth(nth).is_visible():
            return float(self.item_container_product_rate.nth(nth).text_content().replace(',', '.'))
        else:
            return 0.0

    def items_rates(self) -> list:
        items_rates_list = []
        for i in range(len(self.item_names())):
            items_rates_list.append(self.item_rate(nth=i))
        return items_rates_list

    def item_opinion(self, nth) -> int:
        if self.item_container_product_opinion.nth(nth).is_visible():
            return int(self.item_container_product_opinion.nth(nth).text_content().split(' ')[:1][0])
        else:
            return 0
 
    def items_opinions(self) -> list:
        items_opinion_list = []
        for i in range(len(self.item_names())):
            items_opinion_list.append(self.item_opinion(nth = i))
        return items_opinion_list

    def dropdown_text_content(self):
        Logger.info(self.dropdown_text.text_content().replace('\n', '').strip().split(' ')[:1][0])
        return self.dropdown_text.text_content().replace('\n', '').strip().split(' ')[:1][0]

    def page_items_data(self) -> dict:
        page_data = []
        for x in range(len(self.item_names())):
            d = {
                    "Nazwa" : self.item_name(nth = x),
                    "Cena" : self.item_price(nth = x),
                    "Ocena" : self.item_rate(nth = x),
                    "Ilość" : self.item_opinion(nth = x)
                }
            page_data.append(d)
        return page_data

    def all_items_data(self) -> dict:
        data = []
        number_of_pages = int(self.page_number.nth(3).text_content())
        for i in range(0,number_of_pages):
            self.page.wait_for_load_state()
            data.extend(self.page_items_data())
            if i < number_of_pages -1:
                self.next_page_btn.nth(1).click()
                #self.page.wait_for_load_state()
            else:
                continue
        self.page_number.nth(0).click()
        self.page.wait_for_load_state
        Logger.info("Data lenght {}".format(len(data)))
        #Logger.info(data)
        return data

    def sortby_scope(self) -> list:
        return self.sortby_options_container_exact_options.all_text_contents()

    def page_url(self) -> str:
        #Logger.info("Page url: {}".format(self.page.url))
        return self.page.url

    def sortby_param_option_click(self, nth_index, pageURL, test_data):
        self.expand_sortby_container_button_click()
        self.sortby_options_container_exact_options.nth(nth_index).click()
        self.page.wait_for_url(pageURL + test_data["sortbyEndpoints"][nth_index])

    def expected_sort(self, param, data, ascending = False):
        sort_list = [i[param] for i in sorted(data, key = itemgetter(param), reverse=ascending)[:30]]
        Logger.info("EXPECTED SORT DATA: {}".format(sort_list))
        return sort_list

    def actual_sort(self, param, data):
        sort_list = [i[param] for i in data[:30]]
        Logger.info("ACTUAL SORT DATA: {}".format(sort_list))
        return sort_list

    def sorting(self, test_data):
        expected_data = self.all_items_data()
        pageUrl = self.page_url()
        error = []
        for n in range(1, len(self.sortby_options_container_exact_options.all_inner_texts())):
            self.sortby_param_option_click(nth_index=n, pageURL=pageUrl, test_data=test_data)
            dropdown_text = self.dropdown_text_content()
            Logger.info("Dropdown text: {}".format(dropdown_text))
            Logger.info("{}".format(self.sortby_options_container_exact_options.nth(n).text_content()))
            actual_data = self.page_items_data()
            asc = False if n % 2 != 0 else True
            if self.expected_sort(param=dropdown_text, data=expected_data, ascending=asc) != self.actual_sort(param=dropdown_text, data = actual_data):
                error.append("{} : {}".format(dropdown_text, self.sortby_options_container_exact_options.nth(n).text_content()))
        return error
