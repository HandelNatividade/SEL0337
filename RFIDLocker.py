#Dep. de Engenharia Elétrica e Computação - EESC - USP
#Handel Emanuel N. Peres
#n USP: 12681368

#27 de Novembro de 2021

#Este código visa gravar um texto em uma tag RFID
from gpiozero import LED
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
#Coloco os Warnings como falso
GPIO.setwarnings(False)

LEDR = LED(17) #defino onde esta o led
LEDG = LED(27) #defino onde esta o led


leitor = SimpleMFRC522()
while True :
    count = 3
    a = int(input('Para gravar digite -> 2 \nPara ler digite    -> 1\nModo Fechadura     -> 0\n'))
    print(a)
    if a == 2:
        #Crio a variavel em string que vai armazenar o texto que gravarei na tag 
        mensagem = "ABC"
        print ("\n Aproxime a tag: ")
        leitor.write(mensagem) #gravo a mensagem
        print("\n Mensagem gravada!\n")
        sleep(3)
        a = 5
        
    elif a == 1:
        while a == 0:
            print ("\n Aproxime a tag: ")
            sleep(3)
            id,mensagem = leitor.read()
            print("ID: {}\n\Texto: {}".format(id, mensagem))
            sleep(1)
            a = 5
    elif a == 0:
        print ("\n Aproxime a tag: ")
        id,mensagem = leitor.read()
        if id == 427707964172:
            print("Acesso Liberado!\n")
            while count > 0:
                LEDG.on()
                sleep(0.25)
                LEDG.off()
                sleep(0.25)
                count = count-1
        else:   
            print("Acesso Negado!\n")
            while count > 0:
                LEDR.on()
                sleep(0.25)
                LEDR.off()
                sleep(0.25)
                count = count-1
                
    else:
        print("Numero nao aceito\n")


