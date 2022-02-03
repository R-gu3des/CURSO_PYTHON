import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

# print("stderr: ",proc.stderr)
# print("stdout: ",proc.stdout)
# print("returncode: ",proc.returncode)
# print("args: ",proc.args)

saida = proc.stdout
# saida = saida.replace('icmp_seq', 'Ruan Guedes')
print(saida)