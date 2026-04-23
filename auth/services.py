import base64
import numpy as np
import cv2
import pickle
import face_recognition
from database import connect
from face.recognize import get_face_encoding


def base64_to_image(image_data):
    image_data = image_data.split(",")[1]
    image_bytes = base64.b64decode(image_data)
    np_arr = np.frombuffer(image_bytes, np.uint8)
    return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)


def register_user(username, password, image_data):
    img = base64_to_image(image_data)
    encoding = get_face_encoding(img)

    if encoding is None:
        return False, "Rosto não detectado"

    conn = connect()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password, face_encoding) VALUES (?, ?, ?)",
            (username, password, pickle.dumps(encoding))
        )
        conn.commit()
    except:
        return False, "Usuário já existe"
    finally:
        conn.close()

    return True, "Usuário registrado com sucesso"


def login_user(username, password, image_data):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password, face_encoding FROM users WHERE username = ?",
        (username,)
    )

    user = cursor.fetchone()
    conn.close()

    if not user:
        return False, "Usuário não encontrado"

    db_password, db_encoding = user

    if password != db_password:
        return False, "Senha incorreta"

    img = base64_to_image(image_data)
    encoding = get_face_encoding(img)

    if encoding is None:
        return False, "Rosto não detectado"

    saved_encoding = pickle.loads(db_encoding)

    match = face_recognition.compare_faces([saved_encoding], encoding)[0]

    if match:
        return True, "Login realizado com sucesso"
    else:
        return False, "Rosto não reconhecido"