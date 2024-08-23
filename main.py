import os
import json

with open("set-mode/mode.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    mode = loads['mode']
    update = loads['update']
    print("MODE     =",mode)

if update == "1":
    os.popen('sh ~/jk8180-multi/move.sh')

if  mode == "0":
 with open("set-miner-on-multi/ccminer.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    pool = loads['pool']
    wallet = loads['wallet']
    password = loads['pass']
    print("POOL     =",pool)
    print("WALLET   =",wallet)
    print("PASSWORD =",password)
 POOL=pool
 WALLET=wallet
 PASSWORD=password

 with open("set-miner-name-cpu-all/name-cpu-all.json", "r", encoding='utf8') as file:
    text = file.read()
    loads = json.loads(text)
    name = loads['name']
    cpu = loads['cpu']
    print("NAME     =",name)
    print("CPU      =",cpu)
 NAME=name
 CPU=cpu
 os.system(f"cd ccminer && ./ccminer -a verus -o {POOL} -u {WALLET}.{NAME} -p {PASSWORD} -t {CPU}")
