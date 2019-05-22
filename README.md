# GL-devops-entrytask

## Docker
For docker images we will use python3:slim repo with psutil

### Build docker container

```
docker build -t test-mon .
```
**test-mon** - our docker-image name


### Check local docker-images 
```
docker images | grep test-mon
```

## Run monitoring script
For monitoring host params we forward */proc* folder to */host-proc* folder in docker container on run.
You can choose what metric you want to check
**cpu** for CPU params
or
**mem** for Memmory statistics

### Examples
```
docker run -v /proc:/host-proc test-mon cpu
docker run -v /proc:/host-proc test-mon mem

```
## Remove docker-image
```
docker rmi test-mon
```

