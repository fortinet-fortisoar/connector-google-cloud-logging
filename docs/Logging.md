## About the connector
Cloud Logging is a fully managed service that allows you to store, search, analyze, monitor, and alert on logging data and events from Google Cloud.
<p>This document provides information about the Google Cloud Logging Connector, which facilitates automated interactions, with a Google Cloud Logging server using FortiSOAR&trade; playbooks. Add the Google Cloud Logging Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Google Cloud Logging.</p>

### Version information

Connector Version: 1.0.0

FortiSOAR&trade; Version Tested on: 7.5.0-4015

Google Cloud Logging API Version Tested on: v2

Authored By: Fortinet

Certified: Yes

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-google-cloud-logging</pre>

## Prerequisites to configuring the connector
- You must have the credentials of Google Cloud Logging server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Google Cloud Logging server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Google Cloud Logging</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>The service-based URI to which you will connect and perform the automated operations.
</td>
</tr><tr><td>Client ID</td><td>Unique Client ID of the Google Cloud Logging that is used to create an authentication token required to access the Google Cloud Logging API.
</td>
</tr><tr><td>Client Secret</td><td>Unique Client Secret of the Google Cloud Logging that is used to create an authentication token required to access the API. For information on how to get the client secret, see https://developers.google.com/identity/protocols/oauth2/web-server.
</td>
</tr><tr><td>Authorization Code</td><td>The authorization code that you acquired during the authorization step. For more information, see the Accessing the Google Cloud Logging API section.
</td>
</tr><tr><td>Redirect URL</td><td>The redirect_uri of your app, where authentication responses can be sent and received by your app. It must exactly match one of the redirect_uri's you registered in the app registration portal.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Log Entries List</td><td>Retrieve log entries that originated from a project/folder/organization/billing account from Google Cloud.</td><td>get_log_entries_list <br/>Investigation</td></tr>
<tr><td>Get Exclusions List</td><td>Retrieve exclusions that originated from a project/folder/organization/billing account from Google Cloud.</td><td>get_exclusions_list <br/>Investigation</td></tr>
<tr><td>Get Sinks List</td><td>Retrieve sinks that originated from a project/folder/organization/billing account from Google Cloud.</td><td>get_sinks_list <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Log Entries List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Resource Names</td><td>Specify the list of comma-separated resource names based on which you want to retrieve log entries from Google Cloud Logging.
</td></tr><tr><td>Filter</td><td>(Optional) Specify the filter using values of certain attributes, for example, protoPayload.requestMetadata.callerIp = <ip_address>, based on which you want to filter the log entries retrieved from Google Cloud Logging.
</td></tr><tr><td>Order By</td><td>(Optional) Sorting order of the results, choose between Timestamp Ascending or Timestamp Descending. By default it set as Timestamp Ascending.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the maximum count of records that you want this operation to fetch from Google Cloud Logging. By default the value is 50 entries.
</td></tr><tr><td>Page Token</td><td>(Optional) Specify a Page Token if a previous operation returned a partial result. If the previous response contains a nextPageToken element, the value of the nextPageToken element includes a Page Token parameter that specifies a starting point to use for subsequent calls.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "entries": [
        {
            "protoPayload": {
                "@type": "",
                "status": {},
                "authenticationInfo": {
                    "principalEmail": ""
                },
                "requestMetadata": {
                    "callerIp": "",
                    "callerSuppliedUserAgent": "",
                    "requestAttributes": {},
                    "destinationAttributes": {}
                },
                "serviceName": "",
                "methodName": "",
                "authorizationInfo": [
                    {
                        "resource": "",
                        "permission": "",
                        "granted": "",
                        "resourceAttributes": {},
                        "permissionType": ""
                    }
                ],
                "resourceName": ""
            },
            "insertId": "",
            "resource": {
                "type": "",
                "labels": {
                    "project_id": "",
                    "method": "",
                    "service": ""
                }
            },
            "timestamp": "",
            "severity": "",
            "logName": "",
            "receiveTimestamp": ""
        }
    ],
    "nextPageToken": ""
}</pre>

### operation: Get Exclusions List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Parent Resource Name</td><td>Specify the resource name based on which you want to retrieve exclusions from Google Cloud Logging.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the maximum count of records that you want this operation to fetch from Google Cloud Logging.
</td></tr><tr><td>Page Token</td><td>(Optional) Specify a Page Token if a previous operation returned a partial result. If the previous response contains a nextPageToken element, the value of the nextPageToken element includes a Page Token parameter that specifies a starting point to use for subsequent calls.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "exclusions": [
        {
            "name": "",
            "createTime": "",
            "updateTime": ""
        }
    ],
    "nextPageToken": ""
}</pre>

### operation: Get Sinks List
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Parent Resource Name</td><td>Specify the parent resource name based on which you want to retrieve sinks from Google Cloud Logging.
</td></tr><tr><td>Filter</td><td>(Optional) Specify the filter using values of certain attributes, for example, in_scope("ALL"), based on which you want to filter the sinks retrieved from Google Cloud Logging.
</td></tr><tr><td>Page Size</td><td>(Optional) Specify the maximum count of records that you want this operation to fetch from Google Cloud Logging.
</td></tr><tr><td>Page Token</td><td>(Optional) Specify a Page Token if a previous operation returned a partial result. If the previous response contains a nextPageToken element, the value of the nextPageToken element includes a Page Token parameter that specifies a starting point to use for subsequent calls.
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "sinks": [
        {
            "name": "",
            "destination": "",
            "resourceName": ""
        }
    ],
    "nextPageToken": ""
}</pre>
## Included playbooks
The `Sample - Google Cloud Logging - 1.0.0` playbook collection comes bundled with the Google Cloud Logging connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Google Cloud Logging connector.

- Get Exclusions List
- Get Log Entries List
- Get Sinks List

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
