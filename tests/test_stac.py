import pytest
from stac.models.base import STACObject
from stac.models.asset import Asset as MSAsset
from stac.models.link import Link as MSLink
from stac.models.properties import Properties as MSProperties
from stac.models.item import Item as MSItem
from .schema.stac import assert_valid_item_schema


@pytest.fixture
def stac():
    return {}


@pytest.fixture
def asset():
    return {
        "name": "sample-asset",
        "href": "/sample-asset.tif"
    }


@pytest.fixture
def link():
    return {
        "type": "self",
        "rel": "self",
        "href": "http://demo.org/",
        "hreflang": "en"
    }


@pytest.fixture
def properties():
    return {
        "ext_properties": {"prop1": "value1"},
        "license": "CC-0",
        "provider": "geonode",
        "datetime": "2009-04-01T00:00:00+00:00/2009-04-02T00:00:00+00:00"
    }


@pytest.fixture
def geometry():
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                [100.0, 1.0], [100.0, 0.0]
            ]
        ]
    }


@pytest.fixture
def Base(stac):
    return STACObject(stac)


@pytest.fixture
def Asset(asset):
    return MSAsset(asset["href"], asset["name"])


@pytest.fixture
def Link(link):
    return MSLink(link["type"], link["rel"], link["href"], link["hreflang"])


@pytest.fixture
def Properties(properties):
    return MSProperties(
        properties["datetime"],
        properties["provider"],
        properties["license"],
        properties["ext_properties"]
    )


@pytest.fixture
def Item(geometry, Properties, Link, Asset):
    return MSItem(
        "test_sample_id",
        geometry,
        Properties,
        [Link],
        Asset.dict
    )


@pytest.fixture
def Collection():
    return {}


def test_validate_schema_collection(Collection):
    assert True


def test_validate_schema_item(Item):
    assert assert_valid_item_schema(Item.dict)
