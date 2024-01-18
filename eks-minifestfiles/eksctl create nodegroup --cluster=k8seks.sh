eksctl create nodegroup --cluster=k8seks\
 --region=ap-south-1 \
 --name=k8seks-cluster-ng-1 \
 --node-type=t2.medium \
 --nodes=2 \
 --nodes-min=2 \
 --nodes-max=3 \
 --node-volume-size=10 \
 --ssh-access \
 --ssh-public-key ~/.ssh/id_rsa.pub \
 --managed \
 --asg-access \
 --external-dns-access \
 --full-ecr-access \
 --appmesh-access \
 --alb-ingress-access        



 eksctl delete nodegroup --cluster=k8seksnew --name= k8seksnew-cluster-ng-1
 eksctl delete cluster --name=k8seksnew
              		 
