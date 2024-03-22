const { createApp } = Vue;

createApp({
    data() {
        return {
            display: "0",
            numeroAnterior: null,
            numeroAtual: null,
            operador: null
        }
    },
    methods: {
        lidarBotao(botao) {
            switch (botao)
            {
                case 'X':
                case '/':
                case '-':
                case '+':
                    this.lidarOperador(botao);
                    break;

                case '.':
                    this.lidarDecimal();
                    break;

                case 'C':
                    this.lidarLimpar();
                    break;

                case '=':
                    this.lidarIgual();
                    break;

                default:
                    this.lidarNumeros(botao);
            }
        },
        lidarOperador(botao) {
            console.log("O botao digitado foi: ", botao);
        },
        lidarDecimal() {
            console.log("Entrou no decimal")
        },
        lidarLimpar() {
            this.display = '0';
            this.numeroAtual = null;
            this.numeroAnterior = null;
            this.operador = null;
        },
        lidarIgual() {
            console.log("Entrou no igual");
        },
        lidarNumeros(botao) {
            console.log("O botao digitado foi: ", botao);
            this.display = botao;
            let numeroAtual = parseFloat(botao);
            console.log(numeroAtual);
        }
    }
}).mount(app);