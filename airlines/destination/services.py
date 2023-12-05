from destination.models import DestinationModel

class DestinationServices:
    @staticmethod
    def get_context():
        return {
            "destinations": DestinationModel.objects.all()
        }