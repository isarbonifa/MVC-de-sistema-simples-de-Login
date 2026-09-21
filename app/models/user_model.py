# Banco de dados simulado em memória (cuidado: apaga se reiniciar o servidor)
users_db = []


class UserModel:

  @staticmethod
  def find_by_username(username):
    for user in users_db:
      if user["username"] == username:
        return user
    return None

  @staticmethod
  def create_user(username, password):
    users_db.append({"username": username, "password": password})