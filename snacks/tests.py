from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="omar", email="o.fandi02@email.com", password="abc"
        )

        self.snack = Snack.objects.create(title="shawermah", purcheser=self.user ,description="Double")
    

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "shawermah")
        self.assertEqual(f"{self.snack.purcheser}", "omar")
        self.assertEqual(self.snack.description,"Double")


    def test_snack_list_view(self):
        response = self.client.get(reverse("list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "shawermah")
        self.assertTemplateUsed(response, "list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("details", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "omar")
        self.assertTemplateUsed(response, "details.html")

    def test_string_representation(self):
        self.assertEqual(str(self.snack), 'Snack object (1)')


    def test_snack_create_view(self):
        response = self.client.post(
            reverse("create"),
            {
                "title": "znger",
                "purcheser": self.user.id,
                "description": "spaicy",
            }, follow=True
        )

        self.assertRedirects(response, reverse("details", args="2"))
        self.assertContains(response, "znger")



    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("update", args="1"),
            {"title": "Updated title","purcheser":self.user.id,"description":"Updated values"}
        )

        self.assertRedirects(response, reverse("details", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("delete", args="1"))
        self.assertEqual(response.status_code, 200)

