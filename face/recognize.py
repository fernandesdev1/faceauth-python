import face_recognition

def get_face_encoding(image):
    rgb = image[:, :, ::-1]
    encodings = face_recognition.face_encodings(rgb)

    if len(encodings) > 0:
        return encodings[0]

    return None