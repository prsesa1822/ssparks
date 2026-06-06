# AI and Data Analysis Portfolio

Dark, tech-forward static portfolio site for Sarah Sparks. The live site is designed for GitHub Pages and includes:

- A self-contained portfolio homepage
- A web-formatted resume page extracted from the supplied resume PDF
- A web-formatted presentation page extracted from the supplied presentation PDF
- An AI and data analysis snapshot section
- A generator script for rebuilding the HTML pages from local PDFs

## Hosted Files

- `index.html` is the portfolio homepage
- `resume.html` is the web-formatted resume
- `presentation.html` is the web-formatted portfolio presentation
- `generate_pdf_pages.py` extracts local PDFs into static HTML pages
- `requirements.txt` lists Python dependencies

## Local Asset Notes

The original PDFs and generated image/PDF report are kept locally in the working folder. They can be added later with Git or another binary upload route:

- `assets/sarah_sparks_resume.pdf`
- `assets/Presentation_Compressed.pdf`
- `Ai and data analysis.pdf`
- `Ai and data analysis images/`

## GitHub Pages

Enable GitHub Pages from the repository settings and publish from the `main` branch root. The homepage is `index.html`.

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Regenerate the web resume and presentation pages after updating the local PDFs:

```bash
python generate_pdf_pages.py
```
