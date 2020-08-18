import ML_reviews.models as models
import django.db.migrations as migrations
import pandas as pd
import os
import re
import numpy as np
import ML_reviews.perceptron as perceptron
import ML_reviews.evaluation as evaluation
import pickle


model_dictionary = dict()
model_dictionary = {"Appliances":models.Appliances,
                    "ArtsCraftsAndSewing":models.ArtsCraftsAndSewing,
                    "AudioBooks":models.AudioBooks,
                    "Automotive":models.Automotive,
                    "BeautyProducts":models.BeautyProducts,
                    "Books":models.Books,
                    "CDsAndVinyl":models.CDsAndVinyl,
                    "CellPhonesAndAccessories":models.CellPhonesAndAccessories,
                    "ClothingShoesAndJewelry":models.ClothingShoesAndJewelry,
                    "DigitalMusic":models.DigitalMusic,
                    "Electronics":models.Electronics,
                    "Fashion":models.Fashion,
                    "GiftCards":models.GiftCards,
                    "GroceryAndGourmetFood":models.GroceryAndGourmetFood,
                    "HomeAndKitchen":models.HomeAndKitchen,
                    "IndustrialAndScientificSupplies":models.IndustrialAndScientificSupplies,
                    "Magazines":models.Magazines,
                    "MoviesAndTV":models.MoviesAndTV,
                    "MusicalInstruments":models.MusicalInstruments,
                    "OfficeProducts":models.OfficeProducts,
                    "PatioLawnAndGarden":models.PatioLawnAndGarden,
                    "PetSupplies":models.PetSupplies,
                    "Software":models.Software,
                    "SportsAndOutdoors":models.SportsAndOutdoors,
                    "ToolsAndHomeImprovement":models.ToolsAndHomeImprovement,
                    "ToysAndBoardGames":models.ToysAndBoardGames,
                    "VideoGames":models.VideoGames}

def export_df_to_database(table_name, df):
    model_class = model_dictionary[table_name]

    for index, row_series in df.iterrows():
        model = model_class(rating=row_series["rating"], helpful_votes=row_series["helpful_votes"], review=row_series["review"], positive=row_series["positive"])
        model.save()

# def generate_predictor(table_name):
#     model_class = model_dictionary[table_name]
#
#     df = pd.DataFrame.from_records(data=model_class.objects.all().values())
#
#     # Find all unique
#     unique_words_set = set()
#     for index, row_series in df.iterrows():
#         wordList = re.sub("[^\w]", " ", row_series["review"]).split()
#         for word in wordList:
#             # Sets will automatically disregard duplicates.
#             unique_words_set.add(word)
#
#     unique_words_list = []
#     for word in unique_words_set:
#         unique_words_list.append(word)
#
#     skeleton_feature_representation = np.array(object=[unique_words_list])
#     skeleton_feature_representation = np.transpose(a=skeleton_feature_representation)
#     row, column = skeleton_feature_representation.shape
#     data = np.empty(shape=(row, 0))
#     labels = np.empty(shape=(1, 0))
#
#     for index, row_series in df.iterrows():
#         feature_representation = skeleton_feature_representation
#         for row in feature_representation:
#             word = row[0]
#             row[0] = row_series["review"].count(word)
#
#         data=np.append(arr=data, values=feature_representation, axis=1)
#         labels=np.append(arr=labels, values=np.array(object=[[float(row_series["positive"])]]), axis=1)
#
#     data=data.astype(dtype=float)
#     labels.astype(dtype=float)
#
#     # Test
#     # data=np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     #                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
#     # labels=np.array([[-1, -1, -1, -1, -1, 1, 1, 1, 1, 1]])
#
#     T = 10
#     old_accuracy = 0
#     avg_accuracy = 1
#     # print("(" + str(avg_accuracy) + ", " + str(T) + ")")
#
#     while np.abs(avg_accuracy - old_accuracy) > 0.01:
#         T += 10
#         avg_accuracy = evaluation.xval_learning_alg(learner=perceptron.perceptron, data=data, labels=labels,
#                                                        T=T, averaged=True, k=10)
#         old_accuracy = avg_accuracy
#
#         # print("(" + str(avg_accuracy) + ", " + str(T) + ")")
#
#     T = 0
#     training_accuracy = 0
#
#     while training_accuracy < 0.9:
#         T += 10
#         theta, theta_0 = perceptron.perceptron(data=data, labels=labels, T=T, averaged=True)
#         training_accuracy = evaluation.score(data, labels, theta, theta_0) / data.shape[1]
#         print(theta, theta_0, training_accuracy)
#
#
#     predictor = models.Predictors(table_name=table_name, theta=theta.dumps(), theta_0=theta_0.dumps(), avg_accuracy=avg_accuracy)
#     predictor.save()
#     print("\nunpickled theta: \n" + str(pickle.loads(data=theta.dumps())) + "\n")
#     print("\nunpickled theta_0: \n" + str(pickle.loads(data=theta_0.dumps())) + "\n")
#     # pass


