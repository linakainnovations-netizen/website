import sys

b64 = open('logo_b64.txt', 'r').read().strip()
with open('pages/quote-tool.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Inject the constant
html = html.replace('let uploadedLogoDataUrl = null;', f'const DEFAULT_LOGO_B64 = \'{b64}\';\nlet uploadedLogoDataUrl = null;')

# 2. Fix the HTML tags for the logo
html = html.replace(
    '<div id=\"outLogoText\" class=\"print-logo\" style=\"width: 100px; height: 100px; background: #1B4332; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 1rem; text-align: center;\">LINAKA<br>LOGO</div>\n            <img id=\"outLogoImg\" style=\"display: none; max-width: 150px; max-height: 100px;\" alt=\"Custom Logo\">',
    '<img id=\"outLogoImg\" style=\"max-width: 150px; max-height: 100px;\" alt=\"LINAKA INNOVATIONS Logo\">'
)

# 3. Update JS references to outLogoText
html = html.replace("document.getElementById('outLogoText').style.display = 'none';", "")
html = html.replace("document.getElementById('outLogoText').style.display = 'flex';", "")

# 4. updatePreview() injection
html = html.replace(
    'document.getElementById("outDateIssued").textContent',
    'document.getElementById("outLogoImg").src = uploadedLogoDataUrl || DEFAULT_LOGO_B64;\n  document.getElementById("outDateIssued").textContent'
)

# 5. jsPDF download logic
old_pdf_logo = '''  if (uploadedLogoDataUrl) {
    doc.addImage(uploadedLogoDataUrl, 'PNG', 14, 15, 30, 30, '', 'FAST');
  } else {
    doc.setFillColor(...green);
    doc.rect(14, 15, 25, 25, 'F');
    doc.setTextColor(255);
    doc.setFontSize(8);
    doc.text("LINAKA", 17, 26);
    doc.text("LOGO", 19, 30);
  }'''

new_pdf_logo = """  if (uploadedLogoDataUrl) {
    doc.addImage(uploadedLogoDataUrl, 'PNG', 14, 15, 30, 30, '', 'FAST');
  } else {
    doc.addImage(DEFAULT_LOGO_B64, 'PNG', 14, 15, 30, 30, '', 'FAST');
  }"""
html = html.replace(old_pdf_logo, new_pdf_logo)

with open('pages/quote-tool.html', 'w', encoding='utf-8') as f:
    f.write(html)
