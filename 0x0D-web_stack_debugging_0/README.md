# 0x0D-web_stack_debugging_0

This project is part of <b>ALX Software Engineering Program</b>. This is my first web stack debugging as well.

`vagrant@vagrant:~$` docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
`vagrant@vagrant:~$ docker ps`
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
`vagrant@vagrant:~$ curl 0:8080`
curl: (52) Empty reply from server
`vagrant@vagrant:~$`

Here we can see that after starting my Docker container, I curl the port `8080` mapped to the Docker container port 80, it does not return a page but an error message. Note that you might also get the error message `curl: (52) Empty reply from server`.

After executing `service apache start`, The problem is fixed. The file <b>0-give_me_a_page</b> contains the command I executed to fix the problem.

# `DoHardThings`