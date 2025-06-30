from dotenv import load_dotenv
load_dotenv()

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Now import Agno and other dependencies
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.googlesearch import GoogleSearchTools
from agno.tools.dalle import DalleTools
from textwrap import dedent

#web agent
web_agent = Agent(
    name = "Web Agent",
    role = "Search the web to find the most updated and relevant information.",
    model = OpenAIChat(id="gpt-4o"),
    tools = [GoogleSearchTools()],
    instructions = ["Give the most updated and relevant information from the web"],
    show_tool_calls = True,
    markdown = True,
)

#writer agent
writer_agent = Agent(
    name = "Writer Agent",
    role = "Write a blog post on the provided topic",
    model = OpenAIChat(id="gpt-4o"),
   # tools = [GoogleSearchTools()],
    instructions = ["Use proper headings and formatting to write a blog post"],
    show_tool_calls = True,
    markdown = True,
)

#image agent
image_agent = Agent(
    name = "Image Agent",
    model = OpenAIChat(id="gpt-4o"),
    tools = [DalleTools()],
    description = dedent("""
    You are an image generation agent. You are given a topic and you need to generate an image based on the topic.
    You can use the DalleTools to generate the image.
    """),
    instructions = dedent("""
    As an AI image generation agent, follow these steps:
    1. Analyze the user's request carefully to understand the desired style and mood.
    2. Before generating, enhance the prompt with artistic details like lighting, perspective, and atmosphere
    3. Use the `create_image` tool with detailed, well-crafted prompts
    4.  Provide a brief explanation of the artistic choices made
    5. If the request is unclear, ask for clarification about style preferences

    Always aim to create visually striking and meaningful images that capture the user's vision!
    """),

    show_tool_calls = True,
    markdown = True,
)

#Blog formatted agent
blog_formatted_agent = Agent(
    name = "Blog Formatted Agent",
    model = OpenAIChat(id="gpt-4o"),
    role = "Format the blog with headings, paragraphs, and insert an image after the first paragraph.",
    instructions = dedent("""
    Format the given blog content using Markdown.
    - Break long paragraphs for readability.
    - Add an image markdown tag after the first paragraph like this:
      ![AI-generated image](IMAGE_URL)
    - Ensure headings are used for structure (## for main headings, ### for sub).
    - Wrap up with a neat conclusion.
    """),
    show_tool_calls = True,
    markdown = True,
)

