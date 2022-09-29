from playwright.sync_api import Page
from settings.params import settings

class HomePage:


    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator(".search-bar > input")
        self.search_button = page.locator("span[class='button orange jqSearch']")
        self.popup_container = page.locator(".suggestion > .container-inner")
        self.popup_tiles = page.locator("ul.right > li > a > p > .name")
        self.popup_suggestion_list = page.locator(".suggestion > .container-inner > .left > .texts > li > .name > em")
        self.cookies_accept = page.locator(".buttons > span[class='accept button orange']")

    def load(self):
        self.page.goto(settings.TEST_URL)
        self.cookies_accept.click()

    def type_phrase(self, phrase: str):
        self.search_input.type(phrase)

    def search(self):
        self.search_button.click()

    def popup_is_visible(self):
        self.popup_container.wait_for()
        return self.popup_container.is_visible()

    def popup_contains_correct_number_of_tiles(self, test_data):
        tiles = self.popup_tiles.all_inner_texts()
        tilesCounter = len(tiles)
        return tilesCounter == test_data["popupNumberOfTiles"]

    def popup_suggestion_list_contains_phrase(self, phrase: str, test_data):
        suggestion_list = self.popup_suggestion_list.all_text_contents()
        return phrase in suggestion_list[0] and len(suggestion_list) >= test_data["minimumSuggestList"]