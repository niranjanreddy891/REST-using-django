from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Employees
from .serializers import EmployeesSerializer


settings.configure()
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def add_employee(id=0, employee_name=""):
        if employee_name != "" and manager_name != "":
            Employees.objects.create(id=id, employee_name=employee_name, manager_name=manager_name)

    def setUp(self):
        self.add_employee(1, "niru", "pavi")
        self.add_employee(2, "nikki", "pravin")
        self.add_employee(3, "sandy", "Mia")
        self.add_employee(4, "Shashi", "Venki")

class GetAllEmployeesTest(BaseViewTest):
    def test_get_all_employees(self):
        response = self.client.get(
            reverse("employees-all", kwargs={"version": "v1"})
        )
        expected = Employees.objects.all()
        serialized = EmployeesSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)