import os
import os.path as osp

ROOT = '/'

SUBFOLDER_TO_PERMALINK = {
    ROOT: 'https://issaucsd.carrd.co/',
}

for subfolder, link in SUBFOLDER_TO_PERMALINK.items():

    print('making dir for', subfolder, 'with link', link)
    
    f = None
    if subfolder == ROOT:
        f = open('index.html', 'w')
    else:
        os.makedirs(subfolder)
        f = open(f'{subfolder}/index.html', 'w')

    f.write(
f"""<html>
    <head>
        <title>ISSA @ UCSD</title>
        <meta http-equiv="refresh" content="0;url={link}" />
    </head>
    <body>
        <p>You are being redirected to <a href="{link}">{link}</a></p>
        <p>If the redirect does not work, please click the link above to continue.</p>
    </body>
</html>
"""
    )
