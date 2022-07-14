import os
import boto3
import yt_dlp

def lambda_handler(event, context):
    video_id = event['params']['querystring']['video_id']
    video_url = f"https://www.youtube.com/watch?v={video_id}"
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
        f"musics/{video_info['title']}.mp3"
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
        s3.upload_file(local_file, 'lambda-youtube-downloader', s3_file)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': 'lambda-youtube-downloader',
                'Key': s3_file
            }
        )

        url = str(url).split('?')[0]
        return url, "Upload Successful"
    except FileNotFoundError:
        return None, "The file was not found"
    except Exception as e:
        return None, str(e)