import requests

class TestYandexDiskCreateFolder:
    def setup_method(self):
        TOKEN = ''                     # необходимо ввести токен !!!
        PATH = 'New_Folder'
        self.headers = {
            'Authorization': f'OAuth {TOKEN}'
        }
        self.params = {
            'path': PATH
        }
    def teardown_method(self):
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)

    def test_create_folder_201_200_409(self):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 201

        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 200

        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 409

    def test_create_folder_404(self):
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources',
                                params=self.params,
                                headers=self.headers)
        assert response.status_code == 404