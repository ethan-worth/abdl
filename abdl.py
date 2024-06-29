import requests
import json
from bs4 import BeautifulSoup
from pathvalidate import sanitize_filename

artist = input("Enter Artist's Airbit URL:")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Priority': 'u=1',
}

response = requests.get(f'https://airbit.com/{artist}')#, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
msoup = soup.body.script

for item in str(msoup).split('}],'):
    if '"getUserByUsername' in item:
        usrid = (item.split(':')[6].split('"')[0])

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://airbit.com',
    'priority': 'u=1, i',
    'referer': 'https://airbit.com/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

json_data = {
    'operationName': 'SearchBeatsByUser',
    'variables': {
        'userId': f'{usrid}',
        'first': 1000,
        'page': 1,
        'search': '',
    },
    'query': 'query SearchBeatsByUser($userId: ID!, $first: Int!, $page: Int!, $search: String!) {\n  searchBeatsByUser(\n    first: $first\n    page: $page\n    userId: $userId\n    search: $search\n    onlyMarketPlace: true\n  ) {\n    data {\n      ... on Beat {\n        ...BeatFields\n        __typename\n      }\n      __typename\n    }\n    paginatorInfo {\n      hasMorePages\n      total\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment BeatFields on Beat {\n  id\n  user {\n    id\n    name\n    username\n    avatar {\n      s50\n      s100\n      s300\n      s600\n      __typename\n    }\n    licenses {\n      allow_offers\n      broadcasting\n      default_id\n      discounts_enabled\n      discounts {\n        id\n        price\n        quantity\n        __typename\n      }\n      distribution\n      distribution_free\n      enabled\n      id\n      mp3\n      name\n      price\n      trackout\n      wav\n      __typename\n    }\n    muser {\n      id\n      isVerified\n      isProSeller\n      package {\n        id\n        name\n        __typename\n      }\n      __typename\n    }\n    followsCount\n    followersCount\n    isFollowedByUser\n    playCount\n    __typename\n  }\n  liked_by_current_user\n  likeCount\n  name\n  duration\n  filename\n  alias\n  tags {\n    id\n    name\n    __typename\n  }\n  artwork {\n    id\n    sizes {\n      s50\n      s100\n      s300\n      s600\n      __typename\n    }\n    __typename\n  }\n  created: created_at\n  updated_at\n  genre {\n    id\n    name\n    alias\n    __typename\n  }\n  pricing {\n    id\n    price\n    discount\n    license {\n      id\n      __typename\n    }\n    __typename\n  }\n  isForFreeDownload\n  httpStream\n  hls\n  hasWav\n  hasTrackout\n  waveform\n  playCount\n  isPromoted\n  genre {\n    id\n    name\n    alias\n    __typename\n  }\n  mpUrl: marketplaceUrl\n  __typename\n}\n',
}

r = requests.post('https://api.airbit.com/gpl', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"operationName":"SearchBeatsByUser","variables":{"userId":"351962","first":20,"page":1,"search":""},"query":"query SearchBeatsByUser($userId: ID!, $first: Int!, $page: Int!, $search: String!) {\\n  searchBeatsByUser(\\n    first: $first\\n    page: $page\\n    userId: $userId\\n    search: $search\\n    onlyMarketPlace: true\\n  ) {\\n    data {\\n      ... on Beat {\\n        ...BeatFields\\n        __typename\\n      }\\n      __typename\\n    }\\n    paginatorInfo {\\n      hasMorePages\\n      total\\n      __typename\\n    }\\n    __typename\\n  }\\n}\\n\\nfragment BeatFields on Beat {\\n  id\\n  user {\\n    id\\n    name\\n    username\\n    avatar {\\n      s50\\n      s100\\n      s300\\n      s600\\n      __typename\\n    }\\n    licenses {\\n      allow_offers\\n      broadcasting\\n      default_id\\n      discounts_enabled\\n      discounts {\\n        id\\n        price\\n        quantity\\n        __typename\\n      }\\n      distribution\\n      distribution_free\\n      enabled\\n      id\\n      mp3\\n      name\\n      price\\n      trackout\\n      wav\\n      __typename\\n    }\\n    muser {\\n      id\\n      isVerified\\n      isProSeller\\n      package {\\n        id\\n        name\\n        __typename\\n      }\\n      __typename\\n    }\\n    followsCount\\n    followersCount\\n    isFollowedByUser\\n    playCount\\n    __typename\\n  }\\n  liked_by_current_user\\n  likeCount\\n  name\\n  duration\\n  filename\\n  alias\\n  tags {\\n    id\\n    name\\n    __typename\\n  }\\n  artwork {\\n    id\\n    sizes {\\n      s50\\n      s100\\n      s300\\n      s600\\n      __typename\\n    }\\n    __typename\\n  }\\n  created: created_at\\n  updated_at\\n  genre {\\n    id\\n    name\\n    alias\\n    __typename\\n  }\\n  pricing {\\n    id\\n    price\\n    discount\\n    license {\\n      id\\n      __typename\\n    }\\n    __typename\\n  }\\n  isForFreeDownload\\n  httpStream\\n  hls\\n  hasWav\\n  hasTrackout\\n  waveform\\n  playCount\\n  isPromoted\\n  genre {\\n    id\\n    name\\n    alias\\n    __typename\\n  }\\n  mpUrl: marketplaceUrl\\n  __typename\\n}\\n"}'
#response = requests.post('https://api.airbit.com/gpl', headers=headers, data=data)

x = json.loads(r.text)

for song in x["data"]["searchBeatsByUser"]["data"]:
    with open(f'{sanitize_filename(song["name"])}.mp3', 'wb') as f:
        s = requests.get(song["httpStream"])
        f.write(s.content)
    print(song["httpStream"])