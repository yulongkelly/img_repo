import pytest
from django.test import RequestFactory
from django.urls import reverse
from PIL import Image as Img
from io import BytesIO

from images.views import image_create_view, image_detail_view, image_delete_view
from images.models import Image

import pdb

@pytest.fixture(autouse=True)
def test_img():
    size = (200,200)
    color = (255,0,0,0)
    img = Img.new("RGBA",size,color)
    file = BytesIO(img.tobytes())
    file.name = 'test.png'
    file.seek(0)
    return file

@pytest.mark.django_db()
class TestViews:
    def test_image_create_view(self, test_img):
        request = RequestFactory().post(reverse("mycreateview"), data={
           "imgName": test_img.name,
           "img": test_img,
        })

        response = image_create_view(request)
        assert response.status_code == 200
        image = Image.objects.get(name=test_img.name)
        assert image.upload
    
    def test_image_detail_view(self):
        Image.objects.create(name="img1", upload=None)
        Image.objects.create(name="img2", upload=None) 
        request = RequestFactory().get(reverse("mydetailview"), data={})

        response = image_detail_view(request)
        assert response.status_code == 200

    def test_img_delete_view(self):
        Image.objects.create(name="img1", upload=None)
        Image.objects.create(name="img2", upload=None)
        request = RequestFactory().post(reverse("mydeleteview"))

        image_delete_view(request)
        assert not Image.objects.all()
        



