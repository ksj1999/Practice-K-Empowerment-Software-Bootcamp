def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6

    return cond1


# def is_acceptable_password(password: str) -> bool:
#
#     if len(password) <= 6:
#         print("short")
#         return
#     else:
#         print("valid")
#         return
#
# print(is_acceptable_password())

