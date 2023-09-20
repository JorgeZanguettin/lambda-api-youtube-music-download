import os
import boto3
import yt_dlp


BUCKET_NAME = os.environ['BUCKET_NAME']
FOLDER_NAME = os.environ['FOLDER_NAME']


def lambda_handler(event, context):
    if "video_id" in event['params']['querystring']:
        video_url = "https://www.youtube.com/watch?v={}".format(
            event['params']['querystring']['video_id']
        )
    elif "video_url" in event['params']['querystring']:
        video_url = event['params']['querystring']['video_url']
    else:
        return {
          'message': "No video id or url provided"
        }

    video_info = yt_dlp.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"/tmp/{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... {}".format(filename))

    url, log = upload_to_aws(
        filename,
        f"{FOLDER_NAME}/{video_info['title']}.mp3"
    )
    os.remove(
        filename
    )

    return {
        'message': log,
        'download': url
    }


def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(local_file, BUCKET_NAME, s3_file)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': s3_file
            }
        )

        url = str(url).split('?')[0]
        return url, "Upload Successful"
    except FileNotFoundError:
        return None, "The file was not found"
    except Exception as e:
        return None, str(e)
