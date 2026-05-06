import os
import glob
import re

def remove_trading_name():
    files = glob.glob('d:/linaka_innovations/website/**/*.html', recursive=True)
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # 1. Remove from strong tags: <strong>LINAKA INNOVATIONS</strong> (trading as Denfas Simfukwe)<br>
        content = content.replace("<strong>LINAKA INNOVATIONS</strong> (trading as Denfas Simfukwe)<br>", "<strong>LINAKA INNOVATIONS</strong><br>")
        
        # 2. Remove span in quote-tool print preview
        content = content.replace('<span style="font-size: 0.8rem;">(trading as Denfas Simfukwe)</span><br><br>', '')
        
        # 3. Remove doc.text in quote-tool js
        # We will replace doc.text("(trading as Denfas Simfukwe)", 70, 29); with nothing and shift others up by 5
        if 'doc.text("(trading as Denfas Simfukwe)", 70, 29);' in content:
            content = content.replace('doc.text("LINAKA INNOVATIONS-", 70, 24);', 'doc.text("LINAKA INNOVATIONS", 70, 24);')
            content = content.replace('<h2>LINAKA INNOVATIONS-</h2>', '<h2>LINAKA INNOVATIONS</h2>')
            
            content = content.replace('doc.text("(trading as Denfas Simfukwe)", 70, 29);\n', '')
            content = content.replace('doc.text("TPIN: 2002984908", 70, 34);', 'doc.text("TPIN: 2002984908", 70, 29);')
            content = content.replace('doc.text("Call: 0953526534", 70, 39);', 'doc.text("Call: 0953526534", 70, 34);')
            content = content.replace('doc.text("WhatsApp: 0979400243", 70, 44);', 'doc.text("WhatsApp: 0979400243", 70, 39);')
            content = content.replace('doc.text("Email: linakainnovations@gmail.com", 70, 49);', 'doc.text("Email: linakainnovations@gmail.com", 70, 44);')
            
            # Since bank details are at 54, 59, 64, 69, we shift them up to 49, 54, 59, 64
            content = content.replace('doc.text(`Bank: ${bName}`, 70, 54);', 'doc.text(`Bank: ${bName}`, 70, 49);')
            content = content.replace('doc.text(`Acc Name: ${accName}`, 70, 59);', 'doc.text(`Acc Name: ${accName}`, 70, 54);')
            content = content.replace('doc.text(`Acc No: ${bAcc}`, 70, 64);', 'doc.text(`Acc No: ${bAcc}`, 70, 59);')
            content = content.replace('doc.text(`SWIFT: ${bSwift}`, 70, 69);', 'doc.text(`SWIFT: ${bSwift}`, 70, 64);')
            
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")

if __name__ == '__main__':
    remove_trading_name()
