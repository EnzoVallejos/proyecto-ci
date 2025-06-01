from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class CalculadoraViewTest(TestCase):
    def test_suma(self):
        response = self.client.post(reverse('calculadora'), {''
            'num1': '5',
            'num2': '4',
            'operacion': 'sumar'
            })
        self.assertEqual(response.context['resultado'], 1)

    def test_resta(self):
        response = self.client.post(reverse('calculadora'), {''
            'num1': '5',
            'num2': '4',
            'operacion': 'resta'
            })
        self.assertEqual(response.context['resultado'], 1)
