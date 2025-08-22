from . import create_app
import os

# Expose a module-level `app` for WSGI servers (gunicorn expects this)
app = create_app()


def main():
    config = None
    # Use the app variable to run dev server
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


if __name__ == "__main__":
    main()
