#Comentario para modificar o arquivo .py
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName('ExerciceSpark')
    .getOrCreate()
)

# Ler os dados da pasta raw no datalake do S3
enem = (
    spark
    .read
    .format('csv')
    .option('header', True)
    .option('inferSchema', True)
    .option('delimiter', ';')
    .load('s3://dl-igti-edc-anielle/raw/')
)
(
    enem
    .write
    .mode('overwrite')
    .format('parquet')
    .save('s3://dl-igti-edc-anielle/staging/enem')
)