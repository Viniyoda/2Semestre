namespace HelloWorld
//criar um repositorio 
//instalar o GIT
//instalar o NODE.js
//criar a pasta local no PC
//git clone "URL do repositorio"
//npm i -g typescript
//npm i -g ts-node

//npx ts-node (nome do arquivo)
{
   //printf, escreva, print
   console.log("Olá Mundo!!!");

   var numero: number;
   numero = 10;
   console.log(`O número que está alocado na memória é ${numero}`);
   console.log(`O número somado com ele mesmo é (template) ${numero + numero}`);
   var resultado: number = numero + numero;
   console.log(`O número somado com ele mesmo é (normal) ${resultado}`);
   resultado = Math.pow(numero, 10);
   console.log(`O número elevado a 10 é igual: ${resultado}`);
   console.log(`O número elevado a 10 é igual: ${Math.pow(numero, 10)}`);
   resultado = numero % 5;
}