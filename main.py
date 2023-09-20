import json
import re
import os
import tiktoken
from collections import deque
import openai

def read_text_file(file_path):

  try:
    with open(file_path, "r") as f:
    read_file = f.read()


		return read_file

	except FileNotFoundError:
		print(f"Error: File '{file_path}' not found.")
		exit()

def write_jsonl_file(content, file_path):
  
	with open(file_path, "a") as f:
		for item in content:
			json.dump(item, f)
			f.write("\n")


	return

def separate_into_chapters(text):


	return re.split("\s*\*\*\s*", text)

def split_into_chunks(chapter, chunk_size = 2000):
	tokenizer = tiktoken.get_encoding("cl100k_base")
	tokens = tokenizer.encode(chapter)
	chunks = []
	for i in range(0, len(tokens), chunk_size):
		chunk_tokens = tokens[i:i + chunk_size]
		chunks.append(tokenizer.decode(chunk_tokens))


	return chunks

def format_for_fine_tuning(chunks):
  
	author = input("What is your author name? > ")
  system_message = f"You are a junior author who writes in the style of {author}"
  formatted_data = []
  queue = deque(chunks)
  while len(queue) > 1:

    user_message = queue.popleft()
    assistant_message = queue[0]
    message = {
        "messages": [
            { "role": "system", "content": system_message },
            { "role": "user", "content": user_message },
            { "role": "assistant", "content": assistant_message }
        ]
    }
    formatted_data.append(message)


    return formatted_data

def process_files():
  
	books = "books"
	fine_tune_messages = []

	for root, _, files in os.walk(books):
		for file in files:
			file_path = os.path.join(root, file)
			content = read_text_file(file_path)
			chapters = separate_into_chapters(content)

			for chapter in chapters:
				chunks = split_into_chunks(chapter)
				formatted_messages = format_for_fine_tuning(chunks)
				fine_tune_messages.extend(formatted_messages)
			print(f"{file} processed")

	write_jsonl_file(fine_tune_messages, "fine_tune.jsonl")
	print("All files processed")

def fine_tune(file_path):
  
	openai.api_key = os.environ.get("OPENAI_API_KEY")

	JSONL_file = openai.File.create(file=open("fine_tune.jsonl", "rb"), purpose="fine-tune")

	print("Uploaded file id", JSONL_file.id)

	while True:

		upload_file = openai.File.retrieve(id=JSONL_file.id)

    os.sys("clear")
    print("Processing file.")
    time.sleep(1)
    os.sys("clear")
    print("Processing file..")
    time.sleep(1)
    os.sys("clear")
    print("Processing file...")
    time.sleep(1)

		if upload_file.status == "processed":
      os.sys("clear")
			print("File processed")
			break

	fine_tune_job = openai.FineTuningJob.create(training_file=JSONL_file.id, model="gpt-3.5-turbo")

	while True:

		fine_tune_info = openai.FineTuningJob.retrieve(id=fine_tune_job.id)

    os.sys("clear")
    print("Fine-tuning.")
    time.sleep(1)
    os.sys("clear")
    print("Fine-tuning..")
    time.sleep(1)
    os.sys("clear")
    print("Fine-tuning...")
    time.sleep(1)

		if fine_tune_info.status == "succeeded":
			print("fine_tune_info.status)
			print("Fine-tuned model info", fine_tune_info)
			print("Model id", fine_tune_info.fine_tuned_model)

			break


if __name__ == '__main__':
	main()