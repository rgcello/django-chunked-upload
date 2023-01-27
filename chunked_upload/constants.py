

class http_status:
    HTTP_200_OK = 200
    HTTP_400_BAD_REQUEST = 400
    HTTP_403_FORBIDDEN = 403
    HTTP_410_GONE = 410


UPLOADING = 1
COMPLETE = 2

CHUNKED_UPLOAD_CHOICES = (
    (UPLOADING, ('Uploading')),
    (COMPLETE, ('Complete')),
)
