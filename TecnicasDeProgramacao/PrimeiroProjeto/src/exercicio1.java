import java.util.Scanner;

public class exercicio1 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        
        // Declaração das variáveis
        int quantidadeHomens = 0;
        int quantidadeMulheres = 0;
        float alturaMaior = 0;
        float alturaMenor = 0;
        float somaAlturasHomens = 0;
        
        // Entrada de dados
        System.out.println("Quantas pessoas serão cadastradas?");
        int quantidadePessoas = entrada.nextInt();
        
         for (int i = 0; i < quantidadePessoas; i++) {
            System.out.println("Informe o sexo da pessoa (M/F):");
            char sexo = entrada.next().charAt(0);

            System.out.println("Informe a altura da pessoa (em metros):");
            float altura = entrada.nextFloat();

            // Verifica se a pessoa é homem ou mulher
            if (sexo == 'M') {
                quantidadeHomens++;
                somaAlturasHomens += altura;
            } else {
                quantidadeMulheres++;
            }

            // Verifica se a altura é maior ou menor que a altura atual
            if (altura > alturaMaior) {
                alturaMaior = altura;
            }

            if (altura < alturaMenor) {
                alturaMenor = altura;
            }
        }

        // Saída de dados
        System.out.println("A maior altura é " + alturaMaior + " metros.");
        System.out.println("A menor altura é " + alturaMenor + " metros.");
        System.out.println("A média de altura dos homens é " + (somaAlturasHomens / quantidadeHomens) + " metros.");
        System.out.println("A quantidade de mulheres é " + quantidadeMulheres);
    }

}
