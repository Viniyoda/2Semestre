const { createApp } = Vue

createApp({
    data() {
        return {
            heroi: {vida: 100},
            vilao: {vida: 100}
        }
    },
    setup() {

    },
    methods: {
        atacar(isHeroi) {
            if (isHeroi) {
                console.log("Herói atacou");
                this.acaoVilao();
            } else {
                console.log("Vilão atacou");
                //this.acaoVilao();
            }
        },
        defender() {

        },
        pocao() {

        },
        correr() {

        },
        acaoVilao() {
            const acoes = [
                'atacar', 'defender',
                'pocao', 'correr'];
            const acaoAleatoria = 
            acoes[Math.floor(Math.random() * acoes.length)];
            this[acaoAleatoria](false);
        }
    }
}).mount(app);