from crewai import Agent
from tools import youtube_channel_tool

# create blog content writer researcher agent
blog_researcher = Agent(
    role = 'Blog researcher from youtube videos',
    goal = 'get the relevent video content from the video for the topic{topic}',
    verbose = True,
    memory = True,
    backstory=(
        "Expert in understanding videos in AI data science, machine learing and generative ai and providng suggestion"
    ),
    tool = [youtube_channel_tool],
    allow_delegation = True  # I'll be transfering after whatever work that i do or this agent does to someone else.
)


# create a blog writer agent with youtube tools
blog_writer = Agent(
    role = 'Blog Writer',
    goal = 'Narrate compelling tech stories about the video topic {topic} from Youtube channel',
    verbose = True,
    memory = True,
    backstory =(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tool = [youtube_channel_tool],
    allow_delegation = False)