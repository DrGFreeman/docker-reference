from app import app

if __name__ == "__main__":
    app.server.run(host="0.0.0.0", port=5000)