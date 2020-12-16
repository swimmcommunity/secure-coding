import subprocess

def test_dependencies():    
    NO_ERROR_VALUE = 0
    cp = subprocess.run('safety check -r python/dependency_requirements.txt', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert cp.returncode == NO_ERROR_VALUE
    