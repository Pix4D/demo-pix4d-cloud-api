import requests
import boto3

CLOUD_URL = 'https://cloud.pix4d.com'
PROJECT_URL = f"{CLOUD_URL}/project/api/v3/projects"


def get_jwt(client_id, client_secret):
    query_params_dict = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "token_format": "jwt"
    }
    query_params = "&".join([f"{k}={v}" for k, v in query_params_dict.items()])
    url = f"{CLOUD_URL}/oauth2/token/?{query_params}"
    resp = requests.post(url)
    resp.raise_for_status()
    return resp.json()['access_token']


def headers(token):
    return {"Authorization": f"Bearer {token}"}


def create_project(name, token):
    url = f"{PROJECT_URL}/"
    resp = requests.post(url, json={'name': name}, headers=headers(token))
    resp.raise_for_status()
    return resp.json()


def project_s3_creds(project_id, token):
    url = f"{PROJECT_URL}/{project_id}/s3_credentials/"
    resp = requests.get(url, headers=headers(token))
    resp.raise_for_status()
    return resp.json()


def register_images(project_id, token, image_keys):
    url = f"{PROJECT_URL}/{project_id}/inputs/bulk_register/"
    resp = requests.post(url, headers=headers(token), json={
        "input_file_keys": image_keys
    })
    resp.raise_for_status()
    return resp.json()


def start_processing(project_id, token):
    url = f"{PROJECT_URL}/{project_id}/start_processing/"
    resp = requests.post(url, headers=headers(token))
    resp.raise_for_status()
    return resp.json()


def get_outputs(project_id, token):
    url = f"{PROJECT_URL}/{project_id}/outputs/"
    resp = requests.get(url, headers=headers(token))
    resp.raise_for_status()
    return resp.json()


def get_s3_client(project_id, token):
    s3_creds = project_s3_creds(project_id, token)
    return boto3.client('s3',
                        aws_access_key_id=s3_creds['access_key'],
                        aws_secret_access_key=s3_creds['secret_key'],
                        aws_session_token=s3_creds['session_token'])


def get_project(project_id, token):
    url = f"{PROJECT_URL}/{project_id}/"
    resp = requests.get(url, headers=headers(token))
    resp.raise_for_status()
    return resp.json()
