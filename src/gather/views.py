from rest_framework.decorators import api_view
from rest_framework.response import Response
from gather.models import BTC
from gather.serializers import BTCSerializer
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from btc_catcher.tasks import get_btc_info

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def get_btc_rows(request):
    if request.method == 'GET':
        btc_rows = BTC.objects.all().order_by('-last_update')[:10]
        serializer = BTCSerializer(btc_rows, many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def update_btc_info(request):
    if request.method == 'POST':
        get_btc_info.delay()
        return Response('Task scheduled')

