# FaceAuth 🔐

Sistema de autenticação web desenvolvido em Python com Flask que combina login com usuário e senha + verificação facial via webcam.

## 🚀 Funcionalidades

- Cadastro de usuários
- Login com usuário e senha
- Captura de imagem pela webcam (navegador)
- Reconhecimento facial no backend
- Armazenamento com SQLite

## 🛠️ Tecnologias

- Python
- Flask
- OpenCV
- face_recognition
- SQLite
- HTML, CSS, JavaScript

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/faceauth.git
cd faceauth
pip install -r requirements.txt
```

## ▶️ Como usar
```
python app.py
```

Acesse no navegador:
    http://localhost:5000


## ⚠️ Requisitos
- Webcam habilitada no navegador
- Permitir acesso à câmera
- Boa iluminação para melhor reconhecimento


## 🔮 Melhorias futuras
- Hash de senha (bcrypt)
- Sistema de autenticação com sessão ou JWT
- Interface mais moderna
- Proteção contra spoofing