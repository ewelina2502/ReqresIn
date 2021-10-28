import requests

from models.url import get_list_users, get_single, create_user


def get_list():
    response_get_list = requests.get(f'{get_list_users}')
    assert response_get_list.status_code == 200
    users_list = response_get_list.json()
    print(users_list)


def get_single_user():
    response_get_single = requests.get(f'{get_single}' + '/2')
    assert response_get_single.status_code == 200
    # single = response_get_single.json()['data']
    # print(single)
    email_adress = response_get_single.json()['data']['email']
    lastname = response_get_single.json()['data']['last_name']
    print(
        '{', '"email": ', '"', email_adress, '"', ',',
        '"last_name: "', '"', lastname, '"', '}'
    )


class Newuser:

    def __init__(self):
        self.name = 'My_user'
        self.job = 'Leader'

    def create_user(self):
        body = {
                "name": self.name,
                "job": self.job
            }

        response_new_user = requests.post(f'{create_user}', json=body)
        assert response_new_user.status_code == 201
        data_user = response_new_user.json()['id']
        print(data_user)
        return response_new_user.json()['id']
