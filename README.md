# AI-Blogs-Agent
**Multi-Agent AI System for Automated Blog Creation, Image Generation, and PDF Export**

AI Blog Agents is an intelligent, fully-automated content generation pipeline powered by multiple specialized agents. It autonomously searches the web, writes SEO-optimized blog posts, generates high-quality images, formats the blog in markdown, and exports it as a beautifully styled PDF. All in one go!

Built with 💡 [Agno](https://github.com/agno-ai/agno), OpenAI GPT-4o, DALL·E, and WeasyPrint.

# **✨ Features**

**1. Automated Content Generation:** Generates blog posts on any given topic using a team of specialized AI agents.

**2. Web Research:** Utilizes a "Web Agent" to gather up-to-date and relevant information from the internet.

**3. Dynamic Writing:** A "Writer Agent" crafts detailed and well-structured blog posts with proper headings.

**4. AI-Powered Image Generation:** An "Image Agent" creates unique, relevant images using DALL-E to enhance blog posts.

**5. Markdown Formatting:** A "Blog Formatted Agent" formats the blog post in Markdown, ensuring readability and proper image placement.

**6. PDF Export:** Automatically saves the final blog post as a beautifully styled PDF document.

**7. Transparent Execution:** Shows detailed terminal outputs of how each agent is called and what tools they use, providing full visibility into the AI's workflow.


# **🚀 How It Works**

The core of this project is a multi-agent system powered by the agno framework. A team of specialized AI agents collaborates to achieve the goal of generating a complete blog post.
Here's a breakdown of the workflow:

**- Web Agent:** Initiates the process by searching the [web](www.google.com) for the most current and relevant information on the given blog topic.

**- Writer Agent:** Takes the researched information and drafts a comprehensive blog post, ensuring a clear structure with headings. 

**- Image Agent:** Generates a visually appealing and contextually relevant image based on the blog post's topic.

**- Blog Formatted Agent:** Formats the entire blog post into Markdown, incorporating the generated image after the first paragraph and ensuring overall readability.

**- PDF Conversion:** Finally, the Markdown content is converted into a styled PDF document for easy sharing and archiving.

# **Step-by-step Agents Execution**

**1.** User topic will be passed to web_agent. Web_agent will do the internet search and collect the most recent information related to topic.

**2.** The collected information will be passed to next tool agent known as 'writer_agent', who will write the SEO-friendly blog.

![Screenshot from 2025-06-30 16-41-54](https://github.com/user-attachments/assets/8d8f9188-9965-462c-ae58-248723ea4eb9)

**3.** Image_agent will generate the AI image suitable for blog.

**4.** Blog_formatted_agent will convert the whole generated content (blog text and AI image) into the blog format.

![Screenshot from 2025-06-30 16-46-49](https://github.com/user-attachments/assets/7a878162-e0ce-4c21-939a-f2885e059b43)

**5.** The final Blog will be saved as PDF in the root directory of the project.

![Screenshot from 2025-06-30 16-58-35](https://github.com/user-attachments/assets/f8b49467-4bd8-46b7-9f6e-154a7d4e60de)

You can see step-by-step execution of agents workflow on your terminal upon successful execution of the code.


# **⚙️ Setup and Installation**

Follow these steps to get your AI Blog Agents project up and running:

**Prerequisites**
- Python 3.8+
- An OpenAI API Key

**Installation**
**1. Clone the repository:**
```bash
git clone https://github.com/AlishbaAhsan/AI-Blogs-Agent.git
cd AI-Blog-Agents
```

**2. Create the virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install the required dependencies:**
```bash
pip install -r requirnments.txt
```

**Configuration**

**1. Create the .env file:**
In the root directory of your project, create a file named '.env'

**2. Add your OpenAI API Key:**
Inside your .env, add your OpenAI API Key like this:
```bash
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```
Replace 'YOUR_OPENAI_API_KEY' with your actual API Key.

# **▶️ Usage**
To generate a blog post, simply run the BlogAgents.py file:
```bash
python BlogAgents.py
```

The script is currently configured to write a blog post on "updates of AI in 2025." You can easily change this topic within the BlogAgents.py file by modifying the agents_team.run() argument.

Upon successful execution, the script will:
- Display the terminal outputs showing how each agent is called and uses its tools, giving you a transparent view of the process.
- Generate a detailed blog post.
- Save the blog post as a PDF file (e.g., AI_blog_post.pdf) in your project directory.

# **📜 License**
This project is open-source and available under the MIT License.

# **🤝 Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

*You can also contact me at alishbaahsan127@gmail.com*




