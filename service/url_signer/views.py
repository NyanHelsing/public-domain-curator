from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from boto.s3.connection import S3Connection

@api_view(['GET'])
def url_signer(request, format=None):
     c = S3Connection(access_key, secret_key)
    return Response(c.generate_url(
        expires_in=long(expiry),
        method='GET',
        bucket=bucket,
        key=path,
        query_auth=True,
        force_http=(not https)
    ))
