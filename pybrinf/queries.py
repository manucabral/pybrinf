'''
This file contains the queries used to extract data from the browser databases.
TODO: join mozilla and chrome queries
'''

WEBSITE_QUERY = '''
SELECT url, title, visit_count, last_visit_time
FROM urls
ORDER BY last_visit_time DESC
'''
MOZ_WEBSITE_QUERY = '''
SELECT url, title, visit_count, last_visit_date
from moz_places
ORDER BY last_visit_date DESC
'''

DOWNLOAD_QUERY = '''
SELECT total_bytes, current_path, start_time, end_time, tab_url, url
FROM downloads
LEFT JOIN downloads_url_chains
ON downloads.id = downloads_url_chains.id
ORDER BY start_time DESC
'''

MOZ_DOWNLOAD_QUERY = '''
SELECT 0 as total_bytes, content as current_path, dateAdded as start_time,
lastModified as end_time, url, url as tab_url
FROM moz_annos, moz_places
WHERE moz_annos.place_id == moz_places.id
ORDER BY start_time DESC
'''