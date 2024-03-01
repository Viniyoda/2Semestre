namespace vetor 
// normalmente chamado de array
{
    let num: number[] = [2,4,6,8];
    let valor: number = num[3];
    console.log(valor);
    console.log(num);
    /*
    console.log(num[0]);
    console.log(num[1]);
    console.log(num[2]);
    console.log(num[3]);
    */

    for (let i: number = 0; i < num.length; i++)
    {
        console.log(num[i]);
    }

    /*
    let cores: Array<string> = ["vermelho", "verde", "azul"];
    let cores: <string> = ["vermelho", "verde", "azul"];
    */

    type Aluno = {
        ra : number,
        nome : string,
        idade : number
    }

    let alunos: Aluno[];

    alunos = [{
        ra: 123123123123,
        nome: "fulano",
        idade: 10
    },
    {
        ra:223223223223,
        nome: "Ciclano",
        idade: 91
    }]

    alunos.forEach(function (aluno:Aluno):void{
        console.log(aluno)
    })

    let quadrados: number[]
    quadrados =num.map(function (numero:number){
        return numero * numero;
    })

    
}