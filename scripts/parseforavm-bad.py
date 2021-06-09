import subprocess
# REQUIRES SWFDUMP (Find Online)
subprocess.call("mkdir Compatible;mkdir Incompatible", shell=True)
for f in __import__("os").listdir(__import__("sys").argv[1]):
    if f == "Compatible" or f == "Incompatible" or "&" in f:
        continue
    if "ass" in str(subprocess.check_output("swfdump -t %s" % f, shell=True)):
        subprocess.call(f"rm -rf ./Compatible/{f};cp {f} ./Compatible", shell=True)
        print(f"{f}: Compatible")
    elif "as3" in str(subprocess.check_output("swfdump -t %s" % f, shell=True)):
        subprocess.call(f"rm -rf ./Incompatible/{f};cp {f} ./Incompatible", shell=True)
        print(f"{f}: Incompatible")
