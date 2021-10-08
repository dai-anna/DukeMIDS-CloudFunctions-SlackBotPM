# GCP Cloud Functions - Slack Bot Project Manager

## Brief Description
This is a slash command chatbot on Slack that is hosted entirely on the cloud. One serverless Cloud Function sends JSON payloads with HTTP trigger to a Firestore Database, which hosts all my chatbot messages. Another Cloud Function gets triggered via HTTP through the Slack API with their slash command trigger, pulls a random message from my database and returns it to Slack. 

## Architectural Diagram
![Chatbot_diagram](https://user-images.githubusercontent.com/89488845/135667923-c2076e7c-e6f1-4b2e-92cf-91fc3154a632.png)
