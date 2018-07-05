import twitter
import csv


loop_requests = True
show_console = True
dump_raw = True
dump_csv = True

raw_out = 'tweets_raw.txt'
csv_out = 'tweets.csv'

C_KEY = 'somekey'
C_SECRET = 'somesecret'
A_KEY = 'akey'
A_SECRET = 'asecret'

hash_tags = ['%23CannabisAct',
                '%23BillC45',
                '%23C45',
                '%23Legalization',
                '%23CannabisinCanada',
                '%23C46',
                '%23marijuananews',
                '%23marijuana',
                '%23cannabis',
                '%23MarijuanaDecriminalization',
                '%23blessthiscountry',
                '%23LegaliseCannabis'
                ]

sample_dates = ['since%3A2018-06-01%20until%3A2018-06-07', 'since%3A2018-06-08%20until%3A2018-06-14', 'since%3A2018-06-15%20until%3A2018-06-22']

all_messages = []
testquery = "q=pot%20&result_type=recent&since=2018-01-1&count=100"
query = 'l=en&q=%23CannabisAct%20OR%20%23BillC45%20OR%20%23C45%20OR%20%23Legalization%20OR%20%23CannabisinCanada%20OR%20%23C46%20since%3A2018-01-01%20until%3A2018-01-31&count=100'

counter = 0

try:
    api = twitter.Api(consumer_key=C_KEY, consumer_secret=C_SECRET, access_token_key=A_KEY, access_token_secret=A_SECRET)

    if loop_requests:
        for dates_range in sample_dates:
            for hashtag in hash_tags:
                print("getting range: ", dates_range)
                query = 'l=en&q=' + hashtag + '%20'+dates_range+'&count=100'
                results = api.GetSearch(raw_query=query)

                for message in results:
                    print(message)
                    all_messages.append(message)
                print("Mined ", len(results), " tweets")

        print("All messages count : ", len(all_messages))
        # output
        with open(raw_out, 'w', encoding='utf-8') as writer:
            for message in all_messages:
                writer.write(str(message) + '\n')

        # output csv
        c = 0
        with open(csv_out, 'w', encoding='utf-8') as writer:
            csv_writer = csv.writer(writer, delimiter=',', quotechar='"')
            for message in all_messages:
                c += 1
                csv_writer.writerow([c, message.text.strip(), ""])

    else:
        print("Getting a single tweet item:")
        query2 = 'l=en&q=' + hash_tags[0] +'%20' + sample_dates[10] + '&count=100'
        print("Query:\n", query2)
        results = api.GetSearch(raw_query=query2)

        for message in results:
            print(message)
            all_messages.append(message)
        print("Mined ", len(results), " tweets")
    print("Mined ", len(all_messages), " tweets")

except Exception as e:
    print("Exception occured: ", e)






