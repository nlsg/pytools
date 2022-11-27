from os import popen

def get_results(tests):
    return ('python cheatsheet.py ' + t for t in tests)

def exec_tests(tests):
    return [popen(t).read() for t in get_results(tests)]
exec_tests(['python json loads', 'vim map leader', 'hy gfor'])
