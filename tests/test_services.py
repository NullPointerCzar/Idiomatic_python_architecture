from phase0.exceptions import FetchDataError
from phase0.services import UserBatchIterator, UserRecord
def test_user_batch_iterator() -> None:
    
    users = [
        UserRecord(id=1, name="Alice", email="alice@test.com"),
        UserRecord(id=2, name="Bob", email="bob@test.com"),
        UserRecord(id=3, name="Charlie", email="charlie@test.com"),
    ]
    iterator = UserBatchIterator(users, batch_size=2)
    batches = list(iterator)
    assert len(batches) == 2
    assert len(batches[0]) == 2
    assert batches[0][0].name == "Alice"
def test_fetch_data_error_formatting() -> None:


    err = FetchDataError("https://api.test", 404)
    assert "404" in str(err)
    assert err.status_code == 404
