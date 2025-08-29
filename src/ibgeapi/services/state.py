from ibgeapi._compat import override
from ibgeapi.models.state import State
from ibgeapi.services.location import LocationService

class StateService(LocationService):

    def __init__(self) -> None:
        super().__init__(State, "/estados")

    @override
    def parse(self, obj: dict) -> State:
        return State(
            ibge_id=obj["id"],
            name=obj["nome"],
            acronym=obj["sigla"]
        )
