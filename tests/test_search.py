import pytest
from playwright.sync_api import Page, expect
from pages.home import HomePage
from pages.result import ResultPage
from settings.params import settings
from settings.fixtures import test_data


@pytest.mark.parametrize("phrase", settings.PHRASE)
def test_basic_search(page: Page,
    phrase: str,
    test_data: dict, 
    home_page: HomePage,
    result_page: ResultPage) -> None:

    # Given the CentrumRowerowe home page is displayed
    home_page.load()

    # Typing the phrase
    home_page.type_phrase(phrase)

    # Checking the popup is visible
    assert home_page.popup_is_visible(), "Popup is not visible!"

    # Checking that the popup contains expected number of product tiles
    assert home_page.popup_contains_correct_number_of_tiles(test_data), f"Expected number of Tiles: {home_page.popup_contains_correct_number_of_tiles()} but expected: {settings.POPUPNUMBEROFTILES}"

    # Checking that the popup suggest contains phrase in first line
    assert home_page.popup_suggestion_list_contains_phrase(phrase, test_data), f"Expected phrase {phrase}, actual phrase {home_page.popup_suggestion_list.all_text_contents()[0]}"

    # Click search button
    home_page.search()

    # Checking the search phrase header is visible
    assert result_page.search_phrase_header_is_visible(phrase), f"Shearch phrase header is incorrect. Actual {result_page.search_phrase_header.text_content()}, Expected: 'Szukasz: {phrase}' "

    # Checking the number of tiles on result page
    assert result_page.number_of_tiles(test_data), f"Incorrect number of tiles on result page"

    # Clear search input
    result_page.clear_search_input()

    # Type the incorrect phrase
    result_page.type_phrase(test_data["failPhrase"])

    # Click search button
    result_page.search()

    # Checking the incorrect phrase message is displayed and contains correct text
    assert result_page.empty_input_alert_text, f"Incorrect alert text after write fail phrase to search input"

    # Clear search input
    result_page.clear_search_input()

    # Click search button
    result_page.search()

    # Checking the search input contains fail phrase
    assert result_page.search_input_contains_fail_phrase(), "Incorrect phrase in search input"

    # Click the remove search phrase button
    result_page.click_remove_search_phrase_button()

    # Check the all offers page is displayed
    assert result_page.all_offers_page_is_displayed(test_data)
