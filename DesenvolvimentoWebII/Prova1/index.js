const { createApp } = Vue

createApp({
    data() {
        return {
            heroi: {vida: 100},
            vilao: {vida: 100}
        }
    },
    setup() {
        const defender = false;
    },
    methods: {
        atacar(isHeroi) {
            if (isHeroi) {
                console.log("Herói atacou");
                this.acaoVilao();
                this.vilao.vida -= 10;
            } else {
                console.log("Vilão atacou");
                this.heroi.vida -= 20;
            }
        },
        defender(isHeroi) {
            if (isHeroi) {
                console.log("Herói defendeu");
                defender = true;
            } else {
                console.log("Vilão defendeu");
                defender = true;
            }
        },
        pocao(isHeroi) {
            if (isHeroi) {
                console.log("Herói usou poção");
                this.acaoVilao();
                this.heroi.vida += 15;
            } else {
                console.log("Vilão usou poção");
                this.heroi.vida += 25;
                
            }
        },
        correr(isHeroi) {
            if (isHeroi) {
                console.log("");

            } else {
                console.log("");

            }
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