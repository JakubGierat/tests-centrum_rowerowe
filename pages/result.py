from playwright.sync_api import Page
from settings.params import settings

class ResultPage:

    def __init__(self, page:Page):
        self.page = page
        self.search_input = page.locator(".search-bar > input")
        self.search_button = page.locator("span[class='button orange jqSearch']")
        self.search_phrase_header = page.locator("div[class='searched-phrase hidden-xs']")
        self.result_number_of_tiles = page.locator(".item-container > .first-leyer")
        self.results_tiles_title = page.locator(".bottom > .name > a")
        self.empty_input_text = page.locator(".empty-list-text > h2")
        self.remove_search_phrase_btn = page.locator("form[action='ProductList/ProductList']:nth-child(2) > a")

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
        return len(self.result_number_of_tiles.all_inner_texts()) <= test_data["numberOfResultTiles"]

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
        self.remove_search_phrase_btn.click()

    # Check the search phrase header disappeared

    

