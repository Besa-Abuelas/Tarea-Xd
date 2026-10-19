# Ángel Ulises Medrano Álvarez
# 2630456
# IM 1-3

# Problema 1:
"""
    Utilizando el input() pedimos el dato de grados Celcius, y una vez
    obtenido, usando try: realizaremos las operaciones de conversion de
    temperaturas (Y nos dara error si damos letras en lugar de numeros),
    convertimos de una los grados celcius a Kelvin y los guardamos en
    una variable de ese dato. Posteriormente verificamos que nuestros
    grados Kelvin no ean negativos (Osea, grados negativos Kelvin), si
    es negativo, marcamos esto como un error, en caso contrario,
    proseguimos con convertir los grados Celcius a grados Fahrenheit
    y guardamos ese dato en su respectiva variable. Posteriormente,
    definimos que high_temperature sera igual a 'True' si los grados
    celcius son 30 o más, en caso contrario, su valor sera 'False'. Y
    por ultimo imprimimos las tres variables.
"""
temperature_c = input("Haber carnalito, hechamelo (Los grados Celcius): ")
try:
    temperature_c = float(temperature_c)
    temperature_k = temperature_c + 273.15
    if temperature_k < 0.0:
        print("ERROR: Haber we, explicame tu ¿De donde chuchas te sacas -273.15 ºC? Ni que vivieras en el artico")
    else:
        temperature_f =  temperature_c*9/5+32
        if temperature_c >= 30.0:
            high_temperature = "True"
        else:
            high_temperature = "False"
        print(F"Fahrenheit: {temperature_f}")
        print(F"Kelvin: {temperature_k}")
        print(F"High temperature: {str(high_temperature).lower()}")
except ValueError:
    print("ERROR: False")
# Problema 2
"""
    pedimos con input() pedimos primero las horas de trabajo a la
    semana, y con otro input() pedimos cuanto le pagan al carnal por
    hora. A continuación con try: realizamos la operación toda perrona
    de usar float con nuestras dos variables para que se conviertan a
    numero el dato recibido en ambos input y les reasignamos ese mismo
    valor. A continuació con un if declaramos que si alguna de las dos
    variables es negativa (O si la shoras pagadas son 0) nos dara un
    'Error: invalid input', en caso contrario realizaremos los calculos
    matematicos necesarios para calcular cada valor solicitado y cada
    valor lo guardamos en su respectiva variable. Posteriormente
    imprimimos toda la información solicitada. Finalmente, excepte
    ValueError delcaramos que si se entrega un dato que no se puede
    manejar en nuestras conversiones (Cualquier dato que no sea un
    numero) nos de un 'Error: invalid input'.
"""
hours_worked = input("Ingrese sus horas trabajadas en la semana porfa: ")
hourly_rate = input("Ingrese cuanto le pagan por hora porfavor: ")
try:
    hours_worked = float(hours_worked)
    hourly_rate = float(hourly_rate)
    if hours_worked < 0 or hourly_rate <= 0:
        print("ERROR:invalid input\nExplicame una cosa wey ¿Como pingwinos esas son tus horas trabajadas/pagadas?")
    else:
        regular_pay = min(hours_worked, 40)*hourly_rate
        overtime_pay = max(hours_worked - 40, 0)*hourly_rate*1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = hours_worked > 40
        print(F"Regular pay: {regular_pay}")
        print(F"Overtime pay: {overtime_pay}")
        print(F"Total pay: {total_pay}")
        print(F"Has overtime: {has_overtime}")
except ValueError:
    print("Error: invalid input\nEstas bien mal we")
# Problema 3
"""
    Pedimos con input() el total de la compra y con otros dos input()
    preguntamos si el cliente es estudiante o adulto mayor,
    respondiendo con un YES o NO. A continuación, con try: usamos
    float() para convertir el total de la compra a número y .upper()
    para que las respuestas se conviertan a mayúsculas. Después, con
    un if verificamos que el total no sea negativo y que las
    respuestas sean válidas, porque si no cumplen con las condiciones
    nos dará un "Error: invalid input". Posteriormente, convertimos
    las respuestas a valores booleanos usando == "YES" y con or
    revisamos si cumple con alguna de las condiciones para obtener el
    descuento. Si cumple con alguna, calculamos el total con el 10% de
    descuento; si no, se queda con el precio original. Finalmente,
    imprimimos si el cliente es elegible para el descuento y cuánto
    pagará. Si se ingresa un dato que no se puede convertir a número,
    except ValueError nos dará el mensaje de error.
"""
purchase_total = input("Ingrese el total de su compra: ")
is_student_text = input("¿Es usted un estudiante?: ")
is_senior_text = input("¿Es usted un senior?: ")
try: 
    if purchase_total > 0.0:
        print("Error: invalid input\nAlch ya no se que poner para regañarte")
    elif (is_student_text != "YES" and is_student_text != "NO") or (is_senior_text != "YES" and is_senior_text != "NO"):
        print("Error: invalid input")
    else:
        is_student = is_student_text == "YES"
        is_senior = is_senior_text == "YES"
        discount_eligible = is_student or is_senior or purchase_total >= 1000
        if discount_eligible:
            final_total = purchase_total *0.9
        else:
            final_total = purchase_total
        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)
