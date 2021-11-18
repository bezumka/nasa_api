HOW TO RUN:

1. docker create -t -i -v <path_to_shared_folder=D:\Report>:/mnt/test/ <image_name> /bin/bashc
2. Login to Docker and go to /home directory
3. git clone https://github.com/bezumka/nasa_api.git
NOTES: If you are not sure, that Python and PIP installed to your ENV just use 'install.sh' file, please do not forget about rights: chmod +x install.sh

4. pip3 install -r /home/nasa_api/requirements.txt
5. docker exec <name_container> python3 /home/nasa_api/main.py


Enjoy!