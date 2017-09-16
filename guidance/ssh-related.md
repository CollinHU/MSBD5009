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