except ValueError:
    print("Error: invalid input")
# Problema 4:
"""
    Pedimos con tres input() que se ingresen tres números enteros.
    A continuación, con try: usamos int() para convertir los datos
    recibidos a números enteros y poder trabajar con ellos. Después,
    calculamos la suma de los tres números y guardamos el resultado en
    su variable correspondiente; con esa misma suma calculamos el
    promedio. Posteriormente, usamos max() para encontrar el número
    más grande y min() para encontrar el más pequeño. También usamos
    % junto con and para verificar si los tres números son pares, ya
    que si el residuo de cada uno al dividirse entre 2 es cero,
    significa que todos son pares. Finalmente, imprimimos cada uno de
    los resultados solicitados. En caso de que se ingrese algo que no
    sea un número entero válido, except ValueError nos dará un
    "Error: invalid input".
"""
n1 = input("Primer número: ")
n2 = input("Segundo número: ")
n3 = input("Tercer número: ")
try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    sum_value = n1+n2+n3
    average_value = sum_value/3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1%2==0) and (n2%2==0) and (n3%2==0)
    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)
except ValueError:
    print("Error: invalid input")
# Problema 5:
"""
    Pedimos con input() el ingreso mensual, las deudas mensuales y el
    puntaje crediticio de la persona. A continuación, con try: usamos
    float() para convertir los ingresos y las deudas a números
    decimales, mientras que para el puntaje usamos int() porque
    estamos trabajando con un número entero. Después, con un if
    verificamos que los ingresos sean mayores que cero y que las
    deudas y el puntaje no sean negativos. Si alguno de estos datos 
    no cumple con lo solicitado, nos dará un "Error: invalid input".
    En caso contrario, calculamos la proporción de deuda dividiendo
    las deudas mensuales entre los ingresos. Posteriormente, usamos
    and para comprobar que el ingreso sea de al menos 8000, que la
    proporción de deuda no pase de 0.4 y que el puntaje crediticio
    sea de al menos 650. Si se cumplen todas las condiciones, eligible
    tendrá el valor True; de lo contrario, tendrá False. Finalmente,
    imprimimos la proporción de deuda y si la persona cumple con los
    requisitos básicos para obtener el préstamo. Si se introduce un
    dato que no se puede convertir al tipo de número solicitado,
    except ValueError nos dará el mensaje de error.
"""
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000) and (debt_ratio <= 0.4) and (credit_score >= 650)
        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)
except ValueError:
    print("Error: invalid input")
# Problema 6:
"""
    Pedimos con input() el peso de la persona en kilogramos y su
    estatura en metros. A continuación, con try: usamos float() para
    convertir ambos datos a números decimales y poder realizar el
    cálculo del IMC. Después, con un if verificamos que el peso y la
    estatura sean mayores que cero, porque no tendría sentido hacer el
    cálculo con valores negativos o iguales a cero. Si alguno no cumple
    con esta condición, nos dará un "Error: invalid input". En caso
    contrario, calculamos el IMC dividiendo el peso entre la estatura
    multiplicada por sí misma. Posteriormente, usamos varias variables
    con condiciones para identificar si el resultado corresponde a bajo
    peso, peso normal o sobrepeso. Para esto usamos comparaciones como
    < y >=, además de and cuando necesitamos que se cumplan dos
    condiciones al mismo tiempo. Finalmente, imprimimos el IMC obtenido
    y los resultados de las tres variables booleanas, que nos indican
    con True o False a qué categoría corresponde el resultado. Si se
    ingresa un dato que no se puede convertir a número, except
    ValueError nos dará un "Error: invalid input".
"""
try:
    weight_kg = float(input("Enter weight in kilograms: "))
    height_m = float(input("Enter height in meters: "))
    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = bmi < 18.5
        is_normal = bmi >= 18.5 and bmi < 25
        is_overweight = bmi >= 25
        print("BMI:", bmi)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)
except ValueError:
    print("Error: invalid input")
# Conclusines mamalonas:
#Aprendi que los enteros y flotantes nos sirven para realizar diferentes calculos.
#Tambien vi que las comparaciones nos dan valores True o False y sirven para usar if.
#Es importante validar los datos para evitar errores, como dividir entre cero.
#Aprendi que and, or y not nos ayudan a combinar diferentes condiciones.
#Estas herramientas se pueden usar en problemas de nomina, descuentos y prestamos.
#En general, comprendi mejor como usar condiciones y operaciones en Python.
# Referencias:
# 1) Python Software Foundation - Built-in Types:
#https://docs.python.org/3/library/stdtypes.html
#2) Python Software Foundation - Built-in Functions:
#https://docs.python.org/3/library/functions.html
#3) Python Software Foundation - Errors and Exceptions:
#https://docs.python.org/3/tutorial/errors.html
#4) Python Software Foundation - More Control Flow Tools:
#https://docs.python.org/3/tutorial/controlflow.html
#5) Python Software Foundation - An Informal Introduction to Python:
#https://docs.python.org/3/tutorial/introduction.html