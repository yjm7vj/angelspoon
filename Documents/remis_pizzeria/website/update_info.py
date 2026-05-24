import glob

# Paths to process
html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. ftco-intro section
    content = content.replace('000 (123) 456 7890', '681 247 1345')
    content = content.replace('A small river named Duden flows', 'Call us to order')
    
    content = content.replace('198 West 21th Street', '130 N Raleigh St')
    content = content.replace('Suite 721 New York NY 10016', 'Martinsburg, WV 25401')
    
    content = content.replace('Open Monday-Friday', 'Open Monday-Saturday')
    content = content.replace('8:00am - 9:00pm', '10:00am - 10:00pm')
    
    # 2. contact-section (contact.html)
    content = content.replace('198 West 21th Street, Suite 721 New York NY 10016', '130 N Raleigh St, Martinsburg, WV 25401')
    content = content.replace('<a href="tel://1234567920">+ 1235 2355 98</a>', '<a href="tel://6812471345">681 247 1345</a>')
    
    # 3. Footer (all files)
    content = content.replace('203 Fake St. Mountain View, San Francisco, California, USA', '130 N Raleigh St, Martinsburg, WV 25401')
    content = content.replace('<a href="#"><span class="icon icon-phone"></span><span class="text">+2 392 3929 210</span></a>', '<a href="tel://6812471345"><span class="icon icon-phone"></span><span class="text">681 247 1345</span></a>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated contact information in all HTML files.')
