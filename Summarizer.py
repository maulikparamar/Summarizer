import sys
import requests 
import json


def main():
    try:
        arg = sys.argv[1]

        text = "" 
        Isfile = False
        if(arg == '-t'):
            print("read file")
            arg = sys.argv[2]
            f = open(arg,"r")
            data = f.read()
            text = data
            Isfile = True
            f.close()
        else:
            print("read text")
            text = ' '.join(sys.argv[1:])

        # Ollama API, Qwen2 0.5B model in Ollama
        url = "http://localhost:11434/api/generate"
        headers = {
            "Content-Type":"application/json"
        }
        data={
            "model":"qwen2:0.5b",
            "prompt":text,
            "stream":False
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_text = response.text
            data = json.loads(response_text)
            ac_response = data["response"]
            print("Summary of ",text)
            print("--------------")
            print(ac_response)
        else:
            print("error", response.status_code,response.text)
    except:
        print("An exception occurred")
        print("Enter proper value")

if __name__ == '__main__':
    main()