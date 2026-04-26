import os
import glob

def replace_footer_vid():
    files = glob.glob('*.html') + glob.glob('pages/*.html') + glob.glob('website/includes/*.html')
    old_url = "https://assets.mixkit.co/videos/preview/mixkit-software-developer-working-on-code-4174-large.mp4"
    for f in files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        if old_url in content:
            # If the file is in a subdirectory like pages/, the relative path needs ../
            if 'pages' in f or 'includes' in f:
                new_url = "../website/assets/video/6015791_Business_Office_3840x2160.mp4"
            else:
                new_url = "website/assets/video/6015791_Business_Office_3840x2160.mp4"
                
            new_content = content.replace(old_url, new_url)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)

replace_footer_vid()
