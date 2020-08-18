import django.db.models as models
import django.core.exceptions as exceptions


def rating_validator(value):
    if value < 1 or value > 5:
        raise exceptions.ValidationError("Rating must be within the range of [1, 5].")


def helpful_votes_validator(value):
    if value < 0:
        raise exceptions.ValidationError("Number of helpful votes cannot be negative.")


class ReviewData(models.Model):
    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[rating_validator])
    # For weighted data points
    helpful_votes = models.IntegerField(validators=[helpful_votes_validator])
    # Summary + review text
    review = models.TextField(blank=True, null=True)
    positive = models.BooleanField()

    class Meta:
        abstract = True
        constraints = [models.CheckConstraint(check=models.Q(rating__gte=1) & models.Q(rating__lte=5), name="%(class)s_rating_constraint"),
                       models.CheckConstraint(check=models.Q(helpful_votes__gte=0), name="%(class)s_helpful_votes_constraint")]
        verbose_name = "review data"
        verbose_name_plural = "review data"


class Appliances(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "appliance"
        verbose_name_plural = "appliances"


class ArtsCraftsAndSewing(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "arts, crafts and sewing"
        verbose_name_plural = "arts, crafts and sewing"


class AudioBooks(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "audio book"
        verbose_name_plural = "audio books"


class Automotive(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "automotive"
        verbose_name_plural = "automotives"


class BeautyProducts(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "beauty product"
        verbose_name_plural = "beauty products"


class Books(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "book"
        verbose_name_plural = "books"


class CDsAndVinyl(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "CDs and vinyl"
        verbose_name_plural = "CDs and vinyl"


class CellPhonesAndAccessories(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "cell phones and accessories"
        verbose_name_plural = "cell phones and accessories"


class ClothingShoesAndJewelry(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "clothing, shoes and jewelry"
        verbose_name_plural = "clothing, shoes and jewelry"


class DigitalMusic(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "digital music"
        verbose_name_plural = "digital music"


class Electronics(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "electronic"
        verbose_name_plural = "electronics"


class Fashion(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "fashion"
        verbose_name_plural = "fashion"


class GiftCards(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "gift card"
        verbose_name_plural = "gift cards"


class GroceryAndGourmetFood(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "grocery and gourmet food"
        verbose_name_plural = "grocery and gourmet food"


class HomeAndKitchen(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "home and kitchen"
        verbose_name_plural = "home and kitchen"


class IndustrialAndScientificSupplies(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "industrial and scientific supplies"
        verbose_name_plural = "industrial and scientific supplies"


class Magazines(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "magazine"
        verbose_name_plural = "magazines"


class MoviesAndTV(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "movies and TV"
        verbose_name_plural = "movies and TV"


class MusicalInstruments(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "musical instrument"
        verbose_name_plural = "musical instruments"


class OfficeProducts(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "office product"
        verbose_name_plural = "office products"


class PatioLawnAndGarden(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "patio, lawn and garden"
        verbose_name_plural = "patio, lawn and garden"


class PetSupplies(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "pet supply"
        verbose_name_plural = "pet supplies"


class Software(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "software"
        verbose_name_plural = "software"


class SportsAndOutdoors(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "sport and outdoors"
        verbose_name_plural = "sport and outdoors"


class ToolsAndHomeImprovement(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "tools and home improvement"
        verbose_name_plural = "tools and home improvement"


class ToysAndBoardGames(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "toys and board games"
        verbose_name_plural = "toys and board games"


class VideoGames(ReviewData):
    class Meta(ReviewData.Meta):
        verbose_name = "video game"
        verbose_name_plural = "video games"

def percentage_validator(value):
    if value < 0 or value > 1:
        raise exceptions.ValidationError("Accuracy out of range.")

class Predictors(models.Model):
    table_name = models.CharField(max_length=100, unique=True)
    theta = models.TextField()
    theta_0 = models.TextField()
    avg_accuracy = models.DecimalField(max_digits=3, decimal_places=2, validators=[percentage_validator])

    def __str__(self):
        return str(self.table_name)

    class Meta:
        constraints = [models.CheckConstraint(check=models.Q(avg_accuracy__gte=0) & models.Q(avg_accuracy__lte=1), name="%(class)s_avg_accuracy")]
        verbose_name = "predictor"
        verbose_name_plural = "predictors"