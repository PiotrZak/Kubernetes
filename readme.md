
Copy Model into DockerFile.

docker run -d --name serving_base tensorflow/serving
docker cp ./mymodel serving_base:/models/mymodel
docker commit --change "ENV MODEL_NAME mymodel" serving_base my-registry/mymodel-serving
docker kill serving_base
docker rm serving_base
docker run -d -p 8501:8501 my-registry/mymodel-serving