This pod is being used for experiments in federated learning, and it runs a Flask server to fetch information from the already installed `ml-pipeline-ui` in Kubeflow using the `kfp.client` library.

1. **Creating the image**
   - Build the image using a Dockerfile.

2. **Deploying the pod and service**
   - Run the deployment script with `./deploy.sh`.
