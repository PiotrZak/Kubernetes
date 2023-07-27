NAMESPACE ?= test

deploy:		## Deploy image to k8s
	@echo "deploying $(TAG_ESC) to $(NAMESPACE)"
	## Helm2 required.
	helm secrets upgrade --install -f ./cassandra/envs/$(NAMESPACE)/secrets.yaml