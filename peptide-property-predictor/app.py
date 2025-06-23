from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# 预先加载模型
model_ALP = joblib.load("models/trained_ALP_model.pkl")
model_AMP = joblib.load("models/trained_AMP_model.pkl")
model_LW = joblib.load("models/trained_lw_model.pkl")
model_cellrate = joblib.load("models/trained_model.pkl")

# 主页面
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # 获取表单输入
        amp = float(request.form['AMP'])
        qk = float(request.form['QK'])
        yigsr = float(request.form['YIGSR'])
        bmp2 = float(request.form['BMP2'])

        X = pd.DataFrame([[amp, qk, yigsr, bmp2]], 
                         columns=["AMP", "QK", "YIGSR", "BMP2"])

        # 分别预测
        pred_ALP = model_ALP.predict(X)[0]
        pred_AMP = model_AMP.predict(X)[0]
        pred_LW = model_LW.predict(X)[0]
        pred_cellrate = model_cellrate.predict(X)[0]

        return render_template("index.html", 
                               pred_ALP=pred_ALP,
                               pred_AMP=pred_AMP,
                               pred_LW=pred_LW,
                               pred_cellrate=pred_cellrate)

    return render_template("index.html")

# 查看CSV文件
@app.route("/view_csv")
def view_csv():
    df = pd.read_csv("data/4pep_12000.csv")
    df.index = df.index + 1
    return df.to_html()

if __name__ == "__main__":
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
