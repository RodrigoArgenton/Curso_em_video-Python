# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
from tv import tv

ligar = tv(True)
ligar.volume(30)
ligar.print_volume()
ligar.volume(diminuir=20)
ligar.print_volume()
ligar.volume(50)
ligar.print_volume()
ligar.volume(diminuir=40)
ligar.print_volume()
ligar.mudar_canal(55)