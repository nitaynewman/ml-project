# deploy.py
import os
import subprocess

def deploy(model_dir, namespace, cpu, memory, route_url):
    # build docker
    subprocess.run(["docker", "build", "-t", "ml-model:latest", "."], check=True)
    print("finish build")


    # Push Docker
    subprocess.run(["docker", "tag", "ml-model:latest", f"{route_url}/ml-model:latest"], check=True)
    subprocess.run(["docker", "push", f"{route_url}/ml-model:latest"], check=True)
    print("pushed")



    # os config
    subprocess.run(["oc", "apply", "-f", "deployment.yaml"], check=True)
    subprocess.run(["oc", "apply", "-f", "service.yaml"], check=True)
    subprocess.run(["oc", "apply", "-f", "route.yaml"], check=True)

    print("deployment complete.👍")

# deploy(model_dir="path/to/model", namespace="namespace", cpu="500m", memory="128Mi", route_url="route-url")


'''
- need to have logged in before to push
'''