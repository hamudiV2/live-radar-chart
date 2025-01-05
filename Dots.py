from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input values from the form
        scores = [
            float(request.form.get('chem', 0)),
            float(request.form.get('bio', 0)),
            float(request.form.get('phy', 0)),
            float(request.form.get('eng', 0)),
            float(request.form.form.get('math', 0))
        ]

        # Generate the radar chart
        categories = ['Chemistry', 'Biology', 'Physics', 'English', 'Maths']
        num_vars = len(categories)
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angles += angles[:1]
        scores += scores[:1]

        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True), facecolor='#0E1117')
        ax.set_facecolor('#0E1117')
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        plt.xticks(angles[:-1], categories, color='white', size=12)
        plt.yticks([20, 40, 60, 80, 100], ["20%", "40%", "60%", "80%", "100%"], color="white", size=10)
        plt.ylim(0, 100)
        ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)
        ax.plot(angles, scores, linewidth=2, linestyle='solid', color='#1F77B4', label='Scores')
        ax.fill(angles, scores, color='#1F77B4', alpha=0.25)

        # Save the plot to a BytesIO object
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight', pad_inches=0)
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode('utf8')
        plt.close()

        return render_template('index.html', plot_url=plot_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)