import django.test as test
import ML_reviews.models as models
import django.core.exceptions as exceptions
import django.db.utils as utils

# We are testing the abstract class ReviewData that all other models inherit.
class ReviewDataTests(test.TransactionTestCase):
    def setUp(self):
        pass

    def test_rating(self):
        appliance1 = models.Appliances(rating=3, helpful_votes=1, review="abc", positive=True)
        # Application-level
        appliance1.full_clean()
        # Database-level
        appliance1.save()

        # Range check --------------------------------------------------------------------------------
        appliance2 = models.Appliances(rating=0, helpful_votes=1, review="abc", positive=True)
        # Application-level
        with self.assertRaises(exceptions.ValidationError):
            appliance2.full_clean()
        # Database-level
        with self.assertRaises(utils.IntegrityError):
            appliance2.save()

        appliance3 = models.Appliances(rating=6, helpful_votes=1, review="abc", positive=True)
        # Application-level
        with self.assertRaises(exceptions.ValidationError):
            appliance3.full_clean()
        # Database-level
        with self.assertRaises(utils.IntegrityError):
            appliance3.save()

    def test_helpful_votes(self):
        appliance1 = models.Appliances(rating=1, helpful_votes=1, review="abc", positive=True)
        appliance1.save()

        # Cannot be negative
        appliance3 = models.Appliances(rating=1, helpful_votes=-1, review="abc", positive=True)
        # Application-level
        with self.assertRaises(exceptions.ValidationError):
            appliance3.full_clean()
        # Database-level
        with self.assertRaises(utils.IntegrityError):
            appliance3.save()

class PredictorsTests(test.TransactionTestCase):
    def setUp(self):
        pass

    def test_avg_accuracy(self):
        predictor = models.Predictors(table_name="abc", theta=123, theta_0=123, avg_accuracy=-1)
        # Application-level
        with self.assertRaises(exceptions.ValidationError):
            predictor.full_clean()
        # Database-level
        with self.assertRaises(utils.IntegrityError):
            predictor.save()

        predictor = models.Predictors(table_name="abc", theta=123, theta_0=123, avg_accuracy=2)
        # Application-level
        with self.assertRaises(exceptions.ValidationError):
            predictor.full_clean()
        # Database-level
        with self.assertRaises(utils.IntegrityError):
            predictor.save()

        predictor = models.Predictors(table_name="abc", theta=123, theta_0=123, avg_accuracy=0.5)
        # Application-level
        predictor.full_clean()
        # Database-level
        predictor.save()