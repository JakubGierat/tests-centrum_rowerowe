import pytest
from settings.params import settings

@pytest.fixture
def test_data() -> dict:
    return {
        "Url": settings.TEST_URL,
        "phrase": settings.PHRASE,
        "popupNumberOfTiles": settings.POPUPNUMBEROFTILES,
        "minimumSuggestList": settings.MINIMUMSUGGESTLIST,
        "numberOfResultTiles": settings.NUMBEROFRESULTTILES,
        "emptyInputText": settings.EMPTYINPUTTEXT,
        "failPhrase": settings.FAILPHRASE,
        "offersUrl": settings.OFFERSURL,
        "cartUrl": settings.CARTURL,
        'mainMenuCategories': settings.MAINMENUCATEGORIES,
        "mainMenuEndpoints" : settings.MAINMENUENDPOINTS,
        "addToCartAlertHeader" : settings.ADDTOCARTALERTHEADER,
        "shippingCost" : settings.SHIPPINGCOST,
        "emptyCartAlert" : settings.EMPTYCARTALERT,
        "sortbyParams" : settings.SORTBYPARAMS,
        "sortby" : settings.SORTBY,
        "sortbyEndpoints": settings.SORTBYENDPOINTS,
    }

