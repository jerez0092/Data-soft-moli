def guardar_en_txt():
    # Solicitar entradas al usuario
    titulo = input("Escribe el nombre del titulo del juego: ")
    intro = input("Escribe la introducción del juego: ")
    principal = input("Escribe la característica principal como un enunciado: ")
    com_principal = input("Escribe los comentarios entorno al enunciado: ")
    graficos = input("Describe el apartado visual como un enunciado: ")
    com_graficos = input("Escribe los comentarios entorno al enunciado: ")
    gameplay = input("Describe el Gameplay como un enunciado: ")
    com_gameplay = input("Escribe los comentarios entorno al enunciado: ")
    narrativa = input("Describe la historia y la narrativa como un enunciado: ")
    com_narrativa = input("Escribe los comentarios entorno al enunciado: ")
    sonido = input("Describe el apartado sonoro como un enunciado: ")
    com_sonido = input("Escribe los comentarios entorno al enunciado: ")
    negativo = input("Describe lo negativo como un enunciado o simplemente pon Lo negativo: ")
    com_negativo = input("Escribe los comentarios entorno al enunciado: ")
    Nota = input("Coloca una nota: ")
    com_nota = input("Escribe la conclusión si es necesaria: ")

    # Crear el contenido con la estructura HTML
    texto_html = f"""
    <h1>{titulo}</h1>
    <p>{intro}</p>
    <h7>{principal}</h7>
    <p>{com_principal}</p>
    <h7>{graficos}</h7>
    <p>{com_graficos}</p>
    <h7>{gameplay}</h7>
    <p>{com_gameplay}</p>
    <h7>{narrativa}</h7>
    <p>{com_narrativa}</p>
    <h7>{sonido}</h7>
    <p>{com_sonido}</p>
    <h7>{negativo}</h7>
    <p>{com_negativo}</p>
    <h7>{Nota}</h7>
    <p>{com_nota}</p>
    """

    # Guardar el contenido en un archivo de texto
    with open("resumen_juego.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto_html)
    
    print("El archivo TXT se ha guardado exitosamente como 'resumen_juego.txt'.")

# Llamar a la función para guardar el contenido en un archivo de texto
guardar_en_txt()
