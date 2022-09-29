import pytest
from settings.params import settings

@pytest.fixture
def test_data() -> dict:
    return {
        "phrase": settings.PHRASE,
        "popupNumberOfTiles": settings.POPUPNUMBEROFTILES,
        "minimumSuggestList": settings.MINIMUMSUGGESTLIST,
        "numberOfResultTiles": settings.NUMBEROFRESULTTILES,
        "emptyInputText": settings.EMPTYINPUTTEXT,
        "failPhrase": settings.FAILPHRASE
    }