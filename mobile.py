from flask import *
import numpy as np
import pickle

model = pickle.load(open("D:\IT-VEDANT\project\Bob Mobile House\H_SVC_model.pkl","rb"))



app = Flask(__name__)
app.secret_key = "Welcome222?"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict",methods=["GET","POST"])
def predict():
    if request.method == "POST":
        battery_power    =   float( request.form.get("battery_power") )
        blue             =   float( request.form.get("blue") )
        clock_speed      =   float( request.form.get("clock_speed") )
        dual_sim         =   float( request.form.get("dual_sim") )
        fc               =   float( request.form.get("fc") )
        four_g           =   float( request.form.get("four_g") )
        int_memory       =   float( request.form.get("int_memory") )
        m_dep            =   float( request.form.get("m_dep") )
        mobile_wt        =   float( request.form.get("mobile_wt") )
        n_cores          =   float( request.form.get("n_cores") )
        pc               =   float( request.form.get("pc") )
        px_height        =   float( request.form.get("px_height") )
        px_width         =   float( request.form.get("px_width") )
        ram              =   float( request.form.get("ram") )
        sc_h             =   float( request.form.get("sc_h") )
        sc_w             =   float( request.form.get("sc_w") )
        talk_time        =   float( request.form.get("talk_time") )
        three_g          =   float( request.form.get("three_g") )
        touch_screen     =   float( request.form.get("touch_screen") )
        wifi             =   float( request.form.get("wifi") )

        def predict_range(value):
            if value == 0:
                return ("Low")

            elif value == 1:
                return ('Medium')

            elif value == 2:
                return ('High')

            else:
                return ('Very High')


        new_data = [battery_power,blue,clock_speed,dual_sim,fc,four_g,int_memory,m_dep,mobile_wt,n_cores,pc,px_height,px_width,ram,sc_h,sc_w,talk_time,three_g,touch_screen,wifi]
        # print((new_data))

        new_data = np.array([new_data])
        predicted_value = model.predict(new_data)

        answer = predict_range(predicted_value)

        return render_template("index.html",pred_ans = answer)




if (__name__ == "__main__"):
    app.run(debug=True)