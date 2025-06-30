from dotenv import load_dotenv
load_dotenv()

import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Now import Agno and other dependencies
from agno.agent import Agent
from AgentsTeam import web_agent, writer_agent, image_agent, blog_formatted_agent
from save_blogs_as_PDF import markdown_to_pdf

#combining all agents into the team

agents_team = Agent(
    team = [web_agent, writer_agent, image_agent, blog_formatted_agent],
    instructions = [
        "1. Search and gather updated information about the topic.",
        "2. Write a detailed blog post using headings and structure.",
        "3. Generate an image relevant to the topic.",
        "4. Format the blog post with markdown and insert the image after the first paragraph.",
    ],
    show_tool_calls = True,
    markdown = True,
)
agents_team.print_response("Write a blog post on the updates of AI in 2025", stream=True)

# Run full agent flow and extract final blog text
final_output = agents_team.run("Write a blog post on the updates of AI in 2025")
final_blog = "".join([
    e.content for e in final_output
    if hasattr(e, "content") and isinstance(e.content, str)
])

# Save as PDF
markdown_to_pdf(final_blog, output_path="AI_blog_post.pdf")
print("✅ Blog saved as PDF")

