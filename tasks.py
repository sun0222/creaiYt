from crewai import Task
from tools import youtube_channel_tool
from agents import blog_researcher, blog_writer

# first researsch task
research_task = (
    description=(
        "Identify the video topic {topic}."
        "Get the detailed information about video from the channel."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the topic {topic} of video content',
    tools=[youtube_channel_tool],
    agent=blog_researcher,
)


# second writing task
writing_task = (
    description=(
        "Get the information from the youtube channel on the topic{topic}."
    ),
    expected_output='Summarize the information from the youtube channel video on the topic{topic} and create the content from the blog.',
    tools=[youtube_channel_tool],
    agent=blog_writer,
    async_execution=False,
    output_files='new_blog_post.md'
)