from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operacao = request.form['operacao']

        resultado = None
        erro = None

        if operacao == 'soma':
            resultado = num1 + num2
        elif operacao == 'subtracao':
            resultado = num1 - num2
        elif operacao == 'multiplicacao':
            resultado = num1 * num2
        elif operacao == 'divisao':
            if num2 != 0:
                resultado = num1 / num2
            else:
                erro = "Divisão por zero não é permitida!"

        return render_template('index.html', resultado=resultado, num1=num1, num2=num2, operacao=operacao, erro=erro)
    
    except ValueError:
        erro = "Por favor, digite números válidos!"
        return render_template('index.html', erro=erro)

if __name__ == '__main__':
    app.run(debug=True)