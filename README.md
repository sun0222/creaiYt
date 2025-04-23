# CrewAI YouTube to Blog Post Generator

## 🧠 Overview

This project utilizes **CrewAI** to automate the creation of blog posts from **YouTube video content** focused on **Artificial Intelligence (AI)**, **Machine Learning (ML)**, and **Data Science (DS)**. It extracts transcripts or summaries from specified videos, transforms the content into a structured blog post, and optionally publishes it to a blog platform.

---

## 🚀 Features

- **🎥 YouTube Content Extraction:** Automatically extracts transcripts or key information from YouTube videos.
- **📝 AI-Powered Content Generation:** Uses LLMs via CrewAI agents to create engaging, well-structured blog posts.
- **🤖 Automated Workflow:** Sequential agents manage extraction, writing, editing, and optional publishing.
- **📚 Tailored for AI/ML/DS Content:** Special prompts and configurations fine-tuned for technical topics.

---

## ⚙️ How It Works

The process uses a multi-agent CrewAI workflow:

```mermaid
graph LR
    A[YouTube Video URL] --> B(YouTube Content Researcher Agent);
    B -- Extracted Content --> C(Blog Post Writer Agent);
    C -- Draft Blog Post --> D(Technical Editor Agent);
    D -- Final Blog Post --> E{Optional Publisher Agent};
    E -- Published --> F[Blog Platform];
    D -- Final Blog Post --> G[Final Blog Post Output (e.g., file/console)];
    E -- Not Used --> G;
👥 Agent Roles
YouTube Content Researcher Agent:
Extracts transcript or relevant summaries from a YouTube URL using tools or APIs.

Blog Post Writer Agent:
Writes a first draft of the blog post based on the extracted content.

Technical Editor Agent:
Edits and reviews the draft for clarity, technical accuracy, and formatting.

(Optional) Publisher Agent:
Publishes the final blog post to platforms like WordPress, Medium, or dev.to via API.

🛠️ Installation
bash
Copy
Edit
git clone <your-repository-url>
cd <your-repository-name>

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
Dependencies to include in requirements.txt:

crewai

youtube-transcript-api

requests

Others as needed

🔐 Configuration
Create a .env file at the root level with your API keys and config values:

env
Copy
Edit
# LLM Configuration
OPENAI_API_KEY="your_openai_api_key"
# OPENAI_MODEL_NAME="gpt-4"

# (Optional) YouTube API Key
# YOUTUBE_API_KEY="your_youtube_api_key"

# (Optional) Blog Platform API
# BLOG_API_ENDPOINT="your_blog_api_endpoint"
# BLOG_API_KEY="your_blog_api_key"
# BLOG_USERNAME="your_blog_username"
# BLOG_PASSWORD="your_blog_password"
⚠️ Note: Add .env to your .gitignore file to prevent accidental commits.

🧩 Customization
Modify the agent backstories, prompts, and task descriptions in your main script (main.py) to align the tone and content with your needs.

▶️ Usage
Set up your .env file with the required keys.

Add one or more YouTube video URLs to main.py.

Run the pipeline:

bash
Copy
Edit
python main.py
Output will be shown in the console or saved to a file.

If Publisher Agent is enabled, the blog post will be automatically published.

🤝 Contributing
We welcome contributions!
Feel free to:

Submit pull requests

Open issues

Improve features or documentation

📜 License
Specify your license here (e.g., MIT, Apache 2.0).

🙌 Acknowledgments
Powered by CrewAI ⚙️
Inspired by the goal to simplify AI/ML/DS content sharing.

🧑‍💻 Author
Sunil Kumar