from typing import NewType

UserId = NewType('UserId123', int)
some_id = UserId(524313)


def get_user_name(user_id: UserId) -> str:
    print(type(user_id), user_id)
    return "字符串"


# passes type checking
user_a = get_user_name(UserId(42351))

# fails type checking; an int is not a UserId
# user_b = get_user_name(-1)
