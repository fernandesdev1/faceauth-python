let videoStream = null;

async function startCamera() {
    const video = document.getElementById("video");

    try {
        videoStream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = videoStream;
    } catch (err) {
        alert("Erro ao acessar câmera: " + err);
    }
}

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

async function login() {
    const image = captureImage();
    if (!image) return;

    const username = document.querySelector("input[name=username]").value;
    const password = document.querySelector("input[name=password]").value;

    const res = await fetch("/login_face", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username,
            password,
            image
        })
    });

    const data = await res.json();

    if (data.success) {
        alert("✅ " + data.message);
    } else {
        alert("❌ " + data.message);
    }
}