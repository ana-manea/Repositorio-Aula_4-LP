from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def index():
  return render_template('calculator.html')

@app.route('/calcular', methods=['POST'])
def calcular():
  num1 = float(request.form['num1'])
  num2 = float(request.form['num2'])
  operacao = request.form['operacao']

  resultado = None

  if operacao == 'soma':
      resultado = num1 + num2
  elif operacao == 'subtracao':
      resultado = num1 - num2
  elif operacao == 'multiplicacao':
      resultado = num1 * num2
  elif operacao == 'divisao':
      if num2 != 0:
          resultado = num1 / num2

  return render_template('calculator.html', resultado=resultado, num1=num1, num2=num2, operacao=operacao)

if _name_ == '_main_':
  app.run()