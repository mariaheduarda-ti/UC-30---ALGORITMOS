programa {

    funcao inicio() {

        real valorCasa
        real salario
        real prestacaoMensal
        inteiro anos
        inteiro meses
        

        escreva("Digite o valor da casa: ")
        leia(valorCasa)

        escreva("Digite o seu salario: ")
        leia(salario)

        escreva("Em quantos anos você vai pagar: ")
        leia(anos)

        meses = anos * 12
        prestacaoMensal = valorCasa / meses

        escreva("Valor da prestacao mensal: ", prestacaoMensal)

        se(prestacaoMensal <= salario * 0.30) {
            escreva("Emprestimo APROVADO! \n")
        } senao {
            escreva("Emprestimo NEGADO! \n")
        }

    }
}