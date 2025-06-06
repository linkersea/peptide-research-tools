from flask import Flask, render_template, request, make_response
import numpy as np
from sympy import symbols, Eq, solve

app = Flask(__name__)

def calculate_Ts(target_concentrations):
    T1_sym, T2_sym, T3_sym, T4_sym = symbols('T1 T2 T3 T4')
    AMP, QK, YIGSR, BMP2 = target_concentrations

    eq1 = Eq(0.169194168038461 + 0.00890840600089286*T1_sym, AMP)
    eq2 = Eq(0.045379380426254556 + 0.3059683593827991*AMP
             - 0.0014394385070825994*T2_sym
             + 0.00041450856183020135*AMP*T2_sym
             + 0.0046035913943081866*QK*T2_sym, QK)
    eq3 = Eq(0.8533508138114714 - 1.440680274486564*AMP + 0.9407165451509325*QK
             + 0.0052081916764346245*T3_sym
             - 0.0037821281281384816*QK*T3_sym
             + 0.009563042084960914*AMP*T3_sym, YIGSR)
    eq4 = Eq(0.6350487053064278 - 0.9329381966783075*AMP - 0.1048023087962946*QK
             + 0.35352703935596885*YIGSR
             + 0.004445607474410709*T4_sym
             + 0.005226982581547315*AMP*T4_sym
             - 0.0006238265544812882*QK*T4_sym
             - 0.002116348223286234*YIGSR*T4_sym, BMP2)

    solutions = solve([eq1, eq2, eq3, eq4], [T1_sym, T2_sym, T3_sym, T4_sym], dict=True)
    if solutions:
        sol = solutions[0]
        return sol[T1_sym], sol[T2_sym], sol[T3_sym], sol[T4_sym]
    else:
        raise ValueError("Step-by-step solution failed")

@app.after_request
def add_header(response):
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            input_amp = float(request.form['amp'])
            input_qk = float(request.form['qk'])
            input_yigsr = float(request.form['yigsr'])
            input_bmp2 = float(request.form['bmp2'])
            target_concentrations = [input_amp, input_qk, input_yigsr, input_bmp2]
            T1, T2, T3, T4 = calculate_Ts(target_concentrations)
            return render_template('index.html', T1=T1, T2=T2, T3=T3, T4=T4)
        except Exception as e:
            return f"Error occurred: {e}"
    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)