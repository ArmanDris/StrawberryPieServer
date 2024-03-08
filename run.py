from app import create_app

app = create_app(False)

if __name__ == '__main__':
    app.run(
        host='localhost', 
        port=8000, 
        ssl_context=('/etc/letsencrypt/live/strawberry.ddns.net/fullchain.pem', 
                     '/etc/letsencrypt/live/strawberry.ddns.net/privkey.pem')
        )