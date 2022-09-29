from pydantic import BaseSettings

class Base(BaseSettings):
    TEST_URL: str = "https://www.centrumrowerowe.pl/"
    PHRASE: list = ["kierownica"]
    POPUPNUMBEROFTILES: int = 6
    MINIMUMSUGGESTLIST: int = 1
    NUMBEROFRESULTTILES: int = 30
    EMPTYINPUTTEXT: str = "Nie znaleźliśmy produktów odpowiadających Twoim parametrom..."
    FAILPHRASE: str = "abcdefgh12345"


settings = Base()