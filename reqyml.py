#!/usr/bin/python3
"""DOC"""
import requests
import yaml


class Reqyml:
    """
    This is class programm reqyaml
    """
    def __init__(self, config_yaml: dict) -> None:
        with open (config_yaml, "r") as yamlfile:
            self.config = yaml.safe_load(yamlfile)


    def __single_request_param(self,single_config: dict) -> None:
        """Parser signle script from yaml

        Args:
            single_config (dict): 1 script
        """
        self.method = single_config['method']
        self.url = single_config['url']
        self.payload = single_config["payload"] if "payload" in single_config else None
        self.headers = single_config["headers"] if "headers" in single_config else None
        self.response_type = single_config["return"] if "return" in single_config else "text"
        self.verify = single_config["verify"] if "verify" in single_config else True
        self.print_request = \
            single_config["print_requests"] if "print_requests" in single_config else False
        self.print_response = \
            single_config["print_requests"] if "print_requests" in single_config else False


    def __single_request(self, single_config: dict):
        """ 1 Request HTTP

        Args:
            single_config (dict): Dict from yaml file

        Returns:
            _type_: Text, Json return
        """
        self.__single_request_param(single_config)
        if self.method == 'get':
            self.response = requests.request(
                self.method,
                self.url,
                verify=self.verify,
                params=self.payload,
                headers = self.headers
            )
        else:
            self.response = requests.request(
                self.method,
                self.url,
                verify=self.verify,
                json = self.payload,
                headers = self.headers
            )
        if self.print_request:
            self.print_request_method()
        if self.print_response:
            self.print_response_method()
        return self.response_return()


    def response_return(self):
        """Return type response

        Returns:
            _type_: Return respose from type
        """
        if self.response_type == "json":
            return self.response.json()
        if self.response_type == "text":
            return self.response.text


    def all(self) -> list:
        """Iter All reqests from yamlfile

        Returns:
            list: Http-Response
        """
        respose_list = []
        for _, value in self.config.items():
            respose_list.append(self.__single_request(value))
        return respose_list


    def script(self, script):
        """ Select one script or All

        Args:
            script (_type_): _description_

        Returns:
            _type_: _description_
        """
        if script == "all":
            ret = self.all()
        else:
            ret =  self.__single_request(self.config[script])
        return ret


    def print_request_method(self) -> None:
        """Print request
        """
        print("====REQUEST====")
        print(f"{self.response.request.url} - {self.response.request.method}")
        print(f"HEADERS: {self.response.request.headers}")
        print(f"BODY: {self.response.request.body}")
        print("===============")


    def print_response_method(self) -> None:
        """_summary_
        """
        print("====RESPONSE====")
        print(self.response_return())
        print("===============")