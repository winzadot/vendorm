import pytest
from allocation.adapters import repository
from allocation.domain import model

pytestmark = pytest.mark.usefixtures("mappers")


def test_get_by_batchref(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = repository.SqlAlchemyRepository(session)
    b1 = model.Batch(ref="b1", sku="sku1", qty=100, eta=None)
    b2 = model.Batch(ref="b2", sku="sku1", qty=100, eta=None)
    b3 = model.Batch(ref="b3", sku="sku2", qty=100, eta=None)
    p1 = model.Product(sku="sku1", batches=[b1, b2])
    p2 = model.Product(sku="sku2", batches=[b3])
    repo.add(p1)
    repo.add(p2)
    assert repo.get_by_batchref("b2") == p1
    assert repo.get_by_batchref("b3") == p2

def test_get_user(sqlite_session_factory):
    session = sqlite_session_factory()
    repo = repository.SqlAlchemyRepository(session)
    u1 = model.User(uername="username1", password="p@3455", usertype=1)
    u2 = model.User(uername="username2", password="p@3455", usertype=1)
    repo.add(u1)
    repo.add(u2)
    assert repo.get_by_User("username1") == u1
    assert repo.get_by_User("username2") == u2