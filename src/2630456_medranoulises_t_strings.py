# Ángel Ulises Medrano Álvarez
# 2630456
# IM 1-3

# Problema 1:
"""
    Usamos input() para la entrada del nombre, el nombre lo
    normalizamos usando .strip(), y despues usamos el .split()
    para separar cada palabra del nombre y guardarla en una variable
    llamada 'words', a continuación, usamos if para que los nombres
    que vengan vacios (Solo le da enter) tengan una respuesta creativa,
    después, usando 'else', si el nombre si tiene palabras, reasignamos
    el valor de 'full_name' con la función .join() para unir las palabras
    y despues usamos .title() para que la primera letra de cada palabra
    sea mayuscula, y asignamos un string vacio a la variable 'initials',
    posteriormente usamos un for aux in, donde asignamos a intials el 
    string vavio del primer initials, y obtener la primera letra de
    cada palabra y la hacemos mayuscula con .upper() y le sumamos un
    punto para separarlas, para finalmente imprimir el nombre
    formateado y las iniciales del nombre completo (Tanto nombres
    como apelldos).
"""
name = input("Nombre Completo Porfavor: ")
full_name = name.strip()
words = full_name.split()
if len(words) == 0:
    print("Eh we... no seas asi\n")
else:
    full_name = " ".join(words)
    formatted_name = full_name.title()
    initials = ""
    for word in words:
        initials = initials + word[0].upper() + "."
    print("Formatted name:", formatted_name)
    print("Initials:", initials)
    print("\n")

# Problema 2:
"""
    Utilizamos input para pedir el dato de correo electronico,
    el metodo .find() para elegir un elemento de nuestra
    variable y definirla como arroba (En ingles segun google
    'at sign'). y con la técnica llamada slicing, podemos obtener
    una parte de una cadena de un string, en este caso, deseamos el
    dominio, el cual es todo lo que sobra despues del '@', por ende
    designamos 'domain' con la técnica slicing como todo lo que se
    encuentra apartir de una posicion despues del '@', de esta forma,
    nos aseguramos que sin importar cuantas posiciones esten ocupadas
    antes del @, siempre obtengamos como dominio todo lo que se
    encuentra despues del '@'.

    Utilizando 'if', nos aseguramos de que si se cumplen los
    requisitos que serian solo un '@', solo un '.' en el dominio,
    y que no exista ningun espacio ' ' en el email, el correo sea
    validado como verdader 'True', en caso contrario, usaremos 'else'
    para declarar que si no se cumplen estos requisitos, el email sera
    validado como falso 'False'.
"""
email_text = input("Ingrese su correo electronico porfavor ;3: ")
email_text = email_text.strip()
at_sign = email_text.find("@")
domain = email_text[at_sign + 1:]
print(email_text)
if email_text == "":
    print("Eh we... no seas así\nError\n")
else:
    if email_text.count("@") == 1 and "." in domain and " " not in email_text:
        print("Valid email: True")
        print("Dominio:", domain)
        print("\n")
    else:
        print("Valid email: False")
        print("Post: Eres un ojete.\n")
# Problema 3:
"""
    Con input() solicitamos una palabra para revisar si es un
    palindromo, usamos el .strip() para eliminar espacios innecesarios.
    con el primer if, declaramos que si el dato entregado esta vacio,
    le respondemos al muy graciosito como se merece. En caso contario,
    ese dato que se dio le sacaremos todos los espacios innecesarios
    que tenga, y a continuación le aplicamos el metodo .lower() para
    que todas las letras de nuestro string e conviertan en minusculas
    (Esto es vital para la comparación de strings). despues, con el 
    metodo .replace() asesinamos/eliminamos todos los espacios que
    haya dentro de nuestro string reemplazandolos con nada
    (String vacio, de esta forma la comparación se realizara de forma
    más correcta). Luego con un if con len() detectamos que si el
    palindromo tiene menos de 4 caracteres le decimos que lo tiene
    muy chiquito, en caso contrario, usando el metodo slicing inverso,
    guardamos la version inversa del palindromo en text_in_reverse, y
    a continuación con if comparamos ambas variables, si se da el caso
    de que ambas variables son iguales, pus le decimos que si jalo,
    en caso contrario pus le decimos que no jalo y ya, es toda.
"""
phrase = input("Ingrese su palindromo todo feo: ")
phrase = phrase.strip()
if phrase == "":
    print("Quiero que te vayas de mi programa...\nDigo, ERROR\n")
