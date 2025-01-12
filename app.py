from flask import *
from parse import function1
from prompt import airoast
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parsefunc', methods=['POST'])
def parsefunc():
    if request.method=='POST':
        if 'file' not in request.files:
            return render_template('final.html', text="No file selected.")
        f=request.files['file']
        if f.filename == '':  # Check if a file was selected
            return render_template('final.html', text="No file selected.")
        ftext=function1(f)
        fresponse=airoast(ftext)
        return render_template('final.html',text=fresponse)


if __name__=="__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)