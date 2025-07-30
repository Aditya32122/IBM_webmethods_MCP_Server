from mcp.server.fastmcp import FastMCP
import requests
import base64
from typing import Optional

BASE_URL: Optional[str] = None
auth_header: Optional[dict] = None

mcp = FastMCP("IBM WebMethods MCP Server")

@mcp.tool()
def set_credentials(base_url: str, username: str, password: str) -> dict:
    """
    Set the base URL and Basic Auth credentials for WebMethods API Gateway.

    Args:
        base_url (str): The base URL (e.g., https://example.com/rest/apigateway).
        username (str): The username.
        password (str): The password.

    Returns:
        dict: Confirmation message.
    """
    global BASE_URL, auth_header
    BASE_URL = base_url.rstrip("/")
    token = base64.b64encode(f"{username}:{password}".encode()).decode()
    auth_header = {
        "Authorization": f"Basic {token}",
        "Accept": "application/json"
    }
    return {"message": "Credentials set successfully", "base_url": BASE_URL}

def get_headers() -> dict:
    """
    Internal helper to ensure credentials are set.
    """
    if not BASE_URL or not auth_header:
        raise Exception("You must call set_credentials(base_url, username, password) first.")
    return auth_header

@mcp.tool()
def get_all_apis() -> list:
    """
    Retrieve all APIs from the IBM WebMethods API Gateway.

    Returns:
        list: A list of APIs or an error message.
    """
    headers = get_headers()
    url = f"{BASE_URL}/apis"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }
    
@mcp.tool()
def get_all_users() -> list:
    """
    Retrieve all users from the IBM WebMethods API Gateway.

    Returns:
        list: A list of users or an error message.
    """
    headers = get_headers()
    url = f"{BASE_URL}/users"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()
        except Exception:
            return {"error": "Failed to parse JSON response", "raw_response": response.text}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def create_user(first_name: str, last_name: str, login_id: str, email: str, password: str, allow_digest_auth: bool = False) -> dict:
    """
    Create a new user in the IBM WebMethods API Gateway.

    Args:
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        login_id (str): The login ID/username for the user.
        email (str): The email address of the user.
        password (str): The password for the user.
        allow_digest_auth (bool): Whether to allow digest authentication (default: False).

    Returns:
        dict: Response from the API or error message.
    """
    headers = get_headers()
    headers["Content-Type"] = "application/json"

    url = f"{BASE_URL}/users"
    payload = {
        "firstName": first_name,
        "lastName": last_name,
        "loginId": login_id,
        "emailAddresses": [email],
        "password": password,
        "allowDigestAuth": allow_digest_auth
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        try:
            return response.json()
        except Exception:
            return {"message": "User created successfully but response is not JSON.", "raw_response": response.text}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }
    
@mcp.tool()
def get_all_applications() -> list:
    """
    Retrieve all applications from the IBM WebMethods API Gateway.

    Returns:
        list: A list of applications or an error message.
    """
    headers = get_headers()
    headers["Accept"] = "application/json"

    url = f"{BASE_URL}/applications"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()
        except Exception:
            return {"error": "Failed to parse JSON response", "raw_response": response.text}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def get_api_transactions(duration: str, start_date: str, end_date: str, event_type: str = "ALL") -> dict:
    """
    Retrieve API transactions from the IBM WebMethods API Gateway.

    Args:
        duration (str): Duration filter (e.g., '3d' for 3 days).
        start_date (str): Start date in 'YYYY-MM-DD HH:MM:SS' format.
        end_date (str): End date in 'YYYY-MM-DD HH:MM:SS' format.
        event_type (str): Event type (e.g., 'ALL', 'ERROR'). Defaults to 'ALL'.

    Returns:
        dict: The transactions or an error message.
    """
    headers = get_headers()
    headers["Accept"] = "application/json"

    # URL encode the query parameters
    from urllib.parse import quote
    start_date_encoded = quote(start_date, safe='')
    end_date_encoded = quote(end_date, safe='')

    url = (f"{BASE_URL}/apitransactions"
           f"?duration={duration}"
           f"&startDate={start_date_encoded}"
           f"&endDate={end_date_encoded}"
           f"&eventType={event_type}")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()
        except Exception:
            return {"error": "Failed to parse JSON response", "raw_response": response.text}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def create_application(
    name: str,
    description: str,
    version: str,
    identifiers: list,
    consuming_apis: list = None,
    is_suspended: bool = False,
    new_apis_for_association: list = None,
    auth_strategy_ids: list = None,
    teams: list = None,
    contact_emails: list = None,
    site_urls: list = None,
    js_origins: list = None,
    restrict_view_asset: bool = False
) -> dict:
    """
    Create a new application in the IBM WebMethods API Gateway.

    Args:
        name (str): Name of the application.
        description (str): Description of the application.
        version (str): Version number.
        identifiers (list): List of identifier objects (name, key, value[]).
        consuming_apis (list): List of APIs consumed by this application.
        is_suspended (bool): Whether the app is suspended.
        new_apis_for_association (list): List of API IDs for association.
        auth_strategy_ids (list): List of authentication strategy IDs.
        teams (list): List of teams with their IDs.
        contact_emails (list): List of contact emails.
        site_urls (list): List of site URLs.
        js_origins (list): List of JavaScript origins.
        restrict_view_asset (bool): Whether to restrict asset view.

    Returns:
        dict: Response from the API or an error message.
    """
    headers = get_headers()
    headers["Content-Type"] = "application/json"

    url = f"{BASE_URL}/applications"
    payload = {
        "name": name,
        "description": description,
        "version": version,
        "contactEmails": contact_emails or [],
        "siteURLs": site_urls or [],
        "identifiers": identifiers,
        "consumingAPIs": consuming_apis or [],
        "isSuspended": is_suspended,
        "newApisForAssociation": new_apis_for_association or [],
        "jsOrigins": js_origins or [],
        "authStrategyIds": auth_strategy_ids or [],
        "restrictViewAsset": restrict_view_asset,
        "teams": teams or []
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        try:
            return response.json()
        except Exception:
            return {"message": "Application created successfully, but response is not JSON.", "raw_response": response.text}
    else:
        return {"error": f"Error: {response.status_code}", "details": response.text}

@mcp.tool()
def associate_apis_with_application(application_id: str, api_ids: list) -> dict:
    """
    Associate or register one or more APIs with an existing application in IBM WebMethods API Gateway.

    Args:
        application_id (str): The ID of the application to which APIs will be associated.
        api_ids (list): A list of API IDs to associate with the application.

    Returns:
        dict: The API response or an error message.
    """
    headers = get_headers()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json"

    url = f"{BASE_URL}/applications/{application_id}/apis"
    payload = {"apiIDs": api_ids}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        try:
            return response.json()
        except Exception:
            return {
                "message": "APIs successfully associated with the application, but response is not JSON.",
                "raw_response": response.text
            }
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def delete_application(application_id: str) -> dict:
    """
    Delete an application from the IBM WebMethods API Gateway.

    Args:
        application_id (str): The ID of the application to be deleted.

    Returns:
        dict: Confirmation message or error response.
    """
    headers = get_headers()
    url = f"{BASE_URL}/applications/{application_id}"

    response = requests.delete(url, headers=headers)

    if response.status_code in [200, 204]:
        return {"message": f"Application {application_id} deleted successfully."}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def get_api_details(api_id: str) -> dict:
    """
    Retrieve details of a specific API from the IBM WebMethods API Gateway with the help of API ID.

    Args:
        api_id (str): The unique ID of the API.

    Returns:
        dict: API details or an error message.
    """
    headers = get_headers()
    headers["Accept"] = "application/json"

    url = f"{BASE_URL}/apis/{api_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            return response.json()
        except Exception:
            return {"error": "Failed to parse JSON response", "raw_response": response.text}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }
    
