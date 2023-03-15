# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
from contacorrente import contacorrente

pessoa1 = contacorrente(12345, 'pessoa1', 0)
pessoa1.alterarNome('pessoa1nova')
pessoa1.deposito(5000)
pessoa1.saque(1245)
pessoa1.saque(3000)
pessoa1.saque(6000)
pessoa1.deposito(15000)
pessoa1.saque(3000)
pessoa1.saque(6000)
pessoa1.saque(4596)
pessoa1.extrato()