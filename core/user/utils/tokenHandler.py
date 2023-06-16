import jwt
import datetime
from user.utils.errors import TokenError
class token:
    secrete = "this is my secrete"
    def createtokken(self,username,role):
        expiry_time = datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        payload = {
            'username': username,
            'role': role,
            'exp': expiry_time
        }
        token = jwt.encode(payload,self.secrete, algorithm='HS256')
        return token
    
    
    def verify_token(token):
        secret_key = 'your-secret-key'

        try:
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            username = payload['username']
            role = payload['role']
            expiry_time = payload['exp']
            current_time = datetime.datetime.utcnow()
            if current_time > expiry_time:
                return False, None
            return {'username': username, 'role': role}
        except jwt.ExpiredSignatureError:
            raise TokenError("Token expired Please relogin")
        except jwt.InvalidTokenError:
            raise TokenError("Invalid Token")