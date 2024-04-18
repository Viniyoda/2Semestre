const { createApp } = Vue

createApp({
    data() {
        return {
            heroi: {vida: 100, pocao: 3},
            vilao: {vida: 100, pocao: 3}
        }
    },
    setup() {
        var defenderH = false;
        var defenderV = false;
    },
    methods: {
        atacar(isHeroi) {
            if (isHeroi) {
                console.log("Herói atacou");
                this.acaoVilao();
                if (defenderV == false) {
                    this.vilao.vida -= 10;
                }
                else {
                    console.log("Vilão defendeu o ataque");
                }
            } 
            else {
                console.log("Vilão atacou");
                if (defenderH == false) {
                    this.heroi.vida -= 20;
                }
                else {
                    console.log("Herói defendeu o ataque");
                }
            }
            this.defenderReset();
        },
        defender(isHeroi) {
            if (isHeroi) {
                console.log("Herói defendeu");
                defenderH = true;
                this.acaoVilao();
            }
            else {
                console.log("Vilão defendeu");
                defenderV = true;
            }
        },
        usarPocao(isHeroi) {
            if (isHeroi) {
                console.log("Herói usou poção");
                if (this.heroi.pocao > 0) {
                    this.heroi.pocao -= 1;
                    console.log("Poções restantes Herói: ", this.heroi.pocao);
                    this.heroi.vida += 15;
                    if (this.heroi.vida >= 100) {
                        this.heroi.vida = 100;
                    }
                }
                else {
                    console.log("Herói não tem poções restates")
                }
                this.acaoVilao();
            }
            else {
                console.log("Vilão usou poção");
                if (this.vilao.pocao > 0) {
                    this.vilao.pocao -= 1;
                    console.log("Poções restantes Vilão: ", this.vilao.pocao)
                    this.vilao.vida += 15;
                    if (this.vilao.vida >= 100) {
                        this.vilao.vida = 100;
                    }
                }
                else {
                    console.log("Vilão não tem poções restates")
                }
            }
            this.defenderReset();
        },
        especial(isHeroi) {
            let numCerto = Math.floor(Math.random() * 7);
            let numAtaque = Math.floor(Math.random() * 7);
            if (isHeroi) {
                console.log("Herói usou especial");
                this.acaoVilao();
                if (numAtaque == numCerto) {
                    console.log("Herói acertou o especial");
                    this.vilao.vida -= 20;
                }
            } else {
                console.log("Vilão usou especial");
                if (numAtaque == numCerto) {
                    console.log("Vilão acertou o especial");
                    this.heroi.vida -= 25;
                }
            }
            this.defenderReset();
        },
        acaoVilao() {
            const acoes = [
                'atacar', 'defender',
                'usarPocao', 'especial'];
            const acaoAleatoria = 
            acoes[Math.floor(Math.random() * acoes.length)];
            this[acaoAleatoria](false);
        },
        defenderReset(){
            defenderH = false;
            defenderV = false;
        }
    }
}).mount(app);