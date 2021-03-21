from flask import Flask, render_template, flash, request
app = Flask('app')

@app.route('/',methods=['POST','GET'])
def hello_world():
        if request.method == 'POST' and 'equation' in request.form:
                equation = request.form['equation']
                equation = equation.replace(' ', '')
                print(equation)
                if '×' in equation:
                        equation = equation.replace('×', '*')
                        print(equation)


                if '^' in equation:
                        equation = equation.replace('^', '**')
                        print(equation)

                if '÷' in equation:
                        equation = equation.replace('÷', '/')
                        print(equation)

                try:
                        result = eval(equation)
                        print(result)
                        return 'The answer is '+str(result)
                except Exception as e:
                        print(e)
                        return "<p id = 'demo'>wrong</p>" + open('templates/index.html').read()
                

        
        else:
                return 'Parameters missing'

  

app.run(host='0.0.0.0', port=8080)