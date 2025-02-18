"""Test parse strategies."""


def test_json():
    """Test `text/json` parse strategy."""
    from oteapi.models.resourceconfig import ResourceConfig

    from oteapi_ontokb_plugin.strategies.parse import DemoJSONDataParseStrategy

    data = {
        "firstName": "Joe",
        "lastName": "Jackson",
        "gender": "male",
        "age": 28,
        "address": {"streetAddress": "101", "city": "San Diego", "state": "CA"},
        "phoneNumbers": [{"type": "home", "number": "7349282382"}],
    }

    config = ResourceConfig(
        downloadUrl="https://filesamples.com/samples/code/json/sample2.json",
        mediaType="text/jsonDEMO",
    )
    parser = DemoJSONDataParseStrategy(config)
    json = parser.get()

    assert json == data