@mcp.tool()
def delete_api(api_id: str, force_delete: bool = True) -> dict:
    """
    Delete a specific API from the IBM WebMethods API Gateway.

    Args:
        api_id (str): The unique ID of the API.
        force_delete (bool): Whether to force delete the API. Defaults to True.

    Returns:
        dict: Confirmation message or error response.
    """
    headers = get_headers()
    headers["Accept"] = "application/json"

    url = f"{BASE_URL}/apis/{api_id}"
    if force_delete:
        url += "?forceDelete=true"

    response = requests.delete(url, headers=headers)

    if response.status_code in [200, 204]:
        return {"message": f"API {api_id} deleted successfully."}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def activate_api(api_id: str) -> dict:
    """
    Activate a specific API in the IBM WebMethods API Gateway.

    Args:
        api_id (str): The unique ID of the API to be activated.

    Returns:
        dict: Response message or error details.
    """
    headers = get_headers()
    headers["Accept"] = "application/json"

    url = f"{BASE_URL}/apis/{api_id}/activate"
    response = requests.put(url, headers=headers)

    if response.status_code in [200, 204]:
        try:
            return response.json() if response.text else {"message": f"API {api_id} activated successfully."}
        except Exception:
            return {"message": f"API {api_id} activated successfully (non-JSON response)."}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def deactivate_api(api_id: str) -> dict:
    """
    Deactivate a specific API in the IBM WebMethods API Gateway.

    Args:
        api_id (str): The unique ID of the API to be deactivated.

    Returns:
        dict: Response message or error details.
    """
    headers = get_headers()
    headers["Accept"] = "application/json"

    url = f"{BASE_URL}/apis/{api_id}/deactivate"
    response = requests.put(url, headers=headers)

    if response.status_code in [200, 204]:
        try:
            return response.json() if response.text else {"message": f"API {api_id} deactivated successfully."}
        except Exception:
            return {"message": f"API {api_id} deactivated successfully (non-JSON response)."}
    else:
        return {
            "error": f"Error: {response.status_code}",
            "details": response.text
        }

@mcp.tool()
def create_api_from_swagger(file_path: str, api_name: str, api_description: str, api_version: str = "1.0", api_type: str = "swagger") -> dict:
    """
    Create a new API in API Gateway using a Swagger file.

    Args:
        file_path (str): Absolute path to the Swagger/OpenAPI JSON file.
        api_name (str): Name of the API.
        api_description (str): Description of the API.
        api_version (str, optional): Version of the API. Defaults to "1.0".
        api_type (str, optional): Type of import. Defaults to "swagger".

    Returns:
        dict: Response from API Gateway, including API ID or error message.
    """
    headers = get_headers(content_type=None)  # Let `requests` set it for multipart
    headers["Accept"] = "application/json"

    try:
        with open(file_path, 'rb') as f:
            files = {
                'file': (file_path.split("/")[-1], f),
            }
            data = {
                'apiName': api_name,
                'type': api_type,
                'apiDescription': api_description,
                'apiVersion': api_version
            }

            url = f"{BASE_URL}/apis"
            response = requests.post(url, headers=headers, files=files, data=data)

            if response.status_code in [200, 201]:
                return response.json()
            else:
                return {
                    "error": f"Failed to create API. Status code: {response.status_code}",
                    "details": response.text
                }
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}



# Start server
# if __name__ == "__main__":
#     import uvicorn
#     print("Starting IBM WebMethods MCP Server on http://localhost:8000")
#     uvicorn.run("server:mcp", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')