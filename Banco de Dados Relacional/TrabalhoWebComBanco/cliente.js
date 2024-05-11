document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Enviar solicitação para o servidor Node.js
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => {
        if (response.ok) {
            // Redirecionar para a tela do jogo
            window.location.href = 'joguinho.html';
        } else {
            // Exibir mensagem de erro
            document.getElementById('error-message').textContent = 'Usuário ou senha incorretos.';
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});