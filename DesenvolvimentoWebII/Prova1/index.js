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
        usarPocao(isHeroi) {
            if (isHeroi) {
                console.log("Herói usou poção");
                this.heroi.vida += 15;
                if (this.heroi.vida >= 100) {
                    this.heroi.vida = 100;
                }
                this.acaoVilao();
            } else {
                console.log("Vilão usou poção");
                this.vilao.vida += 25;
                if (this.vilao.vida >= 100) {
                    this.vilao.vida = 100;
                }
                
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