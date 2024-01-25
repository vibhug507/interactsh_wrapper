from flask import Flask
import subprocess
from wrapper_service import WrapperService
import sys

app = Flask(__name__)
service = WrapperService()
arguments = sys.argv

@app.route('/api/getURL', methods=['GET'])
def get_url():
    return service.get_url()

@app.route('/api/getInteractions', methods=['GET'])
def get_interactions():
    return service.get_interactions()

def execute_command(command):
    with open(log_file_path, 'w') as log_file:
        server_process = subprocess.Popen(command, stdout=log_file, stderr=subprocess.STDOUT, shell=True)

if __name__ == '__main__':
    host_, port_ = arguments[1], arguments[2]
    # Path to your 'interactsh-client' executable
    interactsh_command_ = arguments[3]
    app.run(host=host_, port=int(port_))
    execute_command(interactsh_command_)

    
