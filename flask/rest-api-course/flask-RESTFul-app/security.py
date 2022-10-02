from hmac import compare_digest
from user import User



# Define users
users = [
    User(1, 'bob', 'asdfg'),
    User(2, 'frank', 'qwert')
]

# Map users and user ids
username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}



def authenticate(username, password):
    user = username_mapping.get(username, None)
    # if user and user.password == password
    # we should avoid using ´==´ to compare strings, and use compare_digest
    # see more at https://docs.python.org/3/library/hmac.html
    if user and compare_digest(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
