from html import escape
from pathlib import Path

from pypdf import PdfReader


def extract_pages(path):
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        pages.append(clean_text("\n".join(lines)))
    return pages


def clean_text(text):
    replacements = {
        chr(0x25CF): "-",
        chr(0x2022): "-",
        chr(0x2013): "-",
        chr(0x2014): "-",
        chr(0x2192): "->",
        chr(0x2018): "'",
        chr(0x2019): "'",
        chr(0x201C): '"',
        chr(0x201D): '"',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def render_page(title, kicker, pages):
    sections = "\n".join(
        f"""      <section class="doc-page">
        <div class="page-tag">Page {index}</div>
        <pre>{escape(text)}</pre>
      </section>"""
        for index, text in enumerate(pages, 1)
    )

    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{escape(title)} | Sarah Sparks</title>
    <style>
      :root {{
        --ink: #f4f7fb;
        --muted: #9fb2c8;
        --paper: #070b12;
        --panel: #0d1420;
        --line: #22344d;
        --cyan: #23d7ff;
        --green: #6affb5;
        --violet: #9b7cff;
      }}

      * {{
        box-sizing: border-box;
      }}

      body {{
        margin: 0;
        font-family:
          Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont,
          "Segoe UI", sans-serif;
        color: var(--ink);
        background: var(--paper);
        background-image:
          linear-gradient(rgba(35, 215, 255, 0.06) 1px, transparent 1px),
          linear-gradient(90deg, rgba(35, 215, 255, 0.05) 1px, transparent 1px),
          radial-gradient(circle at 15% 10%, rgba(35, 215, 255, 0.16), transparent 32%),
          radial-gradient(circle at 85% 0%, rgba(155, 124, 255, 0.14), transparent 34%);
        background-size: 42px 42px, 42px 42px, auto, auto;
      }}

      header,
      main,
      footer {{
        width: min(980px, calc(100% - 36px));
        margin: 0 auto;
      }}

      header {{
        padding: 24px 0 18px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 16px;
        flex-wrap: wrap;
      }}

      a {{
        color: inherit;
      }}

      .nav {{
        display: flex;
        gap: 12px;
        flex-wrap: wrap;
      }}

      .button {{
        min-height: 42px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border: 1px solid var(--line);
        border-radius: 8px;
        padding: 0 14px;
        text-decoration: none;
        font-weight: 700;
        background: rgba(13, 20, 32, 0.84);
      }}

      .hero {{
        padding: 34px 0 24px;
      }}

      .kicker {{
        color: var(--green);
        font-weight: 800;
        text-transform: uppercase;
        font-size: 0.82rem;
        letter-spacing: 0.08em;
      }}

      h1 {{
        margin: 10px 0 12px;
        font-size: clamp(2.1rem, 7vw, 4.8rem);
        line-height: 0.96;
        letter-spacing: 0;
        text-shadow: 0 0 34px rgba(35, 215, 255, 0.28);
      }}

      .lede {{
        max-width: 68ch;
        color: var(--muted);
        line-height: 1.6;
        font-size: 1.05rem;
      }}

      .doc-page {{
        margin: 18px 0;
        border: 1px solid var(--line);
        border-top: 5px solid var(--cyan);
        border-radius: 8px;
        background: rgba(13, 20, 32, 0.94);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.32);
      }}

      .page-tag {{
        padding: 14px 18px;
        color: var(--green);
        font-weight: 800;
        border-bottom: 1px solid var(--line);
      }}

      pre {{
        margin: 0;
        padding: 18px;
        white-space: pre-wrap;
        font: 500 0.98rem/1.55 Inter, ui-sans-serif, system-ui, sans-serif;
        color: var(--ink);
      }}

      footer {{
        padding: 24px 0 34px;
        color: var(--muted);
      }}

      @media (max-width: 560px) {{
        header {{
          align-items: flex-start;
        }}

        .nav,
        .button {{
          width: 100%;
        }}

        .nav {{
          display: grid;
        }}
      }}
    </style>
  </head>
  <body>
    <header>
      <strong>Sarah Sparks</strong>
      <nav class="nav" aria-label="Portfolio navigation">
        <a class="button" href="index.html">Home</a>
        <a class="button" href="resume.html">Resume</a>
        <a class="button" href="presentation.html">Presentation</a>
      </nav>
    </header>
    <main>
      <section class="hero">
        <div class="kicker">{escape(kicker)}</div>
        <h1>{escape(title)}</h1>
        <p class="lede">Extracted from the supplied PDF and formatted as a GitHub Pages-friendly web page for quick review.</p>
      </section>
{sections}
    </main>
    <footer>Sarah Sparks portfolio materials.</footer>
  </body>
</html>
"""


Path("resume.html").write_text(
    render_page(
        "Resume",
        "Operations, CRM & Data Support",
        extract_pages("assets/sarah_sparks_resume.pdf"),
    ),
    encoding="utf-8",
)

Path("presentation.html").write_text(
    render_page(
        "AI and Data Analysis Presentation",
        "Portfolio case study",
        extract_pages("assets/Presentation_Compressed.pdf"),
    ),
    encoding="utf-8",
)

print("created resume.html and presentation.html")
