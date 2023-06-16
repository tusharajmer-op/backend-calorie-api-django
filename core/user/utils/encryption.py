from django.contrib.auth.hashers import make_password

class hashpassword:
    def hash(self,passwrd):
      return make_password(password=passwrd)