# nasdaq_scraper

The application is built from Python using Scrapy library as the main source of development 
to scrape stocks and news data from nasdaq website.
It can produce the following data to be analyzed:
-------------------------------------------------------------------------------------------------------

1) Stock historical price only close, volume from Nasdaq 3 month period from any stock in nasdaq

2) News only title, description from Nasdaq rss feed

The first step is to clone nasdaq_scraper to one of the directory in your computer.
-------------------------------------------------------------------------------------------------------
To get the stock data, follow these steps:
-------------------------------------------------------------------------------------------------------
  1) Open the command prompt

  2) Go to the project’s top level nasdaq directory and run this command: scrapy crawl stock -a symbol=goog -o the_name_of_the_file.csv

In this case, you will get the result of google stock in csv file. The stock symbol can be changed to any stock you want 
e.g. scrapy crawl stock -a symbol=aapl -o the_name_of_the_file.csv for scraping apple stock data.

To get the news data, follow these steps:
-------------------------------------------------------------------------------------------------------
1) Open the command prompt

2) Go to the project’s top level nasdaq directory and run this command: scrapy crawl news the_name_of_the_file.csv

Now, you get the news of stocks and mutual funds from nasdaq website sorted by date.

the_name_of_the_file.csv means naming the file to anything you want

There are generated files as of 9/6/2016 inside the directory: goog.csv, aapl.csv, and news.csv
