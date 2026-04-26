import re

with open('pages/quote-tool.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Payment Terms Input
html = html.replace(
    '        <div style="flex: 1;">\n          <label>Tax Rate (%)</label>\n          <input type="number" id="inTax" value="0" min="0" oninput="saveAndPreview()">\n        </div>\n      </div>',
    '        <div style="flex: 1;">\n          <label>Tax Rate (%)</label>\n          <input type="number" id="inTax" value="0" min="0" oninput="saveAndPreview()">\n        </div>\n      </div>\n      <label style="margin-top: 1rem;">Payment Terms & Notes</label>\n      <textarea id="inPaymentTerms" rows="3" style="width: 100%; padding: 0.65rem; border: 1px solid #ccc; border-radius: 4px; margin-bottom: 1rem;" placeholder="E.g. 50% upfront, 50% upon completion" oninput="saveAndPreview()"></textarea>'
)

# 2. Update Signature Label
html = html.replace(
    '<label>Option 2: Type your Full Name (Backup)</label>\n      <input type="text" id="inSignature" placeholder="Enter name to sign" oninput="saveAndPreview()">',
    '<label>Signatory Name (Mandatory)</label>\n      <input type="text" id="inSignature" placeholder="Print your full name" oninput="saveAndPreview()">'
)

# 3. Update Preview HTML for Payment Terms
old_print_totals = '<div class="print-totals">\n          <div><span>Subtotal:</span><span id="outSubtotal">0.00</span></div>'
new_print_totals = """<div style="display: flex; justify-content: space-between; margin-bottom: 3rem;">
          <div style="width: 55%;">
            <strong style="color: #1B4332;">Payment Terms & Notes:</strong>
            <p id="outPaymentTerms" style="font-size: 0.9rem; margin-top: 0.5rem; white-space: pre-wrap; color: #555;"></p>
          </div>
          <div class="print-totals" style="width: 40%; margin: 0;">
          <div><span>Subtotal:</span><span id="outSubtotal">0.00</span></div>"""
html = html.replace(old_print_totals, new_print_totals)

old_print_totals_end = """<div style="border-bottom: none; margin-top: 0.5rem;">
            <strong style="color: #1B4332; font-size: 1.3rem;">Grand Total:</strong>
            <strong style="color: #1B4332; font-size: 1.3rem;" id="outGrandTotal">0.00</strong>
          </div>
        </div>"""
new_print_totals_end = """<div style="border-bottom: none; margin-top: 0.5rem;">
            <strong style="color: #1B4332; font-size: 1.3rem;">Grand Total:</strong>
            <strong style="color: #1B4332; font-size: 1.3rem;" id="outGrandTotal">0.00</strong>
          </div>
        </div>
      </div>"""
html = html.replace(old_print_totals_end, new_print_totals_end)

# 4. JS: saveAndPreview
html = html.replace('tax: document.getElementById("inTax").value,', 'tax: document.getElementById("inTax").value,\n    paymentTerms: document.getElementById("inPaymentTerms").value,')

# 5. JS: restoreSession
html = html.replace('document.getElementById("inTax").value = data.tax || 0;', 'document.getElementById("inTax").value = data.tax || 0;\n      document.getElementById("inPaymentTerms").value = data.paymentTerms || "";')

# 6. JS: updatePreview
html = html.replace('document.getElementById("outLogoImg").src = uploadedLogoDataUrl || DEFAULT_LOGO_B64;', 'document.getElementById("outLogoImg").src = uploadedLogoDataUrl || DEFAULT_LOGO_B64;\n  document.getElementById("outPaymentTerms").textContent = document.getElementById("inPaymentTerms").value || "N/A";')

html = html.replace(
    """  if (signaturePad && !signaturePad.isEmpty()) {
    sigImg.src = signaturePad.toDataURL("image/png");
    sigImg.style.display = "block";
    sigTxt.style.display = "none";
  } else {
    sigImg.style.display = "none";
    sigTxt.textContent = document.getElementById("inSignature").value;
    sigTxt.style.display = "block";
  }""",
    """  if (signaturePad && !signaturePad.isEmpty()) {
    sigImg.src = signaturePad.toDataURL("image/png");
    sigImg.style.display = "block";
  } else {
    sigImg.style.display = "none";
  }
  sigTxt.textContent = document.getElementById("inSignature").value;
  sigTxt.style.display = "block";
"""
)

# 7. JS: downloadNativePDF (validation)
html = html.replace('if (signaturePad.isEmpty() && !document.getElementById("inSignature").value.trim()) return alert("Signature required.");', 'if (!document.getElementById("inSignature").value.trim()) return alert("Signatory Name is mandatory.");')

# 8. JS: downloadNativePDF (Payment Terms rendering)
old_totals_render = 'doc.setFontSize(10);\n  doc.text("Subtotal:", 140, finalY);'
new_totals_render = """doc.setFontSize(10);
  doc.setFont("helvetica", "bold");
  doc.setTextColor(...green);
  doc.text("Payment Terms & Notes:", 14, finalY);
  doc.setFont("helvetica", "normal");
  doc.setTextColor(...charcoal);
  const splitTerms = doc.splitTextToSize(document.getElementById("inPaymentTerms").value || "N/A", 100);
  doc.text(splitTerms, 14, finalY + 6);
  
  doc.setFontSize(10);
  doc.text("Subtotal:", 140, finalY);"""
html = html.replace(old_totals_render, new_totals_render)

# 9. JS: downloadNativePDF (Signature & Filename)
old_sig_render = """  doc.setTextColor(...charcoal);
  doc.setFontSize(9);
  doc.setFont("helvetica", "normal");
  doc.text("Authorized Signature", 14, finalY + 5);

  if (!signaturePad.isEmpty()) {
    doc.addImage(signaturePad.toDataURL(), 'PNG', 14, finalY - 20, 50, 18);
  } else {
    doc.setFontSize(14);
    doc.setFont("times", "italic");
    doc.setTextColor(...green);
    doc.text(document.getElementById("inSignature").value, 14, finalY - 5);
  }

  doc.setTextColor(150);
  doc.setFontSize(9);
  doc.setFont("helvetica", "italic");
  doc.text("Thank you for choosing LINAKA INNOVATIONS.", 105, 285, { align: "center" });

  const clientName = document.getElementById("inClientName").value.trim().replace(/[^a-z0-9]/gi, '_').toLowerCase();
  doc.save(`${quoteNumber}_${clientName}.pdf`);"""

new_sig_render = """  doc.setTextColor(...charcoal);
  doc.setFontSize(9);
  doc.setFont("helvetica", "normal");
  doc.text("Authorized Signature", 14, finalY + 5);
  doc.setFontSize(11);
  doc.setFont("helvetica", "bold");
  doc.text(document.getElementById("inSignature").value, 14, finalY + 10);

  if (!signaturePad.isEmpty()) {
    doc.addImage(signaturePad.toDataURL(), 'PNG', 14, finalY - 20, 50, 18);
  }

  doc.setTextColor(150);
  doc.setFontSize(9);
  doc.setFont("helvetica", "italic");
  doc.text("Thank you for choosing LINAKA INNOVATIONS.", 105, 285, { align: "center" });

  const clientName = document.getElementById("inClientName").value.trim().replace(/[^a-zA-Z0-9 ]/g, '');
  doc.save(`LINAKA INNOVATION QUOTE - ${clientName}.pdf`);"""
html = html.replace(old_sig_render, new_sig_render)

with open('pages/quote-tool.html', 'w', encoding='utf-8') as f:
    f.write(html)
