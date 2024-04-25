const {createApp} = Vue

createApp({
    data(){
        return {
            componenteAtual: "ComponenteA"
        }
    },
    methods: {
        alterarComponentes() {
            this.componenteAtual = (this.componenteAtual === "ComponenteA")
            ? "ComponenteB" : "ComponenteA"
        }

    },
    components: {
        ComponenteA,
        ComponenteB
    }
}).mount("#app")