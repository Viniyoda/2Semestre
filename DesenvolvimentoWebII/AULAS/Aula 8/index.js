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
            this.display = botao;
            var operador = '';
            operador = botao;
            console.log("O operador digitado foi: ", operador)
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
            this.display = botao;
            console.log("O botao digitado foi: ", botao);
            let numeroAtual = parseFloat(botao);
            let numeroAnterior = 0;
            console.log(numeroAtual);
            if (operador == '+'){
                numeroAnterior = numeroAtual;
                numeroAtual = parseFloat(botao);
            }
        }
    }
}).mount(app);