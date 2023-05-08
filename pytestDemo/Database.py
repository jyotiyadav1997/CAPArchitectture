import paramiko
import mysql.connector
from subprocess import call, STDOUT
import os
# Create the connection object myconn = mysql.connector.connect(
# host="private-leadgen-mysql-ny-1-misc-do-user-7297834-0.b.db.ondigitalocean.com",user="jyoti.y_ro",
# passwd="E#twrT#$#%%^TEGE3rse%^")
DEVNULL = open(os.devnull, 'wb')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='private-leadgen-mysql-ny-1-misc-do-user-7297834-0.b.db.ondigitalocean.com', username='jyoti.y_ro', password='E#twrT#$#%%^TEGE3rse%^')
stdin, stdout, stderr = ssh.exec_command('Database.py')
ssh.close()

CONFIG = dict(
    SSH_SERVER='ssh.server.com',
    SSH_PORT=2222,
    SSH_USER='myuser',
    SSH_KEY='/path/to/user.key',
    REMOTE_PORT=62222,
    UNIX_SOCKET='/tmp/ssh_tunnel.sock',
    KNOWN_HOSTS='/path/to/specific_known_host_to_conflicts',
)


def start():
    return call(
        [
            'ssh', CONFIG['SSH_SERVER'],
            '-Nfi', CONFIG['SSH_KEY'],
            '-MS', CONFIG['UNIX_SOCKET'],
            '-o', 'UserKnownHostsFile=%s' % CONFIG['KNOWN_HOSTS'],
            '-o', 'ExitOnForwardFailure=yes',
            '-p', str(CONFIG['SSH_PORT']),
            '-l', CONFIG['SSH_USER'],
            '-R', '%d:localhost:22' % CONFIG['REMOTE_PORT']
        ],
        stdout=DEVNULL,
        stderr=STDOUT
    ) == 0


def stop():
    return __control_ssh('exit') == 0


def status():
    return __control_ssh('check') == 0


def __control_ssh(command):
    return call(
        ['ssh', '-S', CONFIG['UNIX_SOCKET'], '-O', command, 'x'],
        stdout=DEVNULL,
        stderr=STDOUT
    )