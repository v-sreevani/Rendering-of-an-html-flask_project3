from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/first')
def first():
    return render_template('first.html')

@FAI.route('/data_rendered')
def data_rendered():
    return render_template('data_rendered.html',name='sree',age=21)

if __name__=='__main__':
    FAI.run(debug=True)