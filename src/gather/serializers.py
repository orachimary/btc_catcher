from rest_framework import serializers
from gather.models import BTC


class BTCSerializer(serializers.ModelSerializer):

    class Meta:
        model = BTC
        fields = ('usd_price', 'percent_change_1h', 'percent_change_24h', 'last_update')
