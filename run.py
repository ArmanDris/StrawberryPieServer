import argparse
from app import create_app

parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true', help='run with http locally on port 3001 and test database')
args = parser.parse_args()

app = create_app(test=args.test)

if __name__ == '__main__':
    app.run(
        host='localhost', 
        port=8000, 
        ssl_context=('/etc/letsencrypt/live/strawberry.ddns.net/fullchain.pem', 
                     '/etc/letsencrypt/live/strawberry.ddns.net/privkey.pem')
        )