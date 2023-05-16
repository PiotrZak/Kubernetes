
Copy Model into DockerFile.

ML Certificates - to have access (on macOs terminal):
```
bash /Applications/Python*/Install\ Certificates.command
```
https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz
11 MB

bash /Applications/Python*/Install\ Certificates.command

```
docker run -d --name serving_base tensorflow/serving
docker cp ./mymodel serving_base:/models/mymodel
docker commit --change "ENV MODEL_NAME mymodel" serving_base my-registry/mymodel-serving
docker kill serving_base
docker rm serving_base
docker run -d -p 8501:8501 my-registry/mymodel-serving
```

Terraform:

TerraCognita

works: AWS, Azure, GCP

output with flag:

--hcl or --module and --tfstate

https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/azure_cli

https://techcommunity.microsoft.com/t5/itops-talk-blog/azure-terrafy-import-your-existing-azure-infrastructure-into/ba-p/3357653

