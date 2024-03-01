namespace exercicio4
{
    /*
    Crie um array com 4 objetos, cada um representa um livro com as
    propriedades TITULO, AUTOR E ANO. Em seguida use o método map()
    para criar um novo array(string) contendo apenas os titulos
    */

    type livro = {
        titulo : string,
        autor : string,
        ano : number
    }

    let livros : livro[];

    livros = [
        {
            titulo:"O Hobbit",
            autor:"J.R.R.Tolkien",
            ano:1937
        },
        {
            titulo:"A Guerra dos Mundos",
            autor:"H.G.Wells",
            ano:1898
        },
        {
            titulo:"Viagem ao Centro da Terra",
            autor:"Júlio Verne",
            ano:1864
        },
        {
            titulo:"Fahrenheit 451",
            autor:"Ray Bradbury",
            ano:1953
        }
    ]

    let titulosLivros: string[];
    titulosLivros = livros.map(function (titu:livro){
        return titu.titulo;
    })

    console.log(titulosLivros)

}