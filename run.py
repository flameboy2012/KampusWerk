import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

print app.config['OAUTH_CREDENTIALS_FACEBOOK_ID']

if __name__ == '__main__':
    app.run()