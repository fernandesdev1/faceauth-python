import face_recognition
import cv2

def get_face_encoding(image):
    try:
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        locations = face_recognition.face_locations(rgb)

        if len(locations) == 0:
            return None

        encodings = face_recognition.face_encodings(rgb, locations)

        if len(encodings) > 0:
            return encodings[0]

        return None

    except Exception as e:
        print("Erro face:", e)
        return None