from werkzeug.security import safe_str_cmp
from models.user import UserModel

# https://blog.tecladocode.com/simple-jwt-authentication-with-flask-jwt/

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        # Flask-JWT will take the id property of the user object and store that in the JWT.
        return user

# The identity function is used when we receive a JWT.
# Authorization: JWT <JWT_VALUE_HERE>
# Data stored inside a JWT is called a "payload", so our identity function accepts that payload as a parameter
# The payload['identity'] contains the user's id property that we saved into the JWT when we created it.
# The identity function is not called unless we decorate our endpoints with the @jwt_required() decorator
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)