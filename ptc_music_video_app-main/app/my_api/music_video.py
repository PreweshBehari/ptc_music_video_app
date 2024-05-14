# Import packages
import requests

def get_api_data():
    """ Get Api data from the api url provided

    Yields:
        dict: A dictionary with music video meta data
    """

    # Api url
    api_url = "https://openwhyd.org/hot/electro?format=json"
    # Send request to api url
    response = requests.get(url=api_url)
    # Convert json string to python dict
    api_data = response.json()

    # Check if "tracks" column exists in data
    if "tracks" in api_data:
        # Check if there are records
        if len(api_data["tracks"]) > 0:
            # loop through the data
            # and yield response
            for data in api_data["tracks"]:
                # Create custom field list
                field_data = {
                    "name": data["name"],
                    "image_url": data["img"],
                    "video_url": data["trackUrl"],
                    "score": data["score"],
                }

                yield field_data
        else:
            yield []
