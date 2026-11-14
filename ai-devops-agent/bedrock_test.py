import boto3
import json

# AWS Configuration
REGION = "us-east-1"
MODEL_ID = "amazon.nova-lite-v1:0"

# Create Bedrock Runtime Client
bedrock = boto3.client(
    "bedrock-runtime",
    region_name=REGION
)

def test_bedrock_connection():

    prompt = """
    You are an experienced AWS DevOps Engineer.

    A Kubernetes pod is showing CrashLoopBackOff.

    Explain:
    1. What does CrashLoopBackOff mean?
    2. What are the possible root causes?
    3. Which Kubernetes commands should we execute?
    4. How can we troubleshoot this issue?
    5. What are the production best practices?
    """

    try:

        print("\nConnecting to Amazon Bedrock...")

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
                "maxTokens": 500,
                "temperature": 0.3
            }
        )

        answer = response["output"]["message"]["content"][0]["text"]

        print("\n========== AI DEVOPS ASSISTANT ==========\n")
        print(answer)

        print("\n========== TOKEN USAGE ==========")
        print(json.dumps(response["usage"], indent=4))

        print("\nBedrock connection successful!")

    except Exception as error:

        print("\nBedrock connection failed!")
        print(f"Error: {error}")


if __name__ == "__main__":
    test_bedrock_connection()
