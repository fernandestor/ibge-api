from ibgeapi._compat import override
from ibgeapi.models.region import Region
from ibgeapi.services.location import LocationService

class RegionService(LocationService[Region]):

    def __init__(self) -> None:
        super().__init__(Region, "/regioes")

    @override
    def parse(self, obj: dict) -> Region:
        return Region(
            ibge_id=obj["id"],
            name=obj["nome"],
            acronym=obj["sigla"]
        )
