from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML = """
<html>
    <body>
        <h1>Enterprise Agent Dashboard</h1>
        <form method="post">
            <textarea name="task" rows="5" cols="60" placeholder="Enter your task"></textarea><br>
            <button type="submit">Send</button>
        </form>
        {% if result %}
        <pre>{{ result }}</pre>
        {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        task = request.form.get("task")
        try:
            res = requests.post("http://localhost:8000/task", json={"task": task})
            result = res.json()
        except:
            result = "API not running"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(port=8500, debug=True)
