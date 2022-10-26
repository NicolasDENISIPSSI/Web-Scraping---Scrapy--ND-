# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class WebcrawlerPipeline:
    def process_item(self, item, spider):
        return item


class Database:
    def connectDb():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE IF NOT EXISTS animelist")

    def createTable():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="animelist"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            "CREATE TABLE IF NOT EXISTS animes (title VARCHAR(255), img VARCHAR(255), description TEXT(50000))")

    def addRow(item):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="animelist"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO animes (title, img, description) VALUES (%s, %s, %s)"
        val = (item['title'], item['img'], item['desc'])
        mycursor.execute(sql, val)
        mydb.commit()
