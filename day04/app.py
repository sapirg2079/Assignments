import os
from flask import Flask, render_template, request
from growth_anlysis import analyze_and_plot

app = Flask(__name__)

# folders for uploaded files and static files
UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    rate = None
    max_yield = None
    graph_url = None
    error = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            error = 'No file part in the request.'
            return render_template('index.html', error=error)
            
        file = request.files['file']
        
        if file.filename == '':
            error = 'No file selected.'
            return render_template('index.html', error=error)
            
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # path for the output graph image
            graph_path = os.path.join(STATIC_FOLDER, 'growth_curve.png')
            
            try:
                # analyze the CSV file and generate the growth curve plot
                rate, max_yield = analyze_and_plot(filepath, graph_path)
                # נתיב יחסי להצגה ב-HTML
                graph_url = '/static/growth_curve.png'
            except Exception as e:
                error = f"Error processing file: {e}"
        else:
            error = 'Please upload a valid .csv file.'
            
    return render_template('index.html', rate=rate, max_yield=max_yield, graph_url=graph_url, error=error)

if __name__ == '__main__':
    app.run(debug=True)