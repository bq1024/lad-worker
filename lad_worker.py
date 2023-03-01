from kubernetes import client, config
from common.utils import get_random_port
from common.k8s import *

if __name__ == "__main__":

    container_name = "lad-worker-test"
    container_image = "wbq1995/lad_hello_world"
    container_port = 7860
    host_port = get_random_port()
    host_name = "crosschain.computer"
    container = Container(container_name, container_image, container_port, host_port)
    label = "lad-worker"

    config.load_kube_config()
    apps_v1 = client.AppsV1Api()
    core_v1_api = client.CoreV1Api()
    networking_v1_api = client.NetworkingV1Api()
    deployment = create_deployment_object(container, label)
    create_deployment(apps_v1, deployment)
    create_service(core_v1_api, container_port, label)
    create_ingress(networking_v1_api, container_port, label, host_name)



