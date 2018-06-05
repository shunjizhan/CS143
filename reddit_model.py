from __future__ import print_function
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

# IMPORT OTHER MODULES HERE
import cleantext

def main(context):
    """Main function takes a Spark SQL context."""
    # YOUR CODE HERE
    # YOU MAY ADD OTHER FUNCTIONS AS NEEDED


if __name__ == "__main__":
    conf = SparkConf().setAppName("CS143 Project 2B")
    conf = conf.setMaster("local[*]")
    sc = SparkContext(conf=conf)
    sqlContext = SQLContext(sc)
    sc.addPyFile("cleantext.py")

    # Task 1
    comments = sqlContext.read.json("comments-minimal.json")    # data_frame for comments
    submissions = sqlContext.read.json("submissions.json")		# data_frame for submissions
    labeled_data = sqlContext.read.load("comments-minimal-small.csv", format="csv", sep=",", inferSchema="true", header="true")

    # Task 2
    comments.createOrReplaceTempView("comments_view")			# Register the df as a SQL temporary view
    submissions.createOrReplaceTempView("submissions_view")
    labeled_data.createOrReplaceTempView("labeled_data_view")


    # labelded_comments = sqlContext.sql("	SELECT id, body, labeldem, labelgop, labeldjt FROM comments_view, labeled_data_view WHERE id = Input_id LIMIT 10")
    # labelded_comments.show()
    labelded_comments = sqlContext.sql("SELECT id, body, labeldem, labelgop, labeldjt FROM comments_view, labeled_data_view WHERE id = Input_id LIMIT 3")
    # labelded_comments.printSchema()
	
	# Task 3
    
    # Task 4