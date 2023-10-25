import requests as request

USER_KEY_REDMINE_COM = "047f85e0b24fe4d7651e576fedd11ad410336e2d"
ADMIN_KEY_REDMINE_NET = "8b6fda64b68909ba178c8f783703bed30396eaf5"


def iterative_get_rest_api(dicc_key, get_request):
    headers = {"X-Redmine-API-Key": ADMIN_KEY_REDMINE_NET}
    # Realizo una petición para saber el numero total de issues , aprovecho para cargar los primeros 100
    # creo la variable values y la tomo como base para almacenar el resto de issues

    i = 100
    url = get_request + "?offset=0&limit=100"
    response = request.get(url, headers=headers)
    resp = response.json()
    values = resp.copy()

    limit = values.get("total_count")

    # Recuperar todos los issues
    while i <= limit:
        url = get_request + "?offset=" + str(i) + "&limit=100"
        response = request.get(url, headers=headers)
        resp = response.json()
        values[dicc_key].extend(resp.get(dicc_key))
        i += 100
        print(i)

    values = dict(values.items()).get(dicc_key)

    return values
