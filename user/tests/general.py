# from user.models import User, Doctor, Patient


# # class UserLoginTestCase():

# #     def test_if_data_is_correct_then_register(self):
# #        pass
# #     def test_if_username_already_exists_dont_register(self):
# #             pass

# #     def test_correct_login(self):
# #        pass
    
# #     def test_if_password_incorrect_then_cant_login(self):
# #        pass
    
# #     def test_if_user_not_registered_cant_login(self):
# #        pass


# # ___________________ TDD _____________________

# class GetAllPuppiesTest(TestCase):
#     """ Test module for GET all puppies API """

#     def setUp(self):
#         Puppy.objects.create(
#             name='Casper', age=3, breed='Bull Dog', color='Black')

#     def test_get_all_puppies(self):
#         # get API response
#         response = client.get(reverse('get_post_puppies'))
#         # get data from db
#         puppies = Puppy.objects.all()
#         serializer = PuppySerializer(puppies, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GetSinglePuppyTest(TestCase):
#     """ Test module for GET single puppy API """

#     def setUp(self):
#         self.casper = Puppy.objects.create(
#             name='Casper', age=3, breed='Bull Dog', color='Black')

#     def test_get_valid_single_puppy(self):
#         response = client.get(
#             reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}))
#         puppy = Puppy.objects.get(pk=self.rambo.pk)
#         serializer = PuppySerializer(puppy)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_invalid_single_puppy(self):
#         response = client.get(
#             reverse('get_delete_update_puppy', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# class CreateNewPuppyTest(TestCase):
#     """ Test module for inserting a new puppy """

#     def setUp(self):
#         self.valid_payload = {
#             'name': 'Muffin',
#             'age': 4,
#             'breed': 'Pamerion',
#             'color': 'White'
#         }
#         self.invalid_payload = {
#             'name': '',
#             'age': 4,
#             'breed': 'Pamerion',
#             'color': 'White'
#         }

#     def test_create_valid_puppy(self):
#         response = client.post(
#             reverse('get_post_puppies'),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_invalid_puppy(self):
#         response = client.post(
#             reverse('get_post_puppies'),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class UpdateSinglePuppyTest(TestCase):
#     """ Test module for updating an existing puppy record """

#     def setUp(self):
#         self.casper = Puppy.objects.create(
#             name='Casper', age=3, breed='Bull Dog', color='Black')
#         self.muffin = Puppy.objects.create(
#             name='Muffy', age=1, breed='Gradane', color='Brown')
#         self.valid_payload = {
#             'name': 'Muffy',
#             'age': 2,
#             'breed': 'Labrador',
#             'color': 'Black'
#         }
#         self.invalid_payload = {
#             'name': '',
#             'age': 4,
#             'breed': 'Pamerion',
#             'color': 'White'
#         }

#     def test_valid_update_puppy(self):
#         response = client.put(
#             reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
#             data=json.dumps(self.valid_payload),
#             content_type='application/json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_update_puppy(self):
#         response = client.put(
#             reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}),
#             data=json.dumps(self.invalid_payload),
#             content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# class DeleteSinglePuppyTest(TestCase):
#     """ Test module for deleting an existing puppy record """

#     def setUp(self):
#         self.casper = Puppy.objects.create(
#             name='Casper', age=3, breed='Bull Dog', color='Black')
#         self.muffin = Puppy.objects.create(
#             name='Muffy', age=1, breed='Gradane', color='Brown')

#     def test_valid_delete_puppy(self):
#         response = client.delete(
#             reverse('get_delete_update_puppy', kwargs={'pk': self.muffin.pk}))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_invalid_delete_puppy(self):
#         response = client.delete(
#             reverse('get_delete_update_puppy', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
