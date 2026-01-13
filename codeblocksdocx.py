from docx import Document
from docx.shared import Pt, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# Helper to apply monospace style
def apply_code_style(run):
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0, 0, 0)

    # Add gray highlight background
    highlight = OxmlElement("w:highlight")
    highlight.set(qn("w:val"), "lightGray")
    run._element.get_or_add_rPr().append(highlight)

# Load your DOCX (update path if needed)
doc = Document("SHAPE Website Redesign.docx")

# Keywords that usually indicate code blocks
code_keywords = (
    "javascript", "typescript", "shellscript", "json", "scss",
    "# ", "import ", "export ", "const ", "def ", "class "
)

for para in doc.paragraphs:
    text = para.text.strip().lower()
    if any(text.startswith(keyword) for keyword in code_keywords):
        for run in para.runs:
            apply_code_style(run)

# Save as a new formatted file
doc.save("SHAPE Website Redesign - formatted.docx")
