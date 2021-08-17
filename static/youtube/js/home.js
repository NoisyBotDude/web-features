function videoSuccess() {
    if(document.getElementById("video-form-input").value==="") {
        document.getElementById("video-button").disabled = true;
        document.getElementById("audio-button").disabled = true;
    } else {
        document.getElementById("video-button").disabled = false;
        document.getElementById("audio-button").disabled = false;
    }
}

function playlistSuccess() {
    if(document.getElementById("playlist-form-input").value==="") {
        document.getElementById("playlist-button").disabled = true;
    } else {
        document.getElementById("playlist-button").disabled = false;
    }
}