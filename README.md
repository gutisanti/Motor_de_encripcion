Esto se va a cambiar antes de la entrega.
______________________________________________
Utilizar estos metodos de encriptacion
(Twofish, Serpent, AES(Rijindael), Camellia, Salsa20, ChaCha20, Blowfish, CAST5, Kuznyechik, RC4, DES, 3DES, Skipjack, Safer, IDEA)
------------------------------------------------------------------------------------------------------------------------------------

#Encriptar

"Normales"
1. Clave_corriente   S R
2. Mensaje_numero    S R
3. Mensaje_caracteres   S R

"Error"
1. Clave_caracteres_minimo  E
2. Clave_con_letra  S
3. Clave_con_espacios   E
4. Clave_caracteres    S
   
"Extraordinarios"
1. Mensaje_vacio   E R
2. Mensaje_emojis   S
3. Mensaje_sinogramas    E R

#Desencriptar

"Normales"
1. Clave_corriente  E R
2. Mensaje_numero   E R
3. Mensaje_caracteres  E R

"Extraordinario"
1. Mensaje_vacio  S
2. Mensaje_modificado  E
3. Mensaje_none  S

"Error"
1. Clave_incorrecta E
2. Mensaje_no_encriptado  S
3. Mensaje_corrupto  E
4. Clave_vacia  S
