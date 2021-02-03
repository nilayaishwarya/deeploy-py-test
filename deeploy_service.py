import base64
from typing import Optional, List, Any

import requests

from .models import Deployment, Repository

class DeeployService(object):
  """ 
  A class for interacting with the Deeploy API
  """

  def __init__(self, access_key: str, secret_key: str, host: str) -> None:
    self.__access_key = access_key
    self.__secret_key = secret_key
    self.__host = host

    if not self.__keys_are_valid():
      raise 'Access keys are not valid'
    return

  def __keys_are_valid(self) -> bool:
    # TODO verify keys with host
    return False

  def __get_bearer_header(self) -> str:
    keys_plain = '%s:%s' % (self.__access_key, self.__secret_key)
    keys_ascii_encoded = keys_plain.encode('ascii')
    keys_base64 = base64.b64encode(keys_ascii_encoded).decode('ascii')
    bearer_header = 'Bearer %s' % keys_base64
    return bearer_header

  def get_repositories(self, workspace_id: str) -> List[Repository]:
    return

  def create_deployment(self) -> Deployment:
    return