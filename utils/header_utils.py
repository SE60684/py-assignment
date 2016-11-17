
import re
regex_http_ = re.compile(r'^HTTP_.+$')
regex_content_type = re.compile(r'^CONTENT_TYPE$')
regex_content_length = re.compile(r'^CONTENT_LENGTH$')


def get_header(request):
    request_headers = {}
    for header in request.META:
        if regex_http_.match(header) or regex_content_type.match(header) or regex_content_length.match(header):
            request_headers[header] = request.META[header]
    return request_headers