from locust import HttpUser, task, between

class StressTest(HttpUser):
    wait_time = between(1, 3)

    @task(1)
    def test_text_endpoint(self):
        url = "/find_similarity?text=Cat,Two Cat,Dog,Person,Car"
        # url = "/find_similarity?text=A Cat,Two Cat,Dog,Person,Car"
        files=[('image',('1.jpg',open(r'C:/Users/0152013/Desktop/Test/2.jpg','rb'),'image/jpeg'))]
        res = self.client.post(
            url=url,
            headers={},
            data={},
            files=files
        )