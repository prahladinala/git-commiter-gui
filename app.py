import os
# cmd = 'touch myfile.txt'
# os.system(cmd)

os.system('git init')
os.system('git add .')
os.system('git commit -m "Commit message"')
os.system('git branch -M main')
os.system('git git remote add origin https://github.com/prahladinala/testing.git')
os.system('git push -u origin main')