else:
    formatted_phrase = phrase.lower()
    text = formatted_phrase.replace(" ", "")
    if len(text) < 4:
        print("Lo tienes muy chiquito\n(El palindromo...)\n")
    else:
        text_in_reverse = text[::-1]
        if text == text_in_reverse:
            print("Hey, si jalo :D\n")
        else:
            print("No pus, no pus no jala pá, no es palindromo\n")
# Problema 4:
"""
    Con un input() pedimos una oración, a la cual le retiramos los
    espacios innecesarios usandoo .strip(). A continuación comparamos
    con un if y un == que si la oración que recibimos esta vacia, le
    avisaremos al graciosito que lo vamos a madrear si no le baja a
    su pedo. En caso contrario haremos minusculas las letras del
    string para trabajar mas comodamente con el string, y esto lo
    guardamos en la variable 'formatted_sentence', a su vez usamos el
    metodo .split() para separar cada palabra de la oración y guardarlas
    en la variable 'words'. A continuación, usando un if comprobamos
    si la tiene muy chiquita (La oración). En caso contrario
    imprimiremos: 'El numero de palabras de la oración, la primera
    palabra de la oración, la ultima palabra de la oración , la palabra
    más corta de la oración en terminos de longitud gracias a
    min(words, key=len), y la palabra más larga de la oración en
    terminos de longitud gracias a max(words, key=len). Y ya, estoda.
    '"""
sentence = input("Dame tu oración toda mamalona y poderosa: ")
sentence = sentence.strip()
if sentence == "":
    print("Te voy a madrear wey, parale a tu pedo\nDigo, ERROR\n")
else:
    formatted_sentence = sentence.lower()
    words = formatted_sentence.split()
    if len(words) < 6:
        print("La tienes muy chiquita\n(La oración...)\n")
    else:
        print(F"Word count: {len(words)}")
        print(F"First word: {words[0]}")
        print(F"Last word: {words[-1]}")
        print(F"Shortest word: {min(words, key=len)}")
        print(F"Longest word: {max(words, key=len)}")
# Problema 5:
"""
    Pedimos la contraseña con input(), vereificamos que no venga vacia
    la contraseña con if, en caso contrario lo que hacemos es designar
    como falsas las variables que nos ayudaran más adelante. A
    continuación, usamos un for aux in para recorrer cada caracter
    de la contraseña para designar en que momento las variables
    anteriores se consideraran verdaderas.Posteriormente usando if y
    elif (Alch profe, no encontre otra manera de no usar elif, y mi
    compañero me recomendo usar elif) aplicamos las condiciones que
    deben cumplirse para que la contraseña sea clasificada como:
    'weak, medium, o strong'.
"""
password = input("Pon tu contraseña papu *guiño guiño*: ")
if password == "":
    print("ERROR: NO PUEDES TENER VACIA TU CONTRASEÑA, MEJOR CAMBIATE DE CARRERA\n")
else:
    has_upper = False
    has_lower = False
    has_digit = False
    has_special_character = False
    for character in password:
        if character.isupper():
            has_upper = True
        elif character.islower():
            has_lower = True
        elif character.isdigit():
            has_digit = True
        else:
            has_special_character = True
    if len(password) < 8 or password == password.lower():
        strength = "weak"
        print(F"Password strength: {strength}")
    elif len(password) >= 8 and has_lower and has_upper and has_digit and not has_special_character:
        strength = "medium"
        print(F"Password strength: {strength}")
    elif len(password) >= 8 and has_lower and has_upper and has_digit and has_special_character:
        strength = "strong"
        print(F"Password strength: {strength}")
