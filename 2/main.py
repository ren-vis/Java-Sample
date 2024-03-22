import paramiko
import boto3
from io import BytesIO
from stat import S_ISDIR, S_ISREG
import os

# FTP configuration Environment variable passed from Parameters
host = os.environ['sftp_server']
port =  int(os.environ['sftp_port'])
username = os.environ['sftp_username']
password = os.environ['sftp_password']
remotedir = os.environ['sftp_remotedir']

# S3 configuration  Environment variable passed from Parameters
s3_bucketname = os.environ['s3_bucketname']
s3_foldername = os.environ['s3_folder']



s3 = boto3.resource('s3')
s3client = boto3.client('s3')

# Create FTP connection
transport = paramiko.Transport((host, port))
transport.connect(username = username, password = password)
    
# Create an SFTP client
with paramiko.SFTPClient.from_transport(transport) as sftp:

    # change to a subdirectory if required
    #sftp.chdir('/my-sub-folder')

    for entry in sftp.listdir_attr(remotedir):
        print(entry)
        mode = entry.st_mode

        # we have a regular file, not a folder
        if S_ISREG(mode):
            
            f=entry.filename

            with BytesIO() as data:
                print(f'Downloading file {f} from SFTP.. to S3')

                sftp.getfo(f,data)
                data.seek(0)
                                    
                s3client.upload_fileobj(
                    data,
                    f'{s3_bucketname}',
                    f'{s3_foldername}/{f}'
                ) 