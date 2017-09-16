### ssh-public-key-gen

check out [this github tutorial](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/).

explanation: this command generate ssh-keys public-key `~/.ssh/id_rsa.pub` and private-key `~/.ssh/id_rsa` for authentifications.

### ssh-copy-id

my-example, please replace `msbd5009stu25@csl2wk01.cse.ust.hk` with `your_account@domain_name`, after copying, you do not need to type in passwd anymore for your current local machine.

```zsh
ssh-copy-id  msbd5009stu25@csl2wk01.cse.ust.hk
```

explanation: this command append your local `~/.ssh/id_rsa.pub` to the server `~/.ssh/authorized_keys` file

### ssh login to server tcsh

```zsh
ssh your_account@domain_name
```

### scp usage

copy your local files to server

my-example, you need to replace some things

* replace `~/test.txt` with `your_file_local_path`
* replace `yche@csl2wk01.cse.ust.h` with `your_account@domain_name`
* replace `/tmp/yche` with `remote_dir_you_want_to_put_files`

```zsh
scp ~/test.txt yche@csl2wk01.cse.ust.hk:/tmp/yche
```

### sshfs usage

mount a server directory into your local directory

my-example, you need to replace some things

* replace `yche@csl2wk01.cse.ust.h` with `your_account@domain_name`
* replace `/homes/yche` with `remote_dir_you_want_to_mount`
* replace `~/mnt/ug-clu` with `your_own_local_dir`

```zsh
sshfs -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3 yche@csl2wk01.cse.ust.hk:/homes/yche ~/mnt/ug-clu
```

explanation: the `ServerAliveInterval=15` option asked `sshfs` to check if the server is alive every 15 seconds. `ServerAliveCountMax=3` allows the server to not respond for up to three alive checks. The result is that if the server is unavailable for 1 minute, `sshfs` will reconnect to the server.
