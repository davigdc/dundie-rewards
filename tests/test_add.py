import pytest

from dundie.database import connect, commit, add_person
from dundie.core import add


@pytest.mark.unit
def test_add_movement():
    db = connect()

    pk = "joe@doe.com"
    data = {
        "name": "Joe Doe",
        "role": "Salesman",
        "dept": "Sales",
    }
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    pk = "jim@doe.com"
    data = {
        "name": "Jim Doe",
        "role": "Manager",
        "dept": "Management",
    }
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    add(-30, email="joe@doe.com")
    add(90, dept="Management")

    db = connect()
    assert db["balance"]["joe@doe.com"] == 470
    assert db["balance"]["jim@doe.com"] == 190
