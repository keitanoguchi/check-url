import data
import urllib.request


def color_text(text, color):
    color_codes = {
        "green": "\033[32m",
        "red": "\033[31m",
        "reset": "\033[0m"
    }
    return color_codes[color] + text + color_codes["reset"]


def check_status(url, expected_status):

    indent = "  "

    try:
        res = urllib.request.urlopen(url)
        actual_status = res.getcode()

        if actual_status == expected_status:
            result = color_text("OK", "green")
        else:
            result = color_text("Alert", "red")

        print("[{}] {}".format(result, url))
        print(indent + "code: {}\n".format(actual_status))

    except urllib.error.HTTPError as e:
        actual_status = e.code
        error_reason = e.reason

        if actual_status == expected_status:
            result = color_text("OK", "green")
        else:
            result = color_text("Alert", "red")

        print("[{}] {}".format(result, url))
        print(indent + "code: {}".format(actual_status))
        print(indent + "reason: {}\n".format(error_reason))

    except urllib.error.URLError as e:
        error_reason = e.reason
        result = color_text("Alert", "red")

        print("[{}] {}".format(result, url))
        print(indent + "code: N/A")
        print(indent + "reason: {}\n".format(error_reason))


for i in range(len(data.items)):
    item = data.items[i]
    project = item["project"]

    print("---------- {} ----------".format(project))

    for j in range(len(item["assertions"])):
        assertion = item["assertions"][j]

        url = assertion["url"]
        expected_status = assertion["expected_status"]

        check_status(url, expected_status)
