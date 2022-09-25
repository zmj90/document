multipass

https://multipass.run/docs

```bash
multipass get local.driver
multipass set local.driver=virtualbox

multipass get local.privileged-mounts
multipass set local.privileged-mounts=Yes

multipass networks

# 创建实例
multipass launch --network name=WLAN -d 10G -n primary
multipass launch --network WLAN -d 10G -n primary docker
multipass mount D:\doing\ubuntu primary:/home/ubuntu/zmj
multipass umount primary:Home
```

