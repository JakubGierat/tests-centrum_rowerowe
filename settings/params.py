from pydantic import BaseSettings

class Base(BaseSettings):
    TEST_URL: str = "https://www.centrumrowerowe.pl"
    PHRASE: list = ["kierownica"]
    POPUPNUMBEROFTILES: int = 6
    MINIMUMSUGGESTLIST: int = 1
    NUMBEROFRESULTTILES: int = 30
    EMPTYINPUTTEXT: str = "Nie znaleźliśmy produktów odpowiadających Twoim parametrom..."
    FAILPHRASE: str = "abcdefgh12345"
    OFFERSURL: str = "https://www.centrumrowerowe.pl/oferta/"
    CARTURL: str = "https://www.centrumrowerowe.pl/koszyk/"
    MAINMENUCATEGORIES: list = ['Rowery', 'Akcesoria', 'Trenażery', 'Części', 'Warsztat', 'Odzież i kaski', 'Outdoor', 'Nowości', 'Wyprzedaż']
    MAINMENUENDPOINTS: list = ["rowery/", "akcesoria/", "akcesoria/trenazery-rowerowe/", "czesci/", "warsztat-rowerowy/", "odziez-rowerowa/", "outdoor/", "okazje/nowosci/", "okazje/wyprzedaz/"]
    ADDTOCARTALERTHEADER: str = "produkt został dodany do koszyka"
    SHIPPINGCOST: str = 'gratis'
    EMPTYCARTALERT: str = 'Twój koszyk jest pusty.'


settings = Base()