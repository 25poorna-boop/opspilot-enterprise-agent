from flask import Flask, request, jsonify
from agent.enterprise_agent import EnterpriseAgent

app = Flask(__name__)
agent = EnterpriseAgent()

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/task", methods=["POST"])
def task():
    data = request.get_json(force=True)
    task = data.get("task", "")
    if not task:
        return jsonify({"error": "task is required"}), 400

    result = agent.execute_task(task)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
