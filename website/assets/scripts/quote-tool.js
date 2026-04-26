/**
 * D:\linaka_innovations\website\assets\scripts\quote-tool.js
 * Professional Quote Generator Script using jsPDF
 */

// Initialize form defaults on DOM Load
document.addEventListener('DOMContentLoaded', () => {
  // Add first line item by default
  addItem();
  
  // Set default dates (Today & 14 Days from now)
  const today = new Date();
  document.getElementById('quoteDate').value = today.toISOString().split('T')[0];
  
  const validUntil = new Date();
  validUntil.setDate(today.getDate() + 14); 
  document.getElementById('validUntil').value = validUntil.toISOString().split('T')[0];

  // Generate random auto quote number (e.g. INV-12345)
  const randNum = Math.floor(10000 + Math.random() * 90000);
  document.getElementById('quoteNumber').value = `INV-${randNum}`;

  // Recalculate totals if tax rate changes
  document.getElementById('taxRate').addEventListener('input', calculateTotals);
});

/**
 * Adds a new row for a line item to the form
 */
function addItem() {
  const container = document.getElementById('itemsContainer');
  const itemDiv = document.createElement('div');
  itemDiv.className = 'quote-item-row';
  
  // Define row HTML including inputs that trigger calculateTotals()
  itemDiv.innerHTML = `
    <div style="flex: 2;">
      <input type="text" class="form-control item-desc" placeholder="Item description" oninput="calculateTotals()">
    </div>
    <div style="flex: 1;">
      <input type="number" class="form-control item-qty" placeholder="Qty" value="1" min="1" oninput="calculateTotals()">
    </div>
    <div style="flex: 1;">
      <input type="number" class="form-control item-price" placeholder="Unit Price" min="0" step="0.01" oninput="calculateTotals()">
    </div>
    <div style="flex: 1; display: flex; align-items: center; justify-content: space-between;">
      <span class="item-line-total" style="font-weight: 600;">ZMW 0.00</span>
      <button type="button" class="btn" style="background: #e74c3c; color: white; padding: 0.5rem; font-size: 0.9rem;" onclick="removeItem(this)">🗑️ Remove</button>
    </div>
  `;
  container.appendChild(itemDiv);
}

/**
 * Removes a specific line item row
 */
function removeItem(btn) {
  btn.parentElement.parentElement.remove();
  calculateTotals();
}

// Store current calculation values globally
let currentTotals = { subtotal: 0, tax: 0, grandTotal: 0 };

/**
 * Reads all line items and updates the subtotal, tax, and grand total in the UI
 */
function calculateTotals() {
  const descs = document.querySelectorAll('.item-desc');
  const qtys = document.querySelectorAll('.item-qty');
  const prices = document.querySelectorAll('.item-price');
  const lineTotals = document.querySelectorAll('.item-line-total');
  
  let subtotal = 0;
  
  for (let i = 0; i < descs.length; i++) {
    const qty = parseFloat(qtys[i].value) || 0;
    const price = parseFloat(prices[i].value) || 0;
    const total = qty * price;
    
    lineTotals[i].textContent = `ZMW ${total.toFixed(2)}`;
    subtotal += total;
  }
  
  const taxRate = parseFloat(document.getElementById('taxRate').value) || 0;
  const taxAmount = subtotal * (taxRate / 100);
  const grandTotal = subtotal + taxAmount;
  
  // Update UI
  document.getElementById('displaySubtotal').textContent = `ZMW ${subtotal.toFixed(2)}`;
  document.getElementById('displayTax').textContent = `ZMW ${taxAmount.toFixed(2)}`;
  document.getElementById('displayTotal').textContent = `ZMW ${grandTotal.toFixed(2)}`;

  currentTotals = { subtotal, tax: taxAmount, grandTotal };
}

/**
 * Validates inputs and generates a jsPDF document entirely on the client side.
 */
