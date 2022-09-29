import pytest
from playwright.sync_api import Page, expect
from pages.home import HomePage
from pages.result import ResultPage
from settings.params import settings
from settings.fixtures import test_data

PHRASE = settings.PHRASE


@pytest.mark.parametrize("phrase", PHRASE)
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
    assert result_page.empty_input_alert_text, f"Incorrect aletr text after write fail phrase to search input"

    # Clear search input
    result_page.clear_search_input()

    # Click search button
    result_page.search()

    # Checking the search input contains fail phrase
    assert result_page.search_input_contains_fail_phrase(), "Incorrect phrase in search input"

    # Click the remove search phrase button
    result_page.click_remove_search_phrase_button()

    # Check the search phrase header disappeared
    assert not result_page.search_phrase_header_is_visible(phrase)





'''
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Click html
    page.goto("https://www.centrumrowerowe.pl/")

    # Click [placeholder="Szukaj produktów"]
    page.locator("[placeholder=\"Szukaj produktów\"]").click()

    # Fill [placeholder="Szukaj produktów"]
    page.locator("[placeholder=\"Szukaj produktów\"]").fill("kierownica")

    # Click span:has-text("Szukaj") >> nth=0
    page.locator("span:has-text(\"Szukaj\")").first.click()
    page.wait_for_url("https://www.centrumrowerowe.pl/oferta/?q=kierownica&sort=11")

    # Click [placeholder="Szukaj produktów"]
    page.locator("[placeholder=\"Szukaj produktów\"]").click()

    # Fill [placeholder="Szukaj produktów"]
    page.locator("[placeholder=\"Szukaj produktów\"]").fill("abcdefgh12345")

    # Click .button > .icon
    page.locator(".button > .icon").click()
    page.wait_for_url("https://www.centrumrowerowe.pl/oferta/?q=abcdefgh12345&sort=11")

    # Click text=Nie znaleźliśmy produktów odpowiadających Twoim parametrom...
    page.locator("text=Nie znaleźliśmy produktów odpowiadających Twoim parametrom...").click()

    # Click [placeholder="Szukaj produktów"]
    page.locator("[placeholder=\"Szukaj produktów\"]").click()

    # Click text=Menu Zaloguj się Koszyk Szukaj
    page.locator("text=Menu Zaloguj się Koszyk Szukaj").click()

    # Fill [placeholder="Szukaj produktów"]
    page.locator("[placeholder=\"Szukaj produktów\"]").fill("")

    # Click text=Szukaj
    page.locator("text=Szukaj").click()

    # Click span:has-text("Szukaj") >> nth=0
    page.locator("span:has-text(\"Szukaj\")").first.click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
'''