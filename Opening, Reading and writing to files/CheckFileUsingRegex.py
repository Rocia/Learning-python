import fnmatch, re

regex = fnmatch.translate('*.txt')
print(regex)
#'(?s:.*\\.txt)\\Z'
reobj = re.compile(regex)
reobj.match('foobar.txt')
'''
<_sre.SRE_Match object; span=(0, 10), match='foobar.txt'>
'''
