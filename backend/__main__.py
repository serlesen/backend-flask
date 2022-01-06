from backend import create_app, db, feed_db

app = create_app()

if __name__ == "__main__":
    db.create_all()
    feed_db()
    app.run()
