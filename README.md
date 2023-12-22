# SEL0337
Projetos em Sistemas Embarcados

A prática consistiu em aplicar os conceitos aprendidos no curso para a execução de dois projetos na Raspberry Pi 3B+: 
Uso de uma tag RFID para um sistema de segurança e o uso do módulo de câmera para acender um led 3 vezes caso identificasse um rosto.


##Tag RFID na Raspberry
Utiizou-se de tag RFID (radio frequency identification) que opera no protocolo SPI (Serial Peripheral Interface) para salvar uma determinada mensagem em seu chip acoplado. Ao aproximar a tag do leitor que está emitindo ondas eletomagnéticas na frequência de 13.5 MHz. Essas ondas induzem uma corrente no indutor presente na tag e que, por sua vez, será responsável por ativar o chip interno e permitir a leitura.

<details open>
    <summary>Itens Usados</summary>
    <ul>
        <li>Módulo RFID-MFRC52</li>
        <li>Jumbers</li>
        <li>Protoboard</li>
        <li>Raspberry Pi 3B+</li>
    </ul>
</details>

Fez-se as conexões de acrodo com a figura 1 e aseguindo o esquemático da figura 2.
![image](https://github.com/HandelNatividade/SEL0337/assets/68929575/0fa25dde-063b-4816-8cbb-55072d80b43a)
Figura 1: Tabela de I/O para a conexão do módulo RFID-MFRC52.

![image](https://github.com/HandelNatividade/SEL0337/assets/68929575/80a4a4b5-c580-4f8f-9144-18a9b11e3f84)
Figura 2: Esquemático de ligação da Raspberry no módulo

Usou-se o código xxx.py no terminal linux da raspbery para executar o programa

![image](https://github.com/HandelNatividade/SEL0337/assets/68929575/1c03dc34-98cd-49df-a4fb-b401d328854a)
Figura 3: Montagem Final.



![image](https://github.com/HandelNatividade/SEL0337/assets/68929575/3cba2e6a-434c-47bd-b350-c94bd7a3f539)
