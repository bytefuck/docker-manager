import docker

client = docker.from_env()

""" for container in client.containers.list(all=True):
    print(container.name)
     """
    
container=client.containers.get("cogn-kgm-api-develop")
for line in container.logs(stream=True):
    print(line.decode("utf-8"))