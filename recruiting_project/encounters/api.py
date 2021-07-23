from rest_framework.viewsets import ModelViewSet

from recruiting_project.encounters.models import Starship, Encounter
from recruiting_project.encounters.serializers import StarshipSerializer, EncounterSerializer


class StarshipsModelViewSet(ModelViewSet):
    """
    Model viewset for starships API
    """
    serializer_class = StarshipSerializer

    def get_queryset(self):
        type_ac = self.request.query_params.dict()
        queryset = Starship.objects.filter(**type_ac)
        return queryset


class EncountersModelViewSet(ModelViewSet):
    """
    Model viewset for encounters API
    """
    queryset = Encounter.objects.all()
    serializer_class = EncounterSerializer
