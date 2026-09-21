from flask import Flask


def create_app():
  app = Flask(
      __name__, template_folder="views/templates", static_folder="views/static"
  )
  app.secret_key = (
      "chave-secreta-simples"  # Necessário para usar o session do Flask
  )

  from app.controllers.auth_controller import auth_bp

  app.register_blueprint(auth_bp)

  return app