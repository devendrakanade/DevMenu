import os
import time

while True:
    os.system("tput setaf 2")
    print("\t\tWelcome to Devendra's Menu Driven program.")
    print("\t\t------------------------------------------")
    print("")
    print("")
    os.system("tput setaf 3")
    print("How can i help You: ")
    print("")
    print("")
    os.system("tput setaf 7")
    print("""
     0. To Quit
     1. To Use Linux functions
     2. To Use Hadoop functions
     3. To Use AWS Cloud
     4. To Use Docker functions
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("""
         0. Go to previous menu
         1. Create a directory
         2. List files in current directory
         3. Create an empty file
         4. Create a file and open for editing
         5. Add a new user
         6. Set/change password
         7. Show current RAM usage
         8. Show the disk usage
         9. Check if command is present
         10. Removes a command
         11. Lists the network configuration
         12. Checks the java running services
         13. List the CPU info
         14. Show currenty running processes
         15. Show running time of device
         16. Clear the cache
         17. Check which package provide the command
         18. Checks the connectivity to IP
         19. Create a user for running a specific command
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter directory name: ")
            str = "mkdir " + name
            os.system(str)
            print("")
            print("")
        elif choice == "2":
            os.system("ls -alh")
            print("")
            print("")
        elif choice == "3":
            name = input("Enter file name: ")
            str = "touch " + name
            os.system(str)
            print("")
            print("")
        elif choice == "4":
            name = input("Enter file name: ")
            str = "vim " + name
            os.system(str)
            print("")
            print("")
        elif choice == "5":
            name = input("Enter username: ")
            str = "useradd " + name
            os.system(str)
            print("")
            print("")
        elif choice == "6":
            name = input("Enter username: ")
            str = "passwd " + name
            os.system(str)
            print("")
            print("")
        elif choice == "7":
            os.system("free -m")
            print("")
            print("")
        elif choice == "8":
            os.system("df -h")
            print("")
            print("")
        elif choice == "9":
            name = input("Enter command name: ")
            str = "rpm -q " + name
            os.system(str)
            print("")
            print("")
        elif choice == "10":
            name = input("Enter command name: ")
            str = "rpm -e " + name
            os.system(str)
            print("")
            print("")
        elif choice == "11":
            os.system("ifconfig")
            print("")
            print("")
        elif choice == "12":
            os.system("jps")
            print("")
            print("")
        elif choice == "13":
            os.system("lscpu")
            print("")
            print("")
        elif choice == "14":
            os.system("ps -aux")
            print("")
            print("")
        elif choice == "15":
            os.system("uptime")
            print("")
            print("")
        elif choice == "16":
            os.system("echo 3 > /proc/sys/vm/drop_caches")
            print("")
            print("")
        elif choice == "17":
            name = input("Enter command to search: ")
            str = "yum whatprovides " + name
            os.system(str)
            print("")
            print("")
        elif choice == "18":
            name = input("Enter IP to check connectivity to: ")
            str = "ping -c 5 " + name
            os.system(str)
            print("")
            print("")
        elif choice == "19":
            name = input("Enter commad: ")
            str = "useradd -s " + name
            name = input("Enter the username: ")
            str = str + name
            os.system(str)
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
            print("")
            print("")

    elif choice == "2":
        print("""
         0. Go to previous menu
         1. Checks hadoop version
         2. Format hadoop namenode
         3. Start namenode service
         4. Start datanode service
         5. Show hadoop report
         6. List all the files present in hadoop filesystem
         7. Upload file to hadoop filesystem
         8. Remove file from hadoop filesystem
         9. List contents of a file in hdfs
         10. Upload file with a defined block size
         11. Create an empty file in hadoop filesystem
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("hadoop version")
            print("")
            print("")
        elif choice == "2":
            os.system("hadoop namenode -format")
            print("")
            print("")
        elif choice == "3":
            os.system("hadoop-daemon.sh start namenode")
            print("")
            print("")
        elif choice == "4":
            os.system("hadoop-daemon.sh start datanode")
            print("")
            print("")
        elif choice == "5":
            os.system("hadoop dfsadmin -report")
            print("")
            print("")
        elif choice == "6":
            os.system("hadoop fs -ls /")
            print("")
            print("")
        elif choice == "7":
            name = input("Enter path of file: ")
            str = "hadoop fs -put " + name
            name = input("Enter the destignation in hadoop: ")
            str = str + name
            os.system(str)
            print("")
            print("")
        elif choice == "8":
            name = input("Enter file to delete from hdfs: ")
            str = "hadoop fs -rm " + name
            os.system(str)
            print("")
            print("")
        elif choice == "9":
            name = input("Enter file whose content to view: ")
            str = "hadoop fs -cat " + name
            os.system(str)
            print("")
            print("")
        elif choice == "10":
            name = input("Enter block size(in bytes): ")
            str = "hadoop fs -Ddfs.block.size=" + name
            name = input("Enter path of file: ")
            str = str + " -put " + name + " "
            name = input("Enter destignation in hadoop: ")
            str = str + name
            os.system(str)
            print("")
            print("")
        elif choice == "11":
            name = input("Enter name of file to create in hdfs: ")
            str = "hadoop fs -touchz / " + name
            os.system(str)
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
            print("")
            print("")

    elif choice == "3":
        print("""
         0. Go to previous menu
         1. Configure AWS
         2. Create a Key-Pair
         3. Create a Security Group
         4. Launch an instance
         5. Create EBS
         6. Attach EBS
         7. Create S3 Bucket
         8. Store file in S3 Bucket
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("aws configure")
            print("")
            print("")
        elif choice == "2":
            name = input("Enter key name: ")
            os.system("aws ec2 create-key-pair --key-name {name}")
            print("")
            print("")
        elif choice == "3":
            group_name = input("Enter group name: ")
            description = input("Enter the description of security group: ")
            os.system('aws ec2 create-security-group --group-name {group_name} --description "{description}"')
            print("")
            print("")
        elif choice == "4":
            ami = input("Enter Amazon Machine Image ID: ")
            instance_type = input("Enter the instance type: ")
            count = input("Enter the number of instances you want to launch: ")
            subnet_id = input("Enter the subnet id where you want to launch: ")
            key_name = input("Enter the key pair value you want to use: ")
            security_group = input("Enter the security group name that you use: ")
            os.system("aws ec2 run-instances --image-id {ami} --instance-type {instance_type} --count {count} --subnet-id {subnet_id} --key-name {key_name} --security-group-ids {security_group}")
            print("")
            print("")
        elif choice == "5":
            zone = input("Enter availability zone: ")
            size = input("Enter the size: ")
            os.system("aws ec2 create-volume --availability-zone {zone} --no-encrypted --size {size}")
            print("")
            print("")
        elif choice == "6":
            instance_id = input("Enter EC2 Instance-ID: ")
            vol_id = input("Enter the Volume-ID: ")
            os.system("aws ec2 attach-volume --instance-id {instance_id} --volume-id {vol_id} --device xvdh")
            print("")
            print("")
        elif choice == "7":
            name = input("Enter the name you want to give to bucket: ")
            region = input("Enter the region: ")
            os.system = input("aws s3api create-bucket --bucket {name} --region {region} --create-bucket-configuration LocationConstraint={region}")
            print("")
            print("")
        elif choice == "8":
            bucket = input("Enter name of the bucket: ")
            file_object = input("Enter the path of the object with name: ")
            name_dir = input("Enter the name which you want to give to the object when i will save in the bucket: ")
            os.system = input("aws s3api put-object --bucket {bucket} --key {name_dir} --body \"{file_object}\"")
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
            print("")
            print("")

    elif choice == "4":
        print("""
         0. Go to previous menu
         1. Checks the docker version
         2. Creating a container
         3. Pull image from dockerhub
         4. List running docker containers
         5. List all docker containers
         6. List all images present in system
         7. Starting a docker container
         8. Stopping a docker container
         9. Deleting a docker container
         10. Stop all docker containers
         11. Delete all docker containers
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("docker version")
            print("")
            print("")
        elif choice == "2":
            name = input("Enter name of image: ")
            str = "docker run -it " + name
            name = input("Enter version of image: ")
            str = str + ":" + name
            os.system(str)
            print("")
            print("")
        elif choice == "3":
            name = input("Enter name of image: ")
            str = "docker pull " + name
            name = input("Enter version of image: ")
            str = str + ":" + name
            os.system(str)
            print("")
            print("")
        elif choice == "4":
            os.system("docker ps")
            print("")
            print("")
        elif choice == "5":
            os.system("docker ps -a")
            print("")
            print("")
        elif choice == "6":
            os.system("docker images")
            print("")
            print("")
        elif choice == "7":
            name = input("Enter container name: ")
            str = "docker container start " + name
            os.system(str)
            print("")
            print("")
        elif choice == "8":
            name = input("Enter container name: ")
            str = "docker container stop " + name
            os.system(str)
            print("")
            print("")
        elif choice == "9":
            name = input("Enter container name: ")
            str = "docker container rm " + name
            os.system(str)
            print("")
            print("")
        elif choice == "10":
            os.system("docker container rm $(docker container ls –aq)")
            print("")
            print("")
        elif choice == "11":
            os.system("docker container stop $(docker container ls –aq) && docker system prune –af ––volumes")
            print("")
            print("")
        elif choice == "0":
            continue
        else:
            os.system("tput setaf 1")
            print("ERROR: Command not found")
            os.system("tput setaf 7")
            print("")
            print("")

    elif choice == "0":
        exit()

    else:
        os.system("tput setaf 1")
        print("ERROR: Command not found")
        os.system("tput setaf 7")
        print("")
        print("")

    time.sleep(1)
