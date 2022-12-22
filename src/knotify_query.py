from email.mime import image
import docker

rna_seq = "AAAAAACUAAUAGAGGGGGGACUUAGCGCCCCCCAAACCGUAACCCC"
client = docker.from_env()
ret = client.containers.run("neoaggelos/knotify", "/knotify/bin/rna_analysis --sequence "+rna_seq,auto_remove=True)

print(ret)