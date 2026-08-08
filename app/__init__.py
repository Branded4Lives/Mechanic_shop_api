from flask import Flask, jsonify
from marshmallow import ValidationError

from config import Config

from .extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from .customers import customers_bp
    from .mechanics import mechanics_bp
    from .service_tickets import service_tickets_bp

    app.register_blueprint(customers_bp, url_prefix="/customers")
    app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
    app.register_blueprint(service_tickets_bp, url_prefix="/service-tickets")

    with app.app_context():
        db.create_all()

    @app.get("/")
    def index():
        return jsonify(
            {
                "message": "Mechanic Shop API",
                "resources": {
                    "customers": "/customers",
                    "mechanics": "/mechanics",
                    "service_tickets": "/service-tickets",
                },
            }
        )

    @app.cli.command("init-db")
    def init_db():
        db.drop_all()
        db.create_all()
        print("Database initialized.")

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({"errors": error.messages}), 400

    @app.errorhandler(404)
    def handle_not_found(error):
        return jsonify({"error": "Resource not found"}), 404

    return app