def generate_predictor(table_name):
    model_class = model_dictionary[table_name]

    df = pd.DataFrame.from_records(data=model_class.objects.all().values())

    # Find all unique
    unique_words_set = set()
    for index, row_series in df.iterrows():
        wordList = re.sub("[^\w]", " ", row_series["review"]).split()
        for word in wordList:
            # Sets will automatically disregard duplicates.
            unique_words_set.add(word)

    unique_words_list = []
    for word in unique_words_set:
        unique_words_list.append(word)

    skeleton_feature_representation = np.array(object=[unique_words_list])
    skeleton_feature_representation = np.transpose(a=skeleton_feature_representation)
    row, column = skeleton_feature_representation.shape
    data = np.empty(shape=(row, 0))
    labels = np.empty(shape=(1, 0))
    data = data.astype(dtype=float)
    labels.astype(dtype=float)

    for index, row_series in df.iterrows():
        feature_representation = skeleton_feature_representation
        for row in feature_representation:
            word = row[0]
            row[0] = row_series["review"].count(word)

        feature_representation = feature_representation.astype(dtype=float)
        data = np.append(arr=data, values=feature_representation, axis=1)
        labels = np.append(arr=labels, values=np.array(object=[[float(row_series["positive"])]]), axis=1)

    # Test
    # data=np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    #                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    # labels=np.array([[-1, -1, -1, -1, -1, 1, 1, 1, 1, 1]])

    T = 10
    old_accuracy = 0
    avg_accuracy = 1
    # print("(" + str(avg_accuracy) + ", " + str(T) + ")")

    while np.abs(avg_accuracy - old_accuracy) > 0.01:
        T += 10
        avg_accuracy = evaluation.xval_learning_alg(learner=perceptron.perceptron, data=data, labels=labels,
                                                    T=T, averaged=True, k=10)
        old_accuracy = avg_accuracy

        # print("(" + str(avg_accuracy) + ", " + str(T) + ")")

    T = 0
    training_accuracy = 0

    while training_accuracy < 0.9:
        T += 10
        theta, theta_0 = perceptron.perceptron(data=data, labels=labels, T=T, averaged=True)
        training_accuracy = evaluation.score(data, labels, theta, theta_0) / data.shape[1]
        # print(theta, theta_0, training_accuracy)

    predictor = models.Predictors(table_name=table_name, theta=theta.dumps(), theta_0=theta_0.dumps(),
                                  avg_accuracy=avg_accuracy)
    predictor.save()
    # print("\nunpickled theta: \n" + str(pickle.loads(data=theta.dumps())) + "\n")
    # print("\nunpickled theta_0: \n" + str(pickle.loads(data=theta_0.dumps())) + "\n")
    # pass

def positive(df):
    if float(df["rating"]) > 2.5:
        return True
    elif float(df["rating"]) <= 2.5:
        return False

# Pre-condition: json file name without extension match model name.
def import_data(apps, schema_editor):
    base_dir = "ML_reviews/data"
    # base_dir = "data"
    # base_dir = "./ML_reviews/data"


    for file in os.listdir(base_dir):
        json_path = os.path.join(base_dir, file)
        table_name = re.sub(pattern="\.[a-z]*$", repl="", string=file)

        for df in pd.read_json(path_or_buf=json_path, lines=True, dtype=str, chunksize=500):

            # Some chunks may not have image or style column
            df.drop(
                columns=["verified", "reviewTime", "reviewerID", "asin", "reviewerName", "unixReviewTime"],
                inplace=True)

            if "image" in df.columns:
                df.drop(columns=["image"], inplace=True)

            if "style" in df.columns:
                df.drop(columns=["style"], inplace=True)

            df["review"] = df["summary"] + " " + df["reviewText"]
            df.drop(columns=["reviewText", "summary"], inplace=True)

            # Some chunks may not have vote column:
            df.rename(columns={"overall": "rating"}, inplace=True)

            if "vote" in df.columns:
                df.rename(columns={"vote": "helpful_votes"}, inplace=True)
            elif "vote" not in df.columns:
                df["helpful_votes"] = 0

            df["positive"] = df.apply(func=positive, axis=1)
            df["helpful_votes"].replace(to_replace=",", value="", regex=True, inplace=True)
            df["helpful_votes"].replace(to_replace="nan", value="0", regex=True, inplace=True)
            df = df.astype(
                dtype={"rating":"float", "helpful_votes":"int", "review":"object", "positive":"bool"}).copy()
            export_df_to_database(table_name=table_name, df=df)

        if not models.Predictors.objects.filter(table_name=table_name).exists():
            generate_predictor(table_name)

        print(table_name + " done!")

class Migration(migrations.Migration):
    dependencies = [("ML_reviews", "0001_initial")]
    operations = [migrations.RunPython(import_data)]

# if __name__ == "__main__":
#     import_data(None, None)