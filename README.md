# FastAPI MongoDB Kubernetes Deployment

This project demonstrates how to set up a Kubernetes infrastructure using `kind` (Kubernetes in Docker), deploy MongoDB as the database, and a simple FastAPI application. The setup includes integration with ArgoCD for continuous deployment and GitHub Actions for continuous integration.
![Screenshot 2024-06-26 at 5 44 07 PM](https://github.com/shubhsardana29/Plexicus/assets/52607235/1ad159e4-82c7-4063-a76b-814fce536a2f)

## Prerequisites

- Docker: Required to run `kind` and build Docker images.
- kind: Tool to run Kubernetes clusters locally using Docker containers.
- kubectl: Command-line tool to interact with Kubernetes clusters.
- Helm: Package manager for Kubernetes to deploy applications.
- GitHub Account: To host your code and use GitHub Actions.
- Docker Hub Account: To store your Docker images.

## Summary

This setup provides a fully automated CI/CD pipeline. Changes pushed to the GitHub repository trigger GitHub Actions to build and push the Docker image. ArgoCD monitors the repository and syncs the Kubernetes cluster with the latest manifests, ensuring your application is always up-to-date.

### Resources

- [Docker](https://docs.docker.com/get-docker/)
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)
- [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Helm](https://helm.sh/docs/intro/install/)
- [ArgoCD](https://argo-cd.readthedocs.io/en/stable/getting_started/)
- [GitHub Actions](https://docs.github.com/en/actions)


