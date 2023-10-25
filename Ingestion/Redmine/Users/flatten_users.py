from Functions import export_functions, import_functions


def flatten_users(users):
    MISSING_VALUE = -1
    MISSING_TEXT = "MISSING_TEXT"  # Puedes personalizar el valor predeterminado según tus necesidades
    MISSING_DATE = "MISSING_DATE"  # Puedes personalizar el valor predeterminado según tus necesidades

    # users = dict(values.items()).get('users')

    flattened_data = []
    for user in users:
        # Copia el user original para no modificarlo
        flattened_user = user.copy()

        # Verificar y transformar "login"
        if not ("login" in flattened_user and flattened_user["login"] is not None):
            flattened_user["login"] = MISSING_VALUE

        # Verificar y transformar "firstname"
        if not (
            "firstname" in flattened_user and flattened_user["firstname"] is not None
        ):
            flattened_user["firstname"] = MISSING_TEXT

        # Verificar y transformar "lastname"
        if not (
            "lastname" in flattened_user and flattened_user["lastname"] is not None
        ):
            flattened_user["lastname"] = MISSING_TEXT

        # Verificar y transformar "mail"
        if not ("mail" in flattened_user and flattened_user["mail"] is not None):
            flattened_user["mail"] = MISSING_TEXT

        # Verificar y transformar "created_on"
        if not (
            "created_on" in flattened_user and flattened_user["created_on"] is not None
        ):
            flattened_user["created_on"] = MISSING_DATE

        # Verificar y transformar "updated_on"
        if not (
            "updated_on" in flattened_user and flattened_user["updated_on"] is not None
        ):
            flattened_user["updated_on"] = MISSING_DATE

        # Verificar y transformar "last_login_on"
        if not (
            "last_login_on" in flattened_user
            and flattened_user["last_login_on"] is not None
        ):
            flattened_user["last_login_on"] = MISSING_DATE

        # Verificar y transformar "passwd_changed_on"
        if not (
            "passwd_changed_on" in flattened_user
            and flattened_user["passwd_changed_on"] is not None
        ):
            flattened_user["passwd_changed_on"] = MISSING_DATE

        # Verificar y transformar "twofa_scheme"
        if not (
            "twofa_scheme" in flattened_user
            and flattened_user["twofa_scheme"] is not None
        ):
            flattened_user["twofa_scheme"] = MISSING_VALUE
        flattened_data.append(flattened_user)

    return flattened_data


# raw_users = import_functions.from_json("raw_users.json")

raw_users = import_functions.from_json_s3(
    "bucketfor008182637297", "redmine/users/raw_data/raw_users.json"
)

flattened_users = flatten_users(raw_users)

# export_functions.to_json(flattened_users, "flattened_users.json")

export_functions.to_json_s3(
    flattened_users, "bucketfor008182637297", "redmine/users/raw_data/raw_users.json"
)
