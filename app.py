{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "27a879ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting google-generativeai\n",
      "  Downloading google_generativeai-0.3.2-py3-none-any.whl (146 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m146.9/146.9 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting google-ai-generativelanguage==0.4.0\n",
      "  Downloading google_ai_generativelanguage-0.4.0-py3-none-any.whl (598 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m598.7/598.7 kB\u001b[0m \u001b[31m21.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: tqdm in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (4.64.1)\n",
      "Collecting protobuf\n",
      "  Downloading protobuf-4.25.2-cp37-abi3-macosx_10_9_universal2.whl (394 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m394.2/394.2 kB\u001b[0m \u001b[31m38.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: typing-extensions in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from google-generativeai) (4.3.0)\n",
      "Collecting google-api-core\n",
      "  Downloading google_api_core-2.15.0-py3-none-any.whl (121 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m122.0/122.0 kB\u001b[0m \u001b[31m15.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting google-auth\n",
      "  Downloading google_auth-2.26.2-py2.py3-none-any.whl (186 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m186.5/186.5 kB\u001b[0m \u001b[31m27.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting proto-plus<2.0.0dev,>=1.22.3\n",
      "  Downloading proto_plus-1.23.0-py3-none-any.whl (48 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m48.8/48.8 kB\u001b[0m \u001b[31m6.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hCollecting googleapis-common-protos<2.0.dev0,>=1.56.2\n",
      "  Downloading googleapis_common_protos-1.62.0-py2.py3-none-any.whl (228 kB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m228.7/228.7 kB\u001b[0m \u001b[31m25.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: requests<3.0.0.dev0,>=2.18.0 in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from google-api-core->google-generativeai) (2.28.1)\n",
      "Collecting cachetools<6.0,>=2.0.0\n",
      "  Downloading cachetools-5.3.2-py3-none-any.whl (9.3 kB)\n",
      "Collecting rsa<5,>=3.1.4\n",
      "  Downloading rsa-4.9-py3-none-any.whl (34 kB)\n",
      "Requirement already satisfied: pyasn1-modules>=0.2.1 in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from google-auth->google-generativeai) (0.2.8)\n",
      "Collecting grpcio-status<2.0.dev0,>=1.33.2\n",
      "  Downloading grpcio_status-1.60.0-py3-none-any.whl (14 kB)\n",
      "Collecting grpcio<2.0dev,>=1.33.2\n",
      "  Downloading grpcio-1.60.0-cp39-cp39-macosx_10_10_universal2.whl (9.7 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.7/9.7 MB\u001b[0m \u001b[31m14.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: pyasn1<0.5.0,>=0.4.6 in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from pyasn1-modules>=0.2.1->google-auth->google-generativeai) (0.4.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (1.26.11)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (3.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (2022.9.24)\n",
      "Requirement already satisfied: charset-normalizer<3,>=2 in /Users/hy/opt/anaconda3/lib/python3.9/site-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core->google-generativeai) (2.0.4)\n",
      "Installing collected packages: rsa, protobuf, grpcio, cachetools, proto-plus, googleapis-common-protos, google-auth, grpcio-status, google-api-core, google-ai-generativelanguage, google-generativeai\n",
      "Successfully installed cachetools-5.3.2 google-ai-generativelanguage-0.4.0 google-api-core-2.15.0 google-auth-2.26.2 google-generativeai-0.3.2 googleapis-common-protos-1.62.0 grpcio-1.60.0 grpcio-status-1.60.0 proto-plus-1.23.0 protobuf-4.25.2 rsa-4.9\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install google-generativeai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c125119c-0781-466b-b7c4-1a6a5fa61604",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask,request,render_template\n",
    "import google.generativeai as palm\n",
    "palm.configure(api_key=\"AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4\")\n",
    "model = {\"model\":\"models/chat-bison-001\"}\n",
    "app = Flask(__name__)\n",
    "@app.route(\"/\",methods = [\"GET\",\"POST\"])\n",
    "def index():\n",
    "    if request.method == \"POST\":\n",
    "        q = request.form.get(\"q\")\n",
    "        print(q)\n",
    "        r = palm.chat(\n",
    "        **model,\n",
    "        messages = q\n",
    "        )\n",
    "        \n",
    "        return render_template(\"index.html\", result = r.last)\n",
    "    else:\n",
    "        return render_template(\"index.html\", result = \"waiting for exchange rate.............\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
