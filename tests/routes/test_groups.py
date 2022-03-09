from unittest import mock

from flask import url_for


def fake_session(query):
    class FakeQuery:
        def all(self):
            return [{"id": 1, "name": "First"}, {"id": 2, "name": "Second"}]
    return FakeQuery()


@mock.patch("backend.db.session.scalars", new=lambda query: fake_session(query))
def test_get_all_groups(flask_app):
    # when
    response = flask_app.get(url_for("groups.get_all_groups"))

    # then
    assert response.status_code == 200

    data = response.json
    assert len(data) == 2


def test_get_all_groups_validate(flask_app):
    with mock.patch("backend.db.session.scalars") as mocked_session:
        # given
        mocked_session.return_value = fake_session(None)

        # when
        response = flask_app.get(url_for("groups.get_all_groups"))

        data = response.json
        assert len(data) == 2
        mocked_session.assert_called_once()
