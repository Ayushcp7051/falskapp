from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user_info(user_id):
    url = f"https://api2.sololearn.com/v2/userinfo/v3/profile/{user_id}?sections=1,3,7,8,9"
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaWQiOiJ7XCJJbnN0YW5jZUlkXCI6Mjc1MTAzMDcsXCJVc2VySWRcIjoyMjkwNzE4NSxcIk5pY2tuYW1lXCI6XCLwnZS48J2VqvCdlabwnZWk8J2VmSDwnZWC8J2VpvCdlZ7wnZWS8J2Vo1wiLFwiRGV2aWNlSWRcIjo3Mjk3MTA5MCxcIkNsaWVudElkXCI6MTE0MyxcIkxvY2FsZUlkXCI6MSxcIkFwcFZlcnNpb25cIjpcIjAuMC4wLjBcIixcIklzUHJvXCI6ZmFsc2UsXCJHZW5lcmF0aW9uXCI6XCI1MmQyN2VmMS1iZmFiLTQ3NTgtYmYyOS03M2NkZDRmZTNkZDRcIn0iLCJqdGkiOiJmYTc3Y2ZmOC04ZTk1LTQ4MjItODFlYy05MjJiZjUwODQyNWIiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJVc2VyIiwibmJmIjoxNjg2ODM4OTUzLCJleHAiOjE2ODY4NDI1NTMsImlzcyI6IlNvbG9MZWFybi5TZWN1cml0eS5CZWFyZXIiLCJhdWQiOiJTb2xvTGVhcm4uU2VjdXJpdHkuQmVhcmVyIn0.GjX_4AiuUl5KQ45pOKIkmWOSWDly_qmCT6M5bMzR12c',
        'Cookie': '__cf_bm=SZMQl4rLLqF8ekXEak8lsR4ZRmvJmeRhuu5WE4KcNx8-1686840561-0-AUQJXjDZ+o2UarlA1fS5Lpg7QE4AW+qGkN3aSbunsNya7f+S/TgMZ+N+pjG1PLLxWquS2nQXMdyvWt1CPFcwWW8='
    }

    response = requests.get(url, headers=headers)
    user_data = response.json()

    return jsonify(user_data)

if __name__ == '__main__':
    app.run()
