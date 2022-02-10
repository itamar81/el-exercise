# Deployment
if you wand to run the deployment you need to run the command :
kubectl apply -f .\yamls\depolyment.yml 

to depoly to the cluster I used with miniKube cluster and my image stored localy
so if you want to run it on non local cluster you need to comment the attribute: 
```
imagePullPolicy: Never
```
to 

```
# imagePullPolicy: Never
````

## 