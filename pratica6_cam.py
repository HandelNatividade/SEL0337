#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Escola de Engenharia de São Carlos
#Handel Emanuel Natividade Peres  12681368


#IMPORTO AS BIBLIOTECAS

#from gpiozero import LED
import cv2
import os
import time
from gpiozero import LED
from picamera2 import Picamera2

#DEFINO O LOCAL DOS PINOS
led = LED(17)
#buzzer = Buzzer(17)

face_detector = cv2.CascadeClassifier("/home/sel/12681368/haarcascade_frontalface_default.xml")#UTILIZO O ARQUIVO SALVO NO SEGUINTE DIRETÓRIO
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format":'XRGB8888',"size":(640, 480)})) #DEFINO A FORMATACAO DA CAMERA
picam2.start() #INICIO
output_directory = "detected_faces" #DEFINO ONDE SERÃO SALVAS AS IMAGENS TIRADAS

os.makedirs(output_directory,exist_ok=True)#VERIFICO SE EXISTE A PASTA

while True:
	im = picam2.capture_array()
	grey = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	faces = face_detector.detectMultiScale(grey,1.1,5)

	for(x,y,w,h) in faces:
		cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0)) #CAPTURO O ROSTO	
		timestamp = int(time.time())
		filename = os.path.join(output_directory,f"face_{timestamp}.jpg")

		#AO IDENTIFICAR UM ROSTO, O LED PISCA
		for x in range(3):
			led.on()
			time.sleep(0.25)
			led.off()
		cv2.imwrite(filename,im[y:y+h,x:x+w])#SALVO A IMAGEM
	cv2.imshow("Camera",im)
	cv2.waitKey(1000)
