import markdown

with open("plain.md", 'r') as f:
    markdown_text = f.read()

html = markdown.markdown(markdown_text, extensions=['toc', 'fenced_code'])

with open("plain.html", 'w') as f:
    f.write(html)