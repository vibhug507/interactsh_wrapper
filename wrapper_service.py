import re
import json
from flask import jsonify

class WrapperService:
    def __init__(self):
        self.log_file_path = "logs.log"
        self.active_testing_server = None
        self.active_testing_server_code = None
        # Testing servers in interactsh have the following format: {text}.oast.{text}
        self.url_pattern = re.compile(r'\b\w+\.oast\.\w+\b')

    def find_active_testing_server(self):
        if self.active_testing_server is not None:
            return

        url = ""
        with open(self.log_file_path, 'r') as file:
            for line in file:
                print(line.strip())
                matches = re.findall(self.url_pattern, line.strip())
                if len(matches) > 0:
                    url = matches[0]
                    break

        self.active_testing_server_code = url.split('.')[0]
        self.active_testing_server = url
        return 

    def get_url(self):
        if self.active_testing_server is not None:
            return jsonify({"Testing Server": self.active_testing_server})

        self.find_active_testing_server()
        return jsonify({"Testing Server": self.active_testing_server})

    def get_interactions(self):
        if self.active_testing_server is None:
            self.find_active_testing_server()

        interactions = []
        with open(log_file_path, 'r') as file:
            for line in file:
                words = line.split(' ')
                if words[0] == "[" + self.active_testing_server_code + "]":
                    words.pop(0)
                    interaction = ' '.join(words)
                    interactions.append(interaction)

        return jsonify({"Interactions": interactions})