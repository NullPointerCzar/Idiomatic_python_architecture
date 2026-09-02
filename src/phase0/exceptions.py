from email.mime import message


class ApplicationError(Exception):
    """Base class for all application errors."""
    pass

class FetchDataError(ApplicationError):
    """Raised when there is an error fetching data."""
    def __init__(self, url:str, status_code:int)-> None:
        self.url = url
        self.status_code = status_code
        super().__init__(f"Error fetching data from {url}: {status_code}")
        
class SerializationError(ApplicationError):
    pass