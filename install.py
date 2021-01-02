import subprocess
import glob


wheels = glob.glob("dist/*.whl")
if(not wheels or len(wheels) > 1):
  raise RuntimeError("no or multible weels found")

print("found: " + wheels[0])

subprocess.call(['pip', 'install', wheels[0]])