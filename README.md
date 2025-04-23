# CrewAI YouTube to Blog Post Generator

## Overview

This project utilizes CrewAI to automate the process of creating blog posts from YouTube video content focused on Artificial Intelligence (AI), Machine Learning (ML), and Data Science (DS). It extracts information from specified YouTube videos, synthesizes it into a coherent blog post format, and potentially posts it to a designated platform.

## Features

* **YouTube Content Extraction:** Identifies and extracts key information, transcripts, or summaries from YouTube videos.
* **AI-Powered Content Generation:** Uses LLMs via CrewAI agents to transform extracted video content into well-structured and engaging blog posts.
* **Automated Workflow:** Leverages a CrewAI crew to manage the tasks of extraction, writing, editing, and potentially publishing.
* **Focus on AI/ML/DS:** Tailored prompts and agents designed for technical content in the AI/ML/DS domain.

## How It Works

This project employs a CrewAI setup involving multiple agents and tasks, following this general workflow:

```mermaid
graph LR
    A[YouTube Video URL] --> B(YouTube Content Researcher Agent);
    B -- Extracted Content --> C(Blog Post Writer Agent);
    C -- Draft Blog Post --> D(Technical Editor Agent);
    D -- Final Blog Post --> E{Optional Publisher Agent};
    E -- Published --> F[Blog Platform];
    D -- Final Blog Post --> G[Final Blog Post Output (e.g., file/console)];
    E -- Not Used --> G;


YouTube Content Researcher Agent:
Task: Given a YouTube video URL (A), extract the transcript or relevant summary information. (This might involve external tools or APIs).
Blog Post Writer Agent:
Task: Take the extracted content (B) and write a draft blog post, focusing on clarity, structure, and engagement suitable for an AI/ML/DS audience.
Technical Editor Agent:
Task: Review the draft blog post (C) for technical accuracy, coherence, and proper terminology. Refine the content for quality.
(Optional) Publisher Agent:
Task: Take the final edited blog post (D) and publish it to a specified platform (F) (e.g., WordPress, Medium, dev.to) via its API. If not used, the final post is output directly (G).
These agents collaborate within a Crew to execute the workflow sequentially, passing the content from one stage to the next.
Installation
Clone the repository:
git clone <your-repository-url>
cd <your-repository-name>


Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install dependencies:
pip install -r requirements.txt

(Ensure your requirements.txt file lists crewai and any other necessary libraries like youtube-transcript-api, requests, etc.)
Configuration
Environment Variables: Create a .env file in the root directory and add the necessary API keys and configurations:
# LLM Configuration (e.g., OpenAI)
OPENAI_API_KEY="your_openai_api_key"
# OPENAI_MODEL_NAME="gpt-4" # Or your preferred model

# (Optional) YouTube API Key (if needed for your extraction method)
# YOUTUBE_API_KEY="your_youtube_api_key"

# (Optional) Blog Platform API Keys/Tokens (if using a Publisher Agent)
# BLOG_API_ENDPOINT="your_blog_api_endpoint"
# BLOG_API_KEY="your_blog_api_key"
# BLOG_USERNAME="your_blog_username"
# BLOG_PASSWORD="your_blog_password" # Or API Token


Important: Add .env to your .gitignore file to avoid committing sensitive keys.
Agent/Task Configuration: You might need to adjust agent backstories, goals, and task descriptions within the main Python script (main.py or similar) to fine-tune the output.
Usage
Ensure your environment variables are set (either in .env or exported in your shell).
Modify the main script (main.py or your entry point) to include the YouTube video URL(s) you want to process.
Run the script:
python main.py


The script will execute the CrewAI workflow, and the final blog post content will typically be printed to the console or saved to a file, depending on your implementation. If the Publisher Agent is configured, it will attempt to post the blog.
Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to improve the project.
(Optional: Add more specific contribution guidelines if needed)
License
*(Optional: Specify the license for your project, e.g., MIT, Apache
