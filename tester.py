import pytest
import subprocess
subprocess.call('clear', shell=True)

pytest.main(['-x', 'unit_testing'])