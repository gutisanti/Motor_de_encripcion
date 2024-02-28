Esto se va a cambiar antes de la entrega.
______________________________________________
Utilizar estos metodos de encriptacion
(Twofish, Serpent, AES(Rijindael), Camellia, Salsa20, ChaCha20, Blowfish, CAST5, Kuznyechik, RC4, DES, 3DES, Skipjack, Safer, IDEA)
------------------------------------------------------------------------------------------------------------------------------------

#Encriptar

"Normales"
1. Clave_corriente 
2. Mensaje_numero
3. Mensaje_caracteres

"Error"
1. Clave_caracteres_minimo
2. Clave_con_letra
3. Clave_con_espacios
4. Clave_caracteres
   
"Extraordinarios"
1. Mensaje_vacio
2. Mensaje_emojis
3. Mensaje_sinogramas

#Desencriptar

"Normales"
1. Clave_corriente
2. Mensaje_numero
3. Mensaje_caracteres

"Extraordinario"
1. Mensaje_vacio
2. Mensaje_modificado
3. Mensaje_none

"Error"
1. Clave_incorrecta
2. Mensaje_no_encriptado
3. Mensaje_corrupto
4. Clave_vacia
