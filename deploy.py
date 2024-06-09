# deploy.py
import os
import subprocess

def deploy(model_dir, namespace, cpu, memory, route):
    image_name = "sugar-model"
    image_tag = "latest"
    full_image_name = f"{os.getenv('DOCKER_HUB_USERNAME')}/{image_name}:{image_tag}"

    # Build Docker image
    subprocess.run(["docker", "build", "-t", full_image_name, "."], check=True)

    # Push Docker image
    subprocess.run(["docker", "push", full_image_name], check=True)

    # Login to OpenShift
    subprocess.run(["oc", "login", "--token=<your-token>", "--server=<your-server>"], check=True)

    # Create new project/namespace
    subprocess.run(["oc", "new-project", namespace], check=True)

    # Create deployment
    subprocess.run(["oc", "new-app", full_image_name, "--name=sugar-model", "-n", namespace], check=True)

    # Set resources
    subprocess.run(["oc", "set", "resources", "deployment", "sugar-model", "--limits", f"cpu={cpu},memory={memory}", "-n", namespace], check=True)

    # Expose the service
    subprocess.run(["oc", "expose", "svc/sugar-model", "--hostname", route, "-n", namespace], check=True)

# Example usage
if __name__ == "__main__":
    deploy(model_dir="model", namespace="sugar-namespace", cpu="500m", memory="512Mi", route="sugar-model-route")
