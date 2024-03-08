import argparse
from app import create_app

parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true', help='run with http locally on port 3001 and test database')
args = parser.parse_args()

if __name__ == '__main__':
    if args.test:
        app = create_app(test=True)
        app.run(host='127.0.0.1', port=3001)

    else:
        app = create_app()
        app.run(
            host='0.0.0.0', 
            port=443, 
            ssl_context=('/etc/letsencrypt/live/strawberry.ddns.net/fullchain.pem', 
                         '/etc/letsencrypt/live/strawberry.ddns.net/privkey.pem')
            )