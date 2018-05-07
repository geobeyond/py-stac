from marshmallow import fields, Schema
from pystac.models.geojson_type import GeojsonType
from pystac.models.item import ItemSchema
from pystac.models.base import STACObject


class Collection(STACObject):
    def __init__(
        self, features
    ):
        """STAC Catalog item collection

        Args:
            features (List[Item]):
        """
        self.features = features

    @property
    def dict(self):
        return dict(
            type=GeojsonType.FeatureCollection,
            features=[feature.dict for feature in self.features]
        )

    @property
    def json(self):
        return CollectionSchema().dumps(
            self
        )


class CollectionSchema(Schema):

    features = fields.Nested(ItemSchema, many=True)