# Problema 6:
"""
    Pedimos con un input() el nombre del producto, y con otro input()
    pedimos el precio de dicho producto (Cada uno guardado en una
    variable diferente), una vez defnidas ambas variables, usamos
    .strip() para quitarle espacios innecesarios. A continuación
    verificamos que ninguna de las dos variables este vacia con un if.
    Posteriormente, utilizamos try: para haceer una operación que
    puede generar un error para que, usando float, convertimos el
    texto del precio en un numero decimal, asi mismo, si el precio no
    se puede convertir en numero debido a que se dio un dato que no es
    posible de convertir a numero, try: mandara a que se ejecute el
    except del final, e indicamos que si se entrega un precio
    negativo (Por eso que sea inferior a 0) se de el mensaje de ERROR.
    En caso contrario, convertiremos la variable de tipo entero en una
    variable de tipo string usando el str, y juntamos todo en la
    variable label (Tanto el nombre como precio del producto), y luego
    volvemos a asignar a label el dato que solo empiece desde su
    inicio y llegue al indice numero 30, y posteriormente, usamos el
    metodo .ljust() para que se rellene con espacios la variable
    label hasta que tenga 30 caracteres/indices. A continuación,
    imprimimos nuestra variable label. Finalmente, colocando en la
    identación de try:, colocamos el except para declarar que se
    mostrara como error si no es posible la primera accion de try:.
"""
product_name = input("Nombre epicamentewandingo del producto: ")
price_value = input("Precio (barato porfavor) del producto: ")
product_name = product_name.strip()
price_value = price_value.strip()
if product_name == "" or price_value == "":
    print("ERROR: Esta vacio el nombre y/o precio del producto\n")
else:
    try:
        price_number = float(price_value)
        if price_number < 0:
            print("ERROR: Tu precio no puede ser negativo tonto")
        else:
            price_text = str(price_number)
            label = f"Producto: {product_name} Precio: ${price_text}"
            label = label[:30]
            label = label.ljust(30)
            print("Label: "+label+'"')
    except ValueError:
        print("ERROR: Tu precio no es un numero valido we, \n")

# Asu maquina profe, esta canijo esta vaina, alch no se si podre acabar la segunda tarea pero haber que pex, sinceramente me parece increible y fascinante como todo debe llevar un orden muy especifico y como cada especificacion debe estar bien detallada para poder ejercer una condicion y entregar lo que se debe entregar.
# No pus, el lower() apoya cuando hay condiciones con minusculaer y sobretodo en comparacion de datos, el strip() es escencial para poder trabajar más comodamente con un dato recibido al deshacerce de espacios innecesarios, split() nos apoya cuando se debe trabajar con varios datos de un solo string, join() hace su chambita al unir varios textos, etc Xd.
# Al normalizar un texto se nos es posible realizar una comparación precisa y más coherente entre dos strings.
# Al verificar que no se entregue un dato vacio o que no cumpla con los requesitos pedidos, podemos evitar datos erroneos (O que no esten destinado a ser trabajados con el programa) y datos cuya información no sea adecuada para el programa aunque no marque error.
# Los strings pueden cambiar dependiendo de lo que se necesite, mientas que por otro lado los slices me permiten obtener indices de un texto sin modificar el string original.
# Referencias:
# 1) Python Software Foundation. Python Documentation:Text Sequence Type — str.
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
# 2) Python Software Foundation. Python Documentation:String Methods.
#    https://docs.python.org/3/library/stdtypes.html#string-methods
# 3) Python Software Foundation. Python Tutorial:An Informal Introduction to Python.
# https://docs.python.org/3/tutorial/introduction.html
# 4) Python Software Foundation. Python Documentation:Input and Output.
# https://docs.python.org/3/tutorial/inputoutput.html
# 5) Python Software Foundation. Python Documentation:Built-in Functions.
# https://docs.python.org/3/library/functions.html