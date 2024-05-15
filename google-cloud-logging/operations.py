"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""

import json
from requests import request
from connectors.core.connector import get_logger, ConnectorError
from .google_api_auth import *

CLOUD_LOGGING_API_VERSION = 'v2'

logger = get_logger('google-cloud-logging')


def api_request(method, endpoint, connector_info, config, params=None, data=None, headers={}):
    try:
        go = GoogleAuth(config)
        endpoint = go.host + "/" + endpoint
        token = go.validate_token(config, connector_info)
        headers['Authorization'] = token
        headers['Content-Type'] = 'application/json'
        response = request(method, endpoint, headers=headers, params=params, data=data, verify=go.verify_ssl)
        try:
            from connectors.debug_utils.curl_script import make_curl
            make_curl(method, endpoint, headers=headers, params=params, data=data, verify_ssl=go.verify_ssl)
        except Exception as err:
            logger.error(f"Error in curl utils: {str(err)}")
        if response.ok or response.status_code == 204:
            if 'json' in str(response.headers):
                return response.json()
            else:
                return response
        else:
            logger.error("{0}".format(response.status_code))
            raise ConnectorError("{0}:{1}".format(response.status_code, response.text))
    except requests.exceptions.SSLError:
        raise ConnectorError('SSL certificate validation failed')
    except requests.exceptions.ConnectTimeout:
        raise ConnectorError('The request timed out while trying to connect to the server')
    except requests.exceptions.ReadTimeout:
        raise ConnectorError(
            'The server did not send any data in the allotted amount of time')
    except requests.exceptions.ConnectionError:
        raise ConnectorError('Invalid Credentials')
    except Exception as err:
        raise ConnectorError(str(err))


def check_payload(payload):
    result = {}
    for k, v in payload.items():
        if isinstance(v, dict):
            x = check_payload(v)
            if len(x.keys()) > 0:
                result[k] = x
        elif isinstance(v, list):
            p = []
            for c in v:
                if isinstance(c, dict):
                    x = check_payload(c)
                    if len(x.keys()) > 0:
                        p.append(x)
                elif c is not None and c != '':
                    p.append(c)
            if p != []:
                result[k] = p
        elif v is not None and v != '':
            result[k] = v
    return result


def get_log_entries_list(config, params, connector_info):
    try:
        ORDER_BY = {
            'Timestamp Ascending': 'timestamp asc',
            'Timestamp Descending': 'timestamp desc'
        }
        url = '{0}/entries:list'.format(CLOUD_LOGGING_API_VERSION)
        payload = {
            "resourceNames": params.get('resourceNames').split(","),
            "orderBy": ORDER_BY.get(params.get('orderBy')) if params.get('orderBy') else '',
            "filter": params.get('filter'),
            "pageSize": params.get('pageSize'),
            "pageToken": params.get('pageToken')
        }
        response = api_request('POST', url, connector_info, config, data=json.dumps(payload))
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


def _check_health(config, connector_info):
    try:
        return check(config, connector_info)
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))


operations = {
    'get_log_entries_list': get_log_entries_list
}
