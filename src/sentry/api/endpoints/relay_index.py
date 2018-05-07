from __future__ import absolute_import

from rest_framework.permissions import IsAuthenticated

from sentry.api.base import Endpoint
from sentry.api.paginator import OffsetPaginator
from sentry.api.serializers import serialize
from sentry.models import Relay


class RelayIndexEndpoint(Endpoint):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        """
        List your Relays
        ````````````````

        Return a list of relays know to this Sentry installation available
        to the authenticated session.

        :auth: required
        """
        queryset = Relay.objects.all()

        return self.paginate(
            request=request,
            queryset=queryset,
            order_by='relay_id',
            paginator_cls=OffsetPaginator,
            on_results=lambda x: serialize(x, request.user),
        )
