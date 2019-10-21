from rest_framework.test import APITestCase
from app.models import OpenCelliD


class RestApiTests(APITestCase):

	def setUp(self):
		OpenCelliD.objects.create(mcc=245, net=35, area=45, cell=8798)
		OpenCelliD.objects.create(mcc=245, net=34, area=45, cell=8797)
		OpenCelliD.objects.create(mcc=245, net=34, area=43, cell=8796)
		OpenCelliD.objects.create(mcc=245, net=34, area=43, cell=8795)

	def test_rest_api_all_mcc(self):
		response = self.client.get('/api/opencellid/?mcc=245')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.json()), 4)

	def test_rest_api_all_mcc_net(self):
		response = self.client.get('/api/opencellid/?mcc=245&net=34')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.json()), 3)

	def test_rest_api_all_mcc_net_area(self):
		response = self.client.get('/api/opencellid/?mcc=245&net=34&area=43')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.json()), 2)

	def test_rest_api_all_mcc_net_area_cell(self):
		response = self.client.get('/api/opencellid/?mcc=245&net=35&area=45&8798')

		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.json()), 1)