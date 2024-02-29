class CreateAccount:
    email = ""
    password = ""
    username = ""

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    def create_account(self):
        payload = {
            "email": self.email,
            "password": self.password,
            "username": self.username
        }

        response = make_request(payload, "account.account/CreateAccount")
