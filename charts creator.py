def generate_chart_code_from_eval(function_name, interval_start, interval_end, step=1):
    """
    Génère le code pour une courbe représentant une fonction donnée sur un intervalle donné.
    
    Args:
        function_name (str): Le nom de la fonction (sera utilisé comme titre du graphique).
        interval_start (int): La valeur de départ de l'intervalle pour x.
        interval_end (int): La valeur de fin de l'intervalle pour x.
        step (int, optional): L'incrément pour générer les valeurs de x. Par défaut, 1.

    Returns:
        str: Le code pour la courbe au format YAML.
    """
    x_values = list(range(interval_start, interval_end + 1, step))
    y_values = [eval(function_name.replace("x", str(x))) for x in x_values]
    chart_code = f"""```chart
type: line
labels: {x_values}
series:
  - title: {function_name}
    data: {y_values}
```
"""
    return chart_code

s = str(input("Use eval function or manually created function? yes or no: ")).lower()
if s == "yes" or s == "y":
    function_name = str(input("Enter function name (x**2, x, ...): "))
    interval_start = int(input("Enter interval start: "))
    interval_end = int(input("Enter interval end: "))
    step = int(input("Step"))
    print(generate_chart_code_from_eval(function_name, interval_start, interval_end, step))

else:
    pass



