let stream;

// camera
async function startCamera() {
    const video = document.getElementById("video");

    stream = await navigator.mediaDevices.getUserMedia({ video: true });
    video.srcObject = stream;
}

// captura
function captureImage() {
    const video = document.getElementById("video");

    if (!video.srcObject) {
        alert("Abra a câmera primeiro!");
        return null;
    }

    const canvas = document.createElement("canvas");
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");
    ctx.drawImage(video, 0, 0);

    return canvas.toDataURL("image/jpeg");
}

async function loginUser() {
    const res = await fetch("/login_user", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: document.querySelector("input[name=username]").value,
            password: document.querySelector("input[name=password]").value
        })
    });

    const data = await res.json();

    if (data.success) {
        window.location.href = "/verify";
    } else {
        alert(data.message);
    }
}

async function verifyFace() {
    const image = captureImage();
    if (!image) return;

    const res = await fetch("/verify_face", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ image })
    });

    const data = await res.json();

    if (data.success) {
        window.location.href = "/dashboard";
    } else {
        alert(data.message);
    }
}

async function registerUser() {
    const res = await fetch("/register_user", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: document.querySelector("input[name=username]").value,
            password: document.querySelector("input[name=password]").value
        })
    });

    const data = await res.json();

    if (data.success) {
        alert("Conta criada! Agora registre seu rosto.");
    } else {
        alert(data.message);
    }
}

async function registerFace() {
    const image = captureImage();
    if (!image) return;

    const res = await fetch("/register_face", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: document.querySelector("input[name=username]").value,
            password: document.querySelector("input[name=password]").value,
            image
        })
    });

    const data = await res.json();
    alert(data.message);

    if (data.success) {
        window.location.href = "/";
    }
}