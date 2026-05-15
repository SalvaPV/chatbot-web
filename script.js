function agregarMensaje(texto, clase){
    let chatBox = document.getElementById('chat-box');
    let div = document.createElement('div');
    div.className = clase;
    div.innerHTML = '<span>' + texto + '</span>';
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function enviarMensaje(){
    let input = document.getElementById('mensaje');
    let mensaje = input.value;

    if(mensaje == '') return;

    agregarMensaje(mensaje, 'user');
    input.value = '';

    fetch('chat.php', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: 'mensaje=' + encodeURIComponent(mensaje)
    })
    .then(response => response.text())
    .then(data => {
        agregarMensaje(data, 'bot');
    });
}

document.getElementById('mensaje').addEventListener('keypress', function(e){
    if(e.key == 'Enter'){
        enviarMensaje();
    }
});

//mensaje de bienvenida
document.addEventListener('DOMContentLoaded', function(){
    agregarMensaje('Hola! Soy tu asistente virtual.', 'bot');
});
