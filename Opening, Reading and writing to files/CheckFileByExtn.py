import glob
glob.glob('./[0-9].*')
'''['./1.gif', './2.txt']'''
glob.glob('*.gif')
'''['1.gif', 'card.gif']'''
glob.glob('?.gif')
'''['1.gif']'''
glob.glob('**/*.txt', recursive=True)
'''['2.txt', 'sub/3.txt']'''
glob.glob('./**/', recursive=True)
'''['./', './sub/']'''
