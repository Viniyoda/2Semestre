document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    // Simulação da validação no banco de dados
    if (username === 'usuario' && password === 'senha') {
        // Redirecionar para a tela do jogo (simulado aqui com um alert)
        alert('Login bem-sucedido! Redirecionando para a tela do jogo...');
    } else {
        document.getElementById('error-message').textContent = 'Usuário ou senha incorretos.';
    }
});

document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var newUsername = document.getElementById('newUsername').value;
    var newPassword = document.getElementById('newPassword').value;

    // Simulação de inserção no banco de dados
    // Aqui você deve fazer a lógica para inserir os dados no banco de dados real

    // Exemplo de mensagem de sucesso (simulado)
    document.getElementById('success-message').textContent = 'Cadastro realizado com sucesso!';

    // Limpar os campos após o cadastro
    document.getElementById('newUsername').value = '';
    document.getElementById('newPassword').value = '';
});