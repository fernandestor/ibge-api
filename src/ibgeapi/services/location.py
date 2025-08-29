from collections import defaultdict
from typing import Generic, Type, final
from ibgeapi.models.location import Location
from ibgeapi.services.ibge import IGBEService
from typing import TypeVar

T = TypeVar('T', bound=Location)

class LocationService(IGBEService, Generic[T]):

    def __init__(self, model: Type[T], endpoint: str) -> None:
        super().__init__()
        self._model = model
        self._filters = defaultdict(str)
        self.endpoint = f"/localidades{endpoint}"

    def parse(self, obj: dict) -> T:
        return self._model(
            ibge_id=obj["id"],
            name=obj["nome"]
        )

    @final
    def get(self, loc_id:int) -> T:
        response = self.client.get(f"{self.endpoint}/{loc_id}",
                                   params=self._filters)
        data = response.json()
        if isinstance(data, list):
            data = data[0] if data else None

        return self.parse(data) \
            if data else None

    @final
    def get_all(self, order_by:str="nome") -> list[T]:
        self._filters["orderBy"] = order_by
        response = self.client.get(self.endpoint,
                                   params=self._filters)
        data = response.json()
        return [self.parse(location) for location in data] \
            if data else []
