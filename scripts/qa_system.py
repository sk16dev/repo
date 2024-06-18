import pysolr
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Initialize Solr connection
solr = pysolr.Solr('http://localhost:8983/solr/pdf_core', always_commit=True)

# Initialize T5 model and tokenizer
model_name = 't5-base'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def query_solr(question):
    results = solr.search(question, fl='content', rows=5)  # Adjust the fields and rows as needed
    return results

def generate_answer(question, context):
    input_text = f'question: {question} context: {context}'
    input_ids = tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
    outputs = model.generate(input_ids)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

if __name__ == "__main__":
    question = input("ask?")
    results = query_solr(question)
    for result in results:
        context = result['content']
        answer = generate_answer(question, context)
        print(f"Question: {question}")
        print(f"Answer: {answer}\n")
