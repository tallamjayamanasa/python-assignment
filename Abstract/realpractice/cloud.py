from abc import ABC, abstractmethod

class CloudStorage(ABC):

    @abstractmethod
    def upload(self):
        pass


class GoogleDrive(CloudStorage):

    def upload(self):
        print("File uploaded to Google Drive")


class AWSStorage(CloudStorage):

    def upload(self):
        print("File uploaded to AWS Storage")


class AzureStorage(CloudStorage):

    def upload(self):
        print("File uploaded to Azure Storage")


storage = [
    GoogleDrive(),
    AWSStorage(),
    AzureStorage()
]

for cloud in storage:
    cloud.upload()