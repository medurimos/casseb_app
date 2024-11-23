from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Função para calcular as raízes da equação quadrática
def calcular_raizes(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"As raízes reais são: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x1 = -b / (2 * a)
        return f"A raiz real é: x = {x1}"
    else:
        parte_real = -b / (2 * a)
        parte_imag = math.sqrt(-delta) / (2 * a)
        return f"As raízes complexas são: x1 = {parte_real} + {parte_imag}i, x2 = {parte_real} - {parte_imag}i"

# Rota principal que exibe o formulário e calcula as raízes
@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            # Pega os valores dos campos a, b, c
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])
            resultado = calcular_raizes(a, b, c)
        except ValueError:
            resultado = "Por favor, insira valores numéricos válidos."
    
    # Renderiza o template passando o resultado
    return render_template('pagina.html', resultado=resultado)

# Inicializa o servidor
if __name__ == '__main__':
    app.run(debug=True)
