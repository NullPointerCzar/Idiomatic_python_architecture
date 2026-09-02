import logging
from collections.abc import Iterator

import requests
from pydantic import BaseModel, ValidationError

from .exceptions import FetchDataError, SerializationError

# Obtain logger for this module—NO basicConfig call here!
logger = logging.getLogger(__name__)


class UserRecord(BaseModel):
    id: int
    name: str
    email: str


class UserBatchIterator:
    def __init__(
        self, users: list[UserRecord], batch_size: int = 2
    ) -> None:
        self._users = users
        self._batch_size = batch_size
        self._index = 0

    def __iter__(self) -> Iterator[list[UserRecord]]:
        return self

    def __next__(self) -> list[UserRecord]:
        if self._index >= len(self._users):
            raise StopIteration
        batch = self._users[
            self._index : self._index + self._batch_size
        ]
        self._index += self._batch_size
        return batch


class UserApiClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def fetch_users(self) -> list[UserRecord]:
        logger.info(f"Fetching users from {self.base_url}")
        return self._fetch_users()

    def _fetch_users(self) -> list[UserRecord]:
        try:
            resp = requests.get(self.base_url, timeout=5.0)
        except requests.RequestException as err:
            raise FetchDataError(self.base_url, 0) from err

        if resp.status_code != 200:
            raise FetchDataError(self.base_url, resp.status_code)

        try:
            return [
                UserRecord.model_validate(item)
                for item in resp.json()
            ]
        except ValidationError as err:
            raise SerializationError("Invalid user schema") from err