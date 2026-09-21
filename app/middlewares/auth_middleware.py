from functools import wraps
from flask import flash, redirect, session, url_for


def login_required(f):
  """Bloqueia a rota se o usuário não tiver 'user' na sessão"""

  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user" not in session:
      flash("Faça login para acessar esta página.", "warning")
      return redirect(url_for("auth.login"))
    return f(*args, **kwargs)

  return decorated_function


def guest_required(f):
  """Evita que quem já está logado acesse login/registro"""

  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user" in session:
      return redirect(url_for("auth.welcome"))
    return f(*args, **kwargs)

  return decorated_function