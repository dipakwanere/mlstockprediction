from . import create_app
import os


def main():
    config = None
    app = create_app(config)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


if __name__ == "__main__":
    main()
