from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Importa Flask-Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message
import uuid

app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Inicializa Flask-Migrate

# Configuración de Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'tucorreo@gmail.com'
app.config['MAIL_PASSWORD'] = 'tucontraseña'
mail = Mail(app)

# Modelo de Usuario
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Modelo de Sesión (opcional)
class Session(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    session_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(20), default='ACTIVE')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Validar que todos los campos estén presentes
    if not data or not all(key in data for key in ['firstname', 'lastname', 'email', 'password']):
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    # Verificar si el correo electrónico ya está registrado
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({'error': 'El correo electrónico ya está registrado'}), 400

    # Crear un nuevo usuario
    new_user = User(
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        password=generate_password_hash(data['password'], method='pbkdf2:sha256')  # Usar un método alternativo
    )

    db.session.add(new_user)
    db.session.commit()

    # Enviar correo electrónico de bienvenida
    try:
        msg = Message(
            subject='Bienvenido a nuestra plataforma',
            sender='tucorreo@gmail.com',
            recipients=[data['email']]
        )
        msg.body = f'Hola {data["firstname"]},\n\n¡Bienvenido a nuestra plataforma! Gracias por registrarte.'
        mail.send(msg)
    except Exception as e:
        print(f'Error enviando el correo: {e}')

    return jsonify({'message': 'Usuario registrado exitosamente'}), 201

# Endpoint para el login

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Depuración: Imprime los datos recibidos
    print("Datos recibidos:", data)

    # Validar que todos los campos estén presentes
    if not data or not all(key in data for key in ['email', 'password']):
        print("Faltan campos obligatorios")  # Depuración
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    # Buscar al usuario por su correo electrónico
    user = User.query.filter_by(email=data['email']).first()
    print(f"Usuario encontrado: {user}")  # Depuración

    # Verificar si el usuario existe y si la contraseña es correcta
    if user and check_password_hash(user.password, data['password']):
        print("Contraseña válida")  # Depuración
        # Crear una sesión (opcional)
        session_id = str(uuid.uuid4())
        new_session = Session(id=session_id, user_id=user.id)
        db.session.add(new_session)
        db.session.commit()

        # Devolver una respuesta exitosa
        return jsonify({
            'message': 'Inicio de sesión exitoso',
            'session_id': session_id,
            'user': {
                'id': user.id,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'email': user.email
            }
        }), 200
    else:
        print("Credenciales inválidas")  # Depuración
        return jsonify({'error': 'Credenciales inválidas'}), 401

# Endpoint para cerrar sesión (opcional)
@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()

    # Validar que el session_id esté presente
    if not data or 'session_id' not in data:
        return jsonify({'error': 'Falta el ID de sesión'}), 400

    # Buscar la sesión y marcarla como inactiva
    session = Session.query.filter_by(id=data['session_id']).first()
    if session:
        session.status = 'INACTIVE'
        db.session.commit()
        return jsonify({'message': 'Sesión cerrada exitosamente'}), 200
    else:
        return jsonify({'error': 'Sesión no encontrada'}), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas en la base de datos
    app.run(debug=True)