# import time
from locust import HttpUser, task  # , between
from hsclient import HydroShare
import os
import glob
import urllib3
import logging
import random
urllib3.disable_warnings()

USERNAME = "asdf"
PASSWORD = "asdf"
HOST = "localhost"
PORT = 8000
PROTOCOL = 'http'


class HSUser(HttpUser):
    # wait_time = between(1, 2)
    number_of_resources = 1
    resources = {}

    # @task
    # def home(self):
    #     self.client.get("/home", verify=False)

    # @task
    # def discover(self):
    #     self.client.get("/search", verify=False)

    # @task
    # def delete(self):
    #     if self.resources:
    #         res_key = random.choice(list(self.resources.keys()))
    #         res = self.resources.pop(res_key)
    #         print(f"deleted {res}")
    #         res.delete()

    # @task
    # def my_resources(self):
    #     self.client.get("/my-resources/?f=owned&f=discovered&f=favorites&f=shared", verify=False)

    # @task
    # def create(self):
    #     with self.client.get("/create", catch_response=True) as response:
    #         try:
    #             new_res = self.hs.create()
    #             resIdentifier = new_res.resource_id
    #             self.resources[resIdentifier] = new_res
    #             logging.info(f"created {resIdentifier}")
    #             response.success()
    #         except Exception as e:
    #             logging.error(f"Error creating resource")
    #             # mark as a locust failure
    #             response.failure(f"Error creating resource: {e}")

    @task
    def download(self):
        if not self.resources:
            return
        with self.client.get("/download", catch_response=True) as response:
            res_key = random.choice(list(self.resources.keys()))
            try:
                self.resources[res_key].download()
                logging.info(f"downloaded {res_key}")
                response.success()
            except Exception as e:
                logging.error(f"Error downloading resource: {e}")
                # mark as a locust failure
                response.failure(f"Error downloading resource: {e}")

    @task
    def copy(self):
        if not self.resources:
            return
        with self.client.get("/copy", catch_response=True) as response:
            res_key = random.choice(list(self.resources.keys()))
            try:
                self.resources[res_key].copy()
                logging.info(f"copied {res_key}")
                response.success()
            except Exception as e:
                logging.error(f"Error copying resource: {e}")
                # mark as a locust failure
                response.failure(f"Error copying resource: {e}")

    @task
    def add_files(self):
        if not self.resources:
            return
        with self.client.get("/add_files", catch_response=True) as response:
            res_key = random.choice(list(self.resources.keys()))
            try:
                self.resources[res_key].file_upload("locustfile.py")
                logging.info(f"uploaded file to {res_key}")
                response.success()
            except Exception as e:
                logging.error(f"Error adding files to resource: {e}")
                # mark as a locust failure
                response.failure(f"Error adding files to resource: {e}")

    def create_resource(self):
        try:
            new_res = self.hs.create()
            resIdentifier = new_res.resource_id
            self.resources[resIdentifier] = new_res
            logging.info(f"created {resIdentifier}")
        except Exception:
            logging.error("Error creating resource")
            raise

    # def get_resources(self):
        # http://localhost:8000/hsapi/resource/?owner=asdf&edit_permission=false&published=false&include_obsolete=false

    def on_start(self):
        hs = HydroShare(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, protocol=PROTOCOL)
        self.client.get("/accounts/login/", verify=False)
        self.hs = hs
        self.resources = {}

        # create resources
        # just keep trying until we get the resources created
        for i in range(self.number_of_resources):
            logging.info(f"Creating resource {i}")
            count = 0
            while True:
                try:
                    count += 1
                    logging.info(f"Attempt #{count} for create resource")
                    self.create_resource()
                except Exception:
                    continue
                else:
                    break

    def on_stop(self):
        for res in self.resources.values():
            logging.info(f"deleting {res}")
            res.delete()

        files = glob.glob('./*.zip')
        for f in files:
            logging.info(f"Cleanup file {f}")
            os.remove(f)