# save_blog_as_pdf.py

from markdown import markdown
from weasyprint import HTML
import os

def markdown_to_pdf(markdown_text, output_path="output.pdf"):
    """
    Converts Markdown content to a beautifully styled PDF using WeasyPrint.
    """
    # Convert Markdown to HTML
    html = markdown(markdown_text)

    # Optional: Add minimal styling to make PDF look cleaner
    styled_html = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }}
                h1, h2, h3 {{
                    color: #2C3E50;
                }}
                img {{
                    max-width: 100%;
                    height: auto;
                    margin: 20px 0;
                }}
                code {{
                    background-color: #f4f4f4;
                    padding: 2px 4px;
                    border-radius: 4px;
                }}
                pre {{
                    background-color: #f4f4f4;
                    padding: 10px;
                    overflow-x: auto;
                    border-radius: 6px;
                }}
            </style>
        </head>
        <body>
            {html}
        </body>
    </html>
    """

    # Create the PDF
    HTML(string=styled_html).write_pdf(output_path)
    print(f"✅ Blog saved as: {os.path.abspath(output_path)}")
