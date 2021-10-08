# GCP Cloud Functions - Slack Bot Project Manager

## Brief Description
This is a slash command chatbot on Slack that is hosted entirely on the cloud. One serverless Cloud Function sends JSON payloads with HTTP trigger to a Firestore Database, which hosts all my chatbot messages. Another Cloud Function gets triggered via HTTP through the Slack API with their slash command trigger, pulls a random message from my database and returns it to Slack. 

I added an additional function where we can write to the database using a CLI tool: PMBot.py instead of cURLing or directly using my Google Cloud Function trigger. In the same CLI tool, I also have an option to pull a random message from my database similar to Slack.

**SlackBot Demo**
![Screen Shot 2021-10-08 at 4 26 21 PM](https://user-images.githubusercontent.com/89488845/136621935-6014a92f-fade-4049-81ac-f10561900964.png)

**CLI Tool Demo**
![Screen Shot 2021-10-08 at 4 34 28 PM](https://user-images.githubusercontent.com/89488845/136621910-b7998f95-c59a-4b35-9871-f6602707f560.png)

## Architectural Diagram

![output-onlinepngtools](https://user-images.githubusercontent.com/89488845/136622194-32c66ad4-8899-41b9-bb45-d72692aff21b.png)
