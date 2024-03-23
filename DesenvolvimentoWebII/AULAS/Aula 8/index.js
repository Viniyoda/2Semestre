const { createApp } = Vue;

createApp({
    data() {
        return {
            display: "0"
        }
    },
    setup() {
        const numberAfter = 0;
        const numberBefore = 0;
        const operator = '';
        const value = 0;
    },
    methods: {
        lidarBotao(botao) {
            switch (botao)
            {
                case 'X':
                case '/':
                case '-':
                case '+':
                    this.handlerOperator(botao);
                    break;

                case '.':
                    this.handlerDecimal();
                    break;

                case 'C':
                    this.handlerClear();
                    break;

                case '=':
                    this.handlerEquals();
                    break;

                default:
                    this.handlerNumber(botao);
            }
        },
        handlerClear() {
            this.display = '0';
            numberAfter = 0;
            numberBefore = 0;
            operator = '';
            value = 0;
        },
        handlerOperator(botao) {
            this.display = botao;
            operator = botao;
            console.log("O operator digitado foi: ", operator)
            numberBefore = numberAfter;
            numberAfter = 0;
            console.log(numberBefore);
            console.log(numberAfter);
        },
        handlerDecimal() {
            console.log("Entrou no decimal")
        },
        handlerEquals(value) {
            console.log("Entrou no igual");
            if (operator === '/'){
                value = numberBefore / numberAfter;
                console.log(value);
                numberAfter = value;
            }
            if (operator === 'X'){
                value = numberBefore * numberAfter;
                console.log(value);
                numberAfter = value;
            }
            if (operator === '-'){
                value = numberBefore - numberAfter;
                console.log(value);
                numberAfter = value;
            }
            if (operator === '+'){
                value = numberBefore + numberAfter;
                console.log(value);
                numberAfter = value;
            }
            this.display = value;
        },
        handlerNumber(botao) {
            this.display = botao;
            console.log("O botao digitado foi: ", botao);
            numberAfter = parseFloat(botao);
            console.log(numberAfter);
        }
    }
}).mount(app);