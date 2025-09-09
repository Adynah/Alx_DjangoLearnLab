import secrets
import string

def generate_django_secret_key(length=50):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__== '__main__':
    print(generate_django_secret_key())