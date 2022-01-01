items = [
    {
        "project": "Google",
        "assertions": [
            {
                "url": "https://www.google.com/",
                "expected_status": 200
            },
        ]
    },
    {
        "project": "Yahoo",
        "assertions": [
            {
                "url": "https://www.yahoo.co.jp/hoge",
                "expected_status": 404
            },
            {
                "url": "https://news.yahou.co.jp/",
                "expected_status": 200
            },
        ]
    },
    {
        "project": "tenki.jp",
        "assertions": [
            {
                "url": "https://tenki.jp/",
                "expected_status": 200
            }
        ]
    }
]
