from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template('index.html',target_cgpa=None)

@app.route('/calculate1', methods=['POST'])
def calculate1():
    try:
        num1 = float(request.form['crt-cgpa'])
        num2 = float(request.form['tgt-cgpa'])
        cr_credit=int (request.form['crt-crd'])
        sm_credit=int (request.form['sm-crd'])
        
        expt_cgpa1=float(((sm_credit+cr_credit)*num2-(cr_credit*num1))/sm_credit)
        expt_cgpa=round(expt_cgpa1,2)
         
        
        return render_template('index.html', target_cgpa=expt_cgpa)

    except Exception as e:
              return f"Error: {str(e)}"


@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    try:
        num_semesters = int(request.form['num_semesters'])
        sgpa_list = []
        credit_list = []
        sum_credit=[]

        for i in range(1, num_semesters + 1):
            sgpa_key = f'sgpa_semester_{i}'
            credit_key = f'credit_semester_{i}'
            sgpa = float(request.form[sgpa_key])
            credit = int(request.form[credit_key])
            sgpa_list.append(sgpa)
            credit_list.append(credit)
            sum_credit_key=sgpa_list[i-1]*credit_list[i-1]
            sum_credit.append(sum_credit_key)

        total_sum = sum(sum_credit)
      
        
        nxt_sgpa= float(request.form['tgt-cgpa1'])
        nxt_credit = int(request.form['sm-crd1'])

        total_credit=sum(credit_list)+nxt_credit
        expected_0cgpa=float(((nxt_sgpa*total_credit)-total_sum)/nxt_credit)
        expected_cgpa=round(expected_0cgpa,3)
        # expected_cgpa=total_sum

        return render_template('index.html',expt_sgpa=expected_cgpa)

    except Exception as e:
    
        return f"Error: {str(e)}"
    
if __name__ == '__main__':
    app.run(debug=True)