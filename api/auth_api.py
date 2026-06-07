from api import routes


def login_user(client, data):

    return client.post(routes.Routes.LOGIN, json=data)



def registration_user(client, data):

    return client.post(routes.Routes.REGISTRATION, json=data)

def not_valid_registration(client, data):

    return client.post(routes.Routes.REGISTRATION, json=data)

def get_secure_page(client):
    return client.get(routes.Routes.SECURE_PAGE)

def get_catalog(client):
    return client.get(routes.Routes.CATALOG)


