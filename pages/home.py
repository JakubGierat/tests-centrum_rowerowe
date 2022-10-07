import logging
from playwright.sync_api import Page
from settings.params import settings
import time

logging.basicConfig(level=logging.DEBUG)
Logger = logging.getLogger(__name__)

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator(".search-bar > input")
        self.search_button = page.locator("span[class='button orange jqSearch']")
        self.popup_container = page.locator(".suggestion > .container-inner")
        self.popup_tiles = page.locator("ul.right > li > a > p > .name")
        self.popup_suggestion_list = page.locator(".suggestion > .container-inner > .left > .texts > li > .name > em")
        self.cookies_accept = page.locator(".buttons > span[class='accept button orange']")
        self.main_menu_item_name = page.locator("a[class='menu-item-name']")
        self.main_menu_wrapper_column_1 = page.locator("div[class='main-menu-wrapper menu-column-1'] >> visible=true")
        self.main_menu_wrapper_column_2 = page.locator("div[class='main-menu-wrapper menu-column-2'] >> visible=true")
        self.main_menu_wrapper_column_3 = page.locator("div[class='main-menu-wrapper menu-column-3'] >> visible=true")
        self.main_menu_wrapper = page.locator("//ul")
        self.recommended_product_container = page.locator("div[class='container-inner Recommended']")
        self.recommended_product_item = page.locator("a.gtm-detail-link")
        self.recommended_product_name = page.locator("div.item-container > div.bottom > div.name")
        self.recommended_product_price = page.locator("span.final-price")


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

    def check_main_menu_bar_category_names(self, test_data):
        category_names = self.main_menu_item_name.all_inner_texts()
        expected_category_names = test_data['mainMenuCategories']
        errors = []
        for category in category_names:
            if category.lower() != expected_category_names[category_names.index(category)].lower():
                errors.append(category)
        return len(errors) < 1, "Following main menu bar's categories are incorrect: {}".format(errors)



    def main_menu_bar_wrapper_is_visible(self):
        selectors = {
            'Rowery  ' : self.main_menu_wrapper_column_3,
            'Akcesoria ' : self.main_menu_wrapper_column_3,
            'Trenażery ' : self.main_menu_wrapper_column_1,
            'Części ' : self.main_menu_wrapper_column_3,
            'Warsztat ': self.main_menu_wrapper_column_2,
            'Odzież i kaski ': self.main_menu_wrapper_column_3,
            'Outdoor ' : self.main_menu_wrapper_column_3
        }
        error = 0
        for i in range(len(self.main_menu_item_name.all_inner_texts())-2):
            self.main_menu_item_name.nth(i).hover()
            #time.sleep(0.15)
            selectors[self.main_menu_item_name.nth(i).text_content()].wait_for()

            Logger.info("{} selector to be visible: {}".format(self.main_menu_item_name.nth(i).text_content(), selectors[self.main_menu_item_name.nth(i).text_content()].is_visible()))

            if selectors[self.main_menu_item_name.nth(i).text_content()].is_visible():
                pass
            else:
                error += 1
        Logger.info("Errors: {}".format(error))
        return error == 0

    def main_menu_bar_categories_btns_respond(self, test_data):
        error = []
        Logger.info("Menu bar categories name: {}".format(self.main_menu_item_name.all_inner_texts()))
        for i in range(len(self.main_menu_item_name.all_inner_texts())):
            self.main_menu_item_name.nth(i).click()
            #self.page.wait_for_url(expected_url)
            Logger.info("Actual URL: {} Expected URL: {}".format(self.page.url, test_data["Url"] + test_data["mainMenuEndpoints"][i]))
            if not self.page.url in "{}{}".format(test_data["Url"], test_data["mainMenuEndpoints"][i]):
                error.append(i)
        return len(error) < 1

    def recommended_product_container_is_displayed(self):
        return self.recommended_product_container.is_visible()

    '''    def recommended_product_item_endpoint(self):
        Logger.info(self.recommended_product_item.nth(0).inner_html())
        return self.recommended_product_item.nth(0).first.inner_html()'''

    def recommended_product_item_click(self):
        self.recommended_product_item.nth(0).click()

    def recommended_product_item_name(self) -> str:
        self.recommended_product_name.nth(0).wait_for()
        product_name = self.recommended_product_name.nth(0).inner_text().lower().strip(' ')
        return product_name

    def recommended_product_item_price(self) -> str:
        self.recommended_product_price.nth(0).wait_for()

        product_price = float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',', '.').strip(' ') for i in self.recommended_product_price.first.text_content().split('\n')][0:3]))

        Logger.info("Main page price: {}".format(product_price))

        return float(''.join([i.replace(' ', '').replace('\xa0zł', '').replace(',','.').strip(' ') for i in self.recommended_product_price.first.text_content().split('\n')][0:3]))
    


    

    

    
    

