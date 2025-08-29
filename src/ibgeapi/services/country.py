from ibgeapi._compat import override
from ibgeapi.models.country import Country
from ibgeapi.services.location import LocationService

class CountryService(LocationService):

    def __init__(self) -> None:
        super().__init__(Country, "/paises")
        self._prefix = "pais-"
        self._filters["view"] = "nivelado"

    @override
    def parse(self, obj: dict) -> Country:
        return Country(
            ibge_id=obj[f"{self._prefix}M49"],
            iso_alpha2=obj[f"{self._prefix}ISO-ALPHA-2"],
            iso_alpha3=obj[f"{self._prefix}ISO-ALPHA-3"],
            name=obj[f"{self._prefix}nome"]
        )
