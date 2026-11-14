from flask import Flask, render_template_string, request
import boto3

app = Flask(__name__)

# AWS Bedrock Configuration
REGION = "us-east-1"
MODEL_ID = "amazon.nova-lite-v1:0"

# Bedrock Runtime Client
bedrock = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)

# Web Dashboard
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>AI DevOps Assistant</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            margin: 0;
            padding: 40px;
        }

        .container {
            max-width: 850px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        }

        h1 {
            color: #17365d;
        }

        textarea {
            width: 100%;
            height: 140px;
            padding: 12px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 15px;
        }

        button {
            background: #1769aa;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            margin-top: 15px;
            font-size: 15px;
        }

        button:hover {
            background: #104e80;
        }

        .result {
            background: #f3f6fa;
            padding: 20px;
            margin-top: 25px;
            white-space: pre-wrap;
            overflow-wrap: anywhere;
            border-radius: 8px;
            line-height: 1.6;
        }

        .footer {
            margin-top: 25px;
            color: #777;
            font-size: 13px;
            text-align: center;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>🚀 AI DevOps Assistant</h1>

    <p>Powered by AWS Bedrock - Amazon Nova Lite</p>

    <form method="POST">

        <textarea
            name="prompt"
            placeholder="Enter your DevOps issue here..."
            required
        ></textarea>

        <br>

        <button type="submit">Analyse Issue</button>

    </form>

    {% if answer %}
    <div class="result">
        <h3>🤖 AI Analysis</h3>
        {{ answer }}
    </div>
    {% endif %}

    {% if error %}
    <div class="result">
        <h3>❌ Error</h3>
        {{ error }}
    </div>
    {% endif %}

    <div class="footer">
        AI-Powered DevOps Troubleshooting Assistant
        <br>
        Python | Flask | AWS Bedrock | Nova Lite
    </div>

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    answer = None
    error = None

    if request.method == "POST":

        prompt = request.form.get("prompt", "").strip()

        if prompt:

            try:

                response = bedrock.converse(
                    modelId=MODEL_ID,

                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"text": prompt}
                            ]
                        }
                    ],

                    inferenceConfig={
                        "maxTokens": 700,
                        "temperature": 0.3
                    }
                )

                answer = response["output"]["message"]["content"][0]["text"]

            except Exception as e:

                app.logger.exception("Bedrock request failed")
                error = "Unable to analyse the issue. Check the application logs and AWS Bedrock permissions."

    return render_template_string(
        HTML,
        answer=answer,
        error=error
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
