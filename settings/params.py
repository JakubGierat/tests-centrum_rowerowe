from pydantic import BaseSettings

class Base(BaseSettings):
    TEST_URL: str = "https://www.centrumrowerowe.pl"
    PHRASE: list = ["kierownica", "koło", "opona"]
    POPUPNUMBEROFTILES: int = 6
    MINIMUMSUGGESTLIST: int = 1
    NUMBEROFRESULTTILES: int = 30
    EMPTYINPUTTEXT: str = "Nie znaleźliśmy produktów odpowiadających Twoim parametrom..."
    FAILPHRASE: str = "abcdefgh12345"
    OFFERSURL: str = "https://www.centrumrowerowe.pl/oferta/"
    CARTURL: str = "https://www.centrumrowerowe.pl/koszyk/"
    MAINMENUCATEGORIES: list = ['Rowery', 'Akcesoria', 'Trenażery', 'Części', 'Warsztat', 'Odzież i kaski', 'Outdoor', 'Nowości', 'Wyprzedaż']
    MAINMENUENDPOINTS: list = ["/rowery/", "/akcesoria/", "/akcesoria/trenazery-rowerowe/", "/czesci/", "/warsztat-rowerowy/", "/odziez-rowerowa/", "/outdoor/", "/okazje/nowosci/", "/okazje/wyprzedaz/"]
    ADDTOCARTALERTHEADER: str = "produkt został dodany do koszyka"
    SHIPPINGCOST: str = 'gratis'
    EMPTYCARTALERT: str = 'Twój koszyk jest pusty.'
    SORTBYPARAMS: list = ['Popularność', 'Cena', 'Nazwa', 'Ocena', 'Ilość opinii']
    SORTBY: list = ['największa', 'od najniższej', 'od najwyższej', 'od A do Z', 'od Z do A', 'od najniższej', 'od najwyższej', 'rosnąco', 'malejąco']
    SORTBYENDPOINTS: list = ['?order=2', '?sort=2', '?sort=2&order=2', '?sort=3', '?sort=3&order=2', '?sort=4', '?sort=4&order=2', '?sort=5', '?sort=5&order=2']
    


settings = Base()