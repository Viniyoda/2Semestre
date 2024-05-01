const ComponenteA = {
    template: `
    <div class="componente">
        <h1>Login</h1>
        <label>Email: </label> <input type="email">
        <label>Senha: </label> <input type="password">
    </div>
    `
}

const ComponenteB = {
    template: `
    <div class="componente">
        <h1>Cadastro</h1>
        <label>Email: </label> <input type="email">
        <label>Senha: </label> <input type="password">
        <label>Confirmar Senha: </label> <input type="password">
    </div>
    `
}

const {createApp} = Vue;

createApp({
    data() {
        return {
            componenteAtual: "ComponenteA"
        }
    },
    methods: {
        alterarComponentes() {
            this.componenteAtual = (this.componenteAtual === "ComponenteA") ? "ComponenteB" : "ComponenteA"
        }
    },
    components: {
        ComponenteA,
        ComponenteB
    }
}).mount("#app")