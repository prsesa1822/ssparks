# AI and Data Analysis Portfolio

This project generates a compact visual portfolio about AI and data analysis work. It includes:

- A static portfolio homepage for GitHub Pages
- Sarah Sparks' resume content as a web page
- The portfolio presentation content as a web page
- Local PDF copies of the resume and presentation
- A PDF report built with ReportLab
- A set of presentation-style PNG images built with Pillow
- Source data and chart logic embedded in the Python scripts

## Files

- `index.html` is the portfolio homepage
- `resume.html` is the web-formatted resume
- `presentation.html` is the web-formatted portfolio presentation
- `assets/sarah_sparks_resume.pdf` is the local resume PDF
- `assets/Presentation_Compressed.pdf` is the local presentation PDF
- `build_ai_data_analysis_pdf.py` creates `Ai and data analysis.pdf`
- `export_ai_data_analysis_images.py` creates images in `Ai and data analysis images/`
- `generate_pdf_pages.py` extracts the supplied PDFs into static HTML pages
- `Ai and data analysis images/` contains the exported portfolio images

## GitHub Pages

After pushing this repository to GitHub, enable GitHub Pages from the repository settings and publish from the `main` branch root. The homepage is `index.html`.

## Setup

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Generate Outputs

Create the PDF:

```bash
python build_ai_data_analysis_pdf.py
```

Create the image set:

```bash
python export_ai_data_analysis_images.py
```

Regenerate the web resume and presentation pages:

```bash
python generate_pdf_pages.py
```

## Notes

The scripts use local Windows font paths for Arial:

- `C:/Windows/Fonts/arial.ttf`
- `C:/Windows/Fonts/arialbd.ttf`

If you run this on another operating system, update the font paths in `export_ai_data_analysis_images.py`.
