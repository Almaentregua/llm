# LLM Experiments - Gemini

This repository is designed to experiment with Large Language Models (LLMs), starting with **Gemini** from Google.

## How to Use This Repository

### 1. Create the Environment
Run the following command to create a virtual environment:

```bash
make create-env
```
### 2. Install Dependencies
Install all required dependencies:

```bash
make install
source llm-env/bin/activate
```

### 3. Configure the .env File
Create a .env file in the root directory and add your API key:

```
API_KEY=your_api_key_here
```

You can obtain your API key from Google by visiting this link:
[Google AI Studio - API Key](https://aistudio.google.com/app/u/1/apikey?pli=1)

## Example Usage
Once the environment is set up and the .env file is configured, you can test the functionality by running a script. For instance:

```bash
python3 simpleGeminy.py
```

## Future Additions
This repository will expand to include experiments with other LLMs and integrations. Stay tuned!