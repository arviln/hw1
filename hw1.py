
# coding: utf-8

# In[5]:

import mediacloud, datetime
mc = mediacloud.api.MediaCloud('myapikey')

restrump = mc.sentenceCount('trump', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
resclinton = mc.sentenceCount('clinton', solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])

print restrump['count'] # prints the number of sentences found
print resclinton['count'] # prints the number of sentences found


# In[ ]:




# In[ ]:




# In[ ]:



