from flask import Flask, jsonify
import subprocess
import os

app = Flask(__name__)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@app.route("/run-pipeline", methods=["POST"])
def run_pipeline():
    try:
        # Run the pipeline script
        result = subprocess.run(
            ["python", "scripts/run_pipeline.py"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True
        )

        return jsonify({
            "status": "success",
            "stdout": result.stdout,
            "stderr": result.stderr
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.route("/")
def health():
    return jsonify({
        "status": "api_runner_alive"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)