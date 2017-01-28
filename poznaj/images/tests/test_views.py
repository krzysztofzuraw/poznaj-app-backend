from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from poznaj.images.models import Image

from .factories import ImageFactory


class TestImagesViewSet(APITestCase):

    @classmethod
    def setUpClass(cls):
        cls.image = ImageFactory()
        cls.list_url = reverse('image-list')
        cls.detail_url = reverse('image-detail', kwargs={'pk': cls.image.id})

    @classmethod
    def tearDownClass(cls):
        cls.image.image_file.delete()

    def test_get_all_images(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{
                'id': self.image.id,
                'title': self.image.title,
                'image_file': 'http://testserver/media/{}'.format(self.image.image_file.name),
            }]
        )

    def test_create_image(self):
        response = self.client.post(
            self.list_url,
            data={'title': 'example_image', 'image_file': self.image.image_file}
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Image.objects.count(), 2)
        image = Image.objects.get(title='example_image')
        self.assertEqual(image.title, 'example_image')
        image.image_file.delete()

    def test_delete_image(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Image.objects.count(), 0)

    def test_update_image(self):
        response = self.client.put(self.detail_url, data={'title': 'new_title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(Image.objects.get().title, 'new_title')
