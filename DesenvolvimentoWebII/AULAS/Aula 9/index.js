const { createApp } = Vue;

createApp({
    data() {
        return{
            firstName: '',
            lastName: '',
            status: false,
            destruir: ''
        }
    },
    methods: {
        fullName(){
            return (this.firstName + " " + this.lastName)
        },
        onOff(){
            return this.status = !this.status;
        }
    }/*,
    whatch: {
        destruir(newDestruir){
            if (newDestruir === 'quebrar'){
                setTimeout(() => {
                    this.destruir = 'ok';
                });
            }
        }
    }*/
}).mount("#app");