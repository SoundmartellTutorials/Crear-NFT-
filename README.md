# Crear-NFT basado en GAME OF LIFE

**Script Python para crear mis NFT basados en Conway's Game of Life.**

Mis NFT creados con este Script en: [NFTQuoin] (https://nftquoin.com/)

Este script es una variacion de: [GitHub Pages] (https://github.com/jjo9/conway-s-game-of-life-python)

**Agregue algunas funcionalidades:**

  1. Agregar una imagen de fondo para dibujar las celulas basadas en la imagen.
  
  2. Guardar una imagen de la posicion de las celulas en cada interaccion.
  
  3. Guardan las celulas dibujadas para poder cargar el dibujo si cerramos el programa.
  
  4. Agregue algunas teclas para interactuar con el script.
  

**Como utilizar el script?**

 1. Primero busca la imagen sobre la cual quieres dibujar tu NFT.
 
 2. Con algun programa de edicion de imagenes como Photoshop dale transparencia a la imagen y salvala como .PNG
 
 3. poner la imagen .PNG en el mismo directorio del sript
 
 4. Crear Sub Carpeta con nombre Depot. Ahi se guardarán las imagenes!
 
 5. Con un programa de edicion de video como Adobe Premier pongo todas las imagenes guardadas y hago un GIF animado.
 
 Yo utilizo Pycharm. Creo un enviroment y trabajo desde Pycharm para correr el script.
 
 
 El fichero grid_saved.pickle se guarda en Depot y es donde se guarda la info de las celulas que ya se habian dibujado en caso de que cierres el 
 programa y quieras volver. Asi no tendras que dibujar todo de nuevo.
 
 
 Cuando el scrip este corriendo utilizas las teclas para las diferentes funciones:
 
 --- Drawing phase --- 
 
MOUSE - Left and Right click to paint or clear square

S - Stop Drawing Phase and Start Life Phase

m - Reset to first painting 

k - load saved pickle file

C - Clear grid

R - Fill grid at random

Q - Quit Game

--- Life Phase ---

S - Stop Life Phase and Start Drawing Phase

O - To Decrease speed

P - To Increase speed

Q - Quit Game"""