function generatePDF() {
  // 1. Gather Client Data
  const clientName = document.getElementById('clientName').value.trim();
  if (!clientName) {
    alert("Client Name is required.");
    return;
  }

  // Ensure calculations are fully up to date
  calculateTotals(); 

  const clientAddress = document.getElementById('clientAddress').value.trim() || 'N/A';
  const clientPhone = document.getElementById('clientPhone').value.trim() || 'N/A';
  const clientEmail = document.getElementById('clientEmail').value.trim() || 'N/A';
  
  // 2. Gather Quote Metadata
  const quoteDate = document.getElementById('quoteDate').value || 'N/A';
  const validUntil = document.getElementById('validUntil').value || 'N/A';
  const quoteNumber = document.getElementById('quoteNumber').value;
  const taxRate = document.getElementById('taxRate').value || '0';

  // 3. Gather Line Items
  const descs = document.querySelectorAll('.item-desc');
  const qtys = document.querySelectorAll('.item-qty');
  const prices = document.querySelectorAll('.item-price');
  
  let items = [];
  for (let i = 0; i < descs.length; i++) {
    const desc = descs[i].value.trim();
    const qty = parseFloat(qtys[i].value) || 0;
    const price = parseFloat(prices[i].value) || 0;
    
    if (desc && qty > 0) {
      items.push({ desc, qty, price, total: qty * price });
    }
  }

  if (items.length === 0) {
    alert("Please add at least one valid item with a description and quantity.");
    return;
  }

  // 4. Initialize jsPDF
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF();
  
  // Brand Colors mapped to RGB
  const green = [27, 67, 50]; // var(--color-green)
  const gold = [197, 160, 89]; // var(--color-gold)
  const charcoal = [46, 46, 46];

  // ==========================================
  // PDF HEADER SECTION
  // ==========================================
  
  // Logo Placeholder (Using a green box with white text as requested placeholder)
  doc.setFillColor(green[0], green[1], green[2]);
  doc.rect(20, 20, 40, 30, 'F');
  doc.setTextColor(255);
  doc.setFontSize(10);
  doc.setFont("helvetica", "bold");
  // Centered text in box loosely
  doc.text("LINAKA LOGO", 22, 36);

  // Company Name
  doc.setTextColor(green[0], green[1], green[2]);
  doc.setFontSize(22);
  doc.text("LINAKA INNOVATIONS", 70, 28);
  
  // Company Contact Details
  doc.setTextColor(charcoal[0], charcoal[1], charcoal[2]);
  doc.setFontSize(10);
  doc.setFont("helvetica", "normal");
  doc.text("Call: 0953526534", 70, 36);
  doc.text("WhatsApp: 0979400243", 70, 42);
  doc.text("Email: linakainnovations@gmail.com", 70, 48);
  doc.setFont("helvetica", "bold");
  doc.text("Bank Account: 0104317582200", 70, 54);

  // Quote Title & Meta
  doc.setTextColor(gold[0], gold[1], gold[2]);
  doc.setFontSize(26);
  doc.setFont("helvetica", "bold");
  doc.text("QUOTE", 150, 32);
  
  doc.setTextColor(charcoal[0], charcoal[1], charcoal[2]);
  doc.setFontSize(10);
  doc.setFont("helvetica", "normal");
  doc.text(`Quote #: ${quoteNumber}`, 150, 40);
  doc.text(`Date Issued: ${quoteDate}`, 150, 46);
  doc.text(`Valid Until: ${validUntil}`, 150, 52);

  // Separator line
  doc.setDrawColor(220, 220, 220);
  doc.line(20, 65, 190, 65);

  // ==========================================
  // CLIENT INFO SECTION
  // ==========================================
  doc.setFontSize(12);
  doc.setFont("helvetica", "bold");
  doc.setTextColor(green[0], green[1], green[2]);
  doc.text("Quote For:", 20, 75);
  
  doc.setFontSize(10);
  doc.setFont("helvetica", "normal");
  doc.setTextColor(charcoal[0], charcoal[1], charcoal[2]);
  doc.text(`Name: ${clientName}`, 20, 82);
  doc.text(`Address: ${clientAddress}`, 20, 88);
  doc.text(`Phone: ${clientPhone}`, 20, 94);
  doc.text(`Email: ${clientEmail}`, 20, 100);

  // ==========================================
  // TABLE HEADER SECTION
  // ==========================================
  let startY = 115;
  doc.setFillColor(green[0], green[1], green[2]);
  doc.rect(20, startY, 170, 10, 'F');
  doc.setTextColor(255);
  doc.setFont("helvetica", "bold");
  doc.text("Description", 25, startY + 7);
  doc.text("Qty", 120, startY + 7);
  doc.text("Unit Price (ZMW)", 140, startY + 7);
  doc.text("Total (ZMW)", 175, startY + 7, { align: "center" });

  // ==========================================
  // TABLE ROWS SECTION
  // ==========================================
  let y = startY + 16;
  doc.setTextColor(charcoal[0], charcoal[1], charcoal[2]);
  doc.setFont("helvetica", "normal");

  items.forEach(item => {
    // Handling long descriptions by wrapping them
    const splitDesc = doc.splitTextToSize(item.desc, 85);
    doc.text(splitDesc, 25, y);
    doc.text(item.qty.toString(), 120, y);
    doc.text(item.price.toFixed(2), 140, y);
    doc.text(item.total.toFixed(2), 175, y, { align: "center" });
    
    y += (splitDesc.length * 5) + 5;
    
    // Page break logic if items run off page
    if (y > 260) {
      doc.addPage();
      y = 20;
    }
  });

  // ==========================================
  // TOTALS SECTION
  // ==========================================
  doc.setDrawColor(green[0], green[1], green[2]);
  doc.setLineWidth(0.5);
  doc.line(110, y, 190, y);
  
  y += 8;
  doc.text("Subtotal:", 135, y);
  doc.text(currentTotals.subtotal.toFixed(2), 175, y, { align: "center" });
  
  y += 6;
  doc.text(`Tax (${taxRate}%):`, 135, y);
  doc.text(currentTotals.tax.toFixed(2), 175, y, { align: "center" });
  
  y += 8;
  doc.setFont("helvetica", "bold");
  doc.setTextColor(green[0], green[1], green[2]);
  doc.setFontSize(12);
  doc.text("Grand Total:", 135, y);
  doc.text(`ZMW ${currentTotals.grandTotal.toFixed(2)}`, 175, y, { align: "center" });

  // ==========================================
  // FOOTER SECTION
  // ==========================================
  doc.setTextColor(120);
  doc.setFontSize(10);
  doc.setFont("helvetica", "italic");
  doc.text("Thank you for choosing LINAKA INNOVATIONS.", 105, 280, { align: "center" });

  // Force PDF download
  doc.save(`Quote_${quoteNumber}_${clientName.replace(/\s+/g, '_')}.pdf`);
}